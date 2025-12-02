from gateway.quay_gateway import QuayGateway
from model.action_response import ActionResponse
from model.organization_model import GetOrganization


class GetOrganizationAction:
    def __init__(self, gateway=None):
        self.gateway = gateway or QuayGateway()

    @staticmethod
    def exists(name: str) -> bool:
        try:
            gateway = QuayGateway()
            result = gateway.get_organization(name)
            return result is not None
        except Exception as e:
            if "404" in str(e):  # NOT FOUND means it does not exist
                return False
            raise e

    def execute(self, data: dict) -> ActionResponse:
        try:
            print(f"[GetOrganizationAction] Executing with data: {data}")
            org = GetOrganization(**data)
            print(f"[GetOrganizationAction] Filtered model data: {org.model_dump()}")
            result = self.gateway.get_organization(org.name)

            return ActionResponse(
                success=True,
                message="Organization fetched successfully",
                data={"organization": org.name, "result": result}
            )

        except Exception as e:
            return ActionResponse(
                success=False,
                message=str(e)
            )
