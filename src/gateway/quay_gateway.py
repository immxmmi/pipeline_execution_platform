from gateway.client import ApiClient


class QuayGateway:
    def __init__(self, client=None):
        self.client = client or ApiClient()

    def create_organization(self, name: str):
        payload = {"name": name}
        return self.client.post("/organization/", json=payload)

    def delete_organization(self, name: str):
        return self.client.delete(f"/organization/{name}")

    def get_organization(self, name: str):
        return self.client.get(f"/organization/{name}")

    def list_organizations(self):
        return self.client.get("/organization/")
