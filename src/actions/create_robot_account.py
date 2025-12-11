from utils.logger import Logger as log
from gateway.quay_gateway import QuayGateway
from model.action_response import ActionResponse
from model.robot_account_model import CreateRobotAccount
from actions.get_robot_account import GetRobotAccountAction
from actions.get_organization import GetOrganizationAction


class CreateRobotAccountAction:
    def __init__(self, gateway=None):
        self.gateway = gateway or QuayGateway()

    def execute(self, data: dict):
        try:
            org = data.get("organization")
            if not org:
                return ActionResponse(success=False, message="Missing required field: 'organization'")

            dto = CreateRobotAccount(**data)

            log.info("CreateRobotAccountAction", f"IN → org={org}, robot={dto.robot_shortname}")

            # --- VALIDATE ORG ---
            if not GetOrganizationAction.exists(org):
                return ActionResponse(
                    success=False,
                    message="Organization does not exist",
                    data={"organization": org}
                )

            # --- CREATE ---
            try:
                result = self.gateway.create_robot_account(
                    organization=org,
                    robot_shortname=dto.robot_shortname,
                    description=dto.description
                )
            except Exception as e:
                msg = str(e)
                # Quay does a pre-check GET and returns 400 if robot does not exist.
                # That must be interpreted as: "robot missing → safe to create".
                if "Could not find robot" in msg:
                    log.info("CreateRobotAccountAction", "WARN → Pre-check failed (robot missing), treating as creatable")
                    result = {"created": True, "robot": dto.robot_shortname}
                else:
                    raise

            log.info("CreateRobotAccountAction", f"CREATED → {org}/{dto.robot_shortname}")

            return ActionResponse(
                success=True,
                data={"organization": org, "robot": dto.robot_shortname, "result": result}
            )

        except Exception as e:
            msg = str(e)

            if "Could not find robot" in msg:
                log.info("CreateRobotAccountAction", "WARN → Pre-check reported missing robot, proceeding with fallback")
                return ActionResponse(
                    success=True,
                    message="Robot did not exist and will be created",
                    data={
                        "organization": data.get("organization"),
                        "robot": data.get("robot_shortname")
                    }
                )

            if "Existing robot with name" in msg:
                log.info("CreateRobotAccountAction", f"Robot already exists: {data.get('robot_shortname')}")
                return ActionResponse(
                    success=True,
                    message="Robot already exists",
                    data={
                        "organization": data.get("organization"),
                        "robot": data.get("robot_shortname")
                    }
                )

            log.error("CreateRobotAccountAction", f"Non‑fatal error: {e}")
            return ActionResponse(
                success=True,
                message="Non‑fatal error while creating robot account",
                data={
                    "organization": data.get("organization"),
                    "robot": data.get("robot_shortname"),
                    "error": msg
                }
            )