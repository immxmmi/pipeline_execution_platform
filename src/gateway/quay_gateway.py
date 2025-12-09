from gateway.client import ApiClient


class QuayGateway:
    def __init__(self, client=None):
        self.client = client or ApiClient()

    def create_organization(self, name: str):
        payload = {"name": name}
        if self.client.cfg.debug:
            print(f"[DEBUG] create_organization name={name}")
        if self.client.cfg.debug:
            print(f"[DEBUG] QuayGateway.create_organization called with args: ({name},)")
        return self.client.post("/organization", json=payload)

    def delete_organization(self, name: str):
        if self.client.cfg.debug:
            print(f"[DEBUG] delete_organization name={name}")
        if self.client.cfg.debug:
            print(f"[DEBUG] QuayGateway.delete_organization called with args: ({name},)")
        return self.client.delete(f"/organization/{name}")

    def get_organization(self, name: str):
        if self.client.cfg.debug:
            print(f"[DEBUG] get_organization name={name}")
        if self.client.cfg.debug:
            print(f"[DEBUG] QuayGateway.get_organization called with args: ({name},)")
        return self.client.get(f"/organization/{name}")

    def list_organizations(self):
        if self.client.cfg.debug:
            print("[DEBUG] list_organizations")
        if self.client.cfg.debug:
            print(f"[DEBUG] QuayGateway.list_organizations called with args: ()")
        return self.client.get("/organization")

    def create_robot_account(self, organization: str, robot_shortname: str, description: str | None = None):
        payload = {"description": description}
        if self.client.cfg.debug:
            print(f"[DEBUG] create_robot_account org={organization} robot={robot_shortname} description={description}")
        if self.client.cfg.debug:
            print(f"[DEBUG] QuayGateway.create_robot_account called with args: ({organization}, {robot_shortname}, {description})")
        return self.client.put(
            f"/organization/{organization}/robots/{robot_shortname}",
            json=payload
        )

    def delete_robot_account(self, organization: str, robot_shortname: str):
        if self.client.cfg.debug:
            print(f"[DEBUG] delete_robot_account org={organization} robot={robot_shortname}")
        if self.client.cfg.debug:
            print(f"[DEBUG] QuayGateway.delete_robot_account called with args: ({organization}, {robot_shortname})")
        return self.client.delete(f"/organization/{organization}/robots/{robot_shortname}")

    def get_robot_account(self, organization: str, robot_shortname: str):
        if self.client.cfg.debug:
            print(f"[DEBUG] get_robot_account org={organization} robot={robot_shortname}")
        if self.client.cfg.debug:
            print(f"[DEBUG] QuayGateway.get_robot_account called with args: ({organization}, {robot_shortname})")
        return self.client.get(f"/organization/{organization}/robots/{robot_shortname}")

    def list_robot_accounts(self, organization: str):
        if self.client.cfg.debug:
            print(f"[DEBUG] list_robot_accounts org={organization}")
        if self.client.cfg.debug:
            print(f"[DEBUG] QuayGateway.list_robot_accounts called with args: ({organization},)")
        return self.client.get(f"/organization/{organization}/robots/")
