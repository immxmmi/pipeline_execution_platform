import requests

from config.loader import Config


class ApiClient:
    def __init__(self):
        cfg = Config()
        self.base_url = cfg.base_url.rstrip('/')
        self.headers = {'Content-Type': 'application/json'}
        if cfg.token:
            self.headers['Authorization'] = f'Bearer {cfg.token}'

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        response.raise_for_status()
        return response.json() if response.text else {}

    def get(self, endpoint, **kwargs):
        return self.request('GET', endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request('POST', endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request('PUT', endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request('DELETE', endpoint, **kwargs)
