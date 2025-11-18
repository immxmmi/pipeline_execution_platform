from actions.create_organization import CreateOrganizationAction
from actions.delete_organization import DeleteOrganizationAction
from actions.get_organization import GetOrganizationAction
from actions.list_organizations import ListOrganizationsAction

ACTION_REGISTRY = {
    "create_organization": CreateOrganizationAction,
    "delete_organization": DeleteOrganizationAction,
    "get_organization": GetOrganizationAction,
    "list_organizations": ListOrganizationsAction,
} 