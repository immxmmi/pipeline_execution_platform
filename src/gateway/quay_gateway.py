from gateway.client import ApiClient
from utils.logger import Logger as log


class QuayGateway:
    def __init__(self, client=None):
        self.client = client or ApiClient()

    def create_organization(self, name: str):
        payload = {"name": name}
        log.debug("QuayGateway", f"create_organization name={name}")
        log.debug("QuayGateway", f"create_organization args=({name},)")
        return self.client.post("/organization/", json=payload)

    def delete_organization(self, name: str):
        log.debug("QuayGateway", f"delete_organization name={name}")
        log.debug("QuayGateway", f"delete_organization args=({name},)")
        return self.client.delete(f"/organization/{name}")

    def get_organization(self, name: str):
        log.debug("QuayGateway", f"get_organization name={name}")
        log.debug("QuayGateway", f"get_organization args=({name},)")
        return self.client.get(f"/organization/{name}")

    def list_organizations(self):
        log.debug("QuayGateway", "list_organizations")
        log.debug("QuayGateway", "list_organizations args=()")
        return self.client.get("/organization")

    def create_robot_account(self, organization: str, robot_shortname: str, description: str | None = None):
        payload = {"description": description}
        log.debug("QuayGateway", f"create_robot_account org={organization} robot={robot_shortname} description={description}")
        log.debug("QuayGateway", f"create_robot_account args=({organization}, {robot_shortname}, {description})")
        try:
            return self.client.put(
                f"/organization/{organization}/robots/{robot_shortname}".rstrip("/"),
                json=payload
            )
        except Exception as e:
            msg = str(e)

            if "Existing robot with name" in msg:
                return {
                    "created": False,
                    "robot": f"{organization}+{robot_shortname}",
                    "reason": "already_exists"
                }

            if "Could not find robot" in msg:
                return {
                    "created": True,
                    "robot": f"{organization}+{robot_shortname}",
                    "reason": "precheck_missing"
                }

            raise

    def delete_robot_account(self, organization: str, robot_shortname: str):
        log.debug("QuayGateway", f"delete_robot_account org={organization} robot={robot_shortname}")
        log.debug("QuayGateway", f"delete_robot_account args=({organization}, {robot_shortname})")
        return self.client.delete(f"/organization/{organization}/robots/{robot_shortname}")

    def get_robot_account(self, organization: str, robot_shortname: str):
        log.debug("QuayGateway", f"get_robot_account org={organization} robot={robot_shortname}")
        log.debug("QuayGateway", f"get_robot_account args=({organization}, {robot_shortname})")
        try:
            return self.client.get(
                f"/organization/{organization}/robots/{robot_shortname}".rstrip("/")
            )
        except Exception as e:
            msg = str(e)

            if "Could not find robot" in msg or "404" in msg:
                return {
                    "exists": False,
                    "organization": organization,
                    "robot": robot_shortname,
                    "reason": "not_found"
                }

            if "Existing robot with name" in msg:
                return {
                    "exists": True,
                    "organization": organization,
                    "robot": robot_shortname,
                    "reason": "already_exists"
                }

            return {
                "exists": False,
                "organization": organization,
                "robot": robot_shortname,
                "reason": "api_error",
                "error": msg
            }

    def list_robot_accounts(self, organization: str):
        log.debug("QuayGateway", f"list_robot_accounts org={organization}")
        log.debug("QuayGateway", f"list_robot_accounts args=({organization},)")
        return self.client.get(f"/organization/{organization}/robots/")
