from gateway.quay_gateway import QuayGateway
from model.action_response import ActionResponse
from model.organization_model import DeleteOrganization


class DeleteOrganizationAction:
    def __init__(self, gateway=None):
        self.gateway = gateway or QuayGateway()

    def execute(self, data: dict) -> ActionResponse:
        try:
            org = DeleteOrganization(**data)
            result = self.gateway.delete_organization(org.name)

            return ActionResponse(
                success=True,
                message="Organization deleted successfully",
                data={"organization": org.name, "result": result}
            )

        except Exception as e:
            return ActionResponse(
                success=False,
                message=str(e)
            )
