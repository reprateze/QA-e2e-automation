import requests

from utils.config import API_BASE_URL


class BaseClient:
    DEFAULT_TIMEOUT = 10

    def __init__(self):
        self.base_url = API_BASE_URL
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        kwargs.setdefault("timeout", self.DEFAULT_TIMEOUT)
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        kwargs.setdefault("timeout", self.DEFAULT_TIMEOUT)
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        kwargs.setdefault("timeout", self.DEFAULT_TIMEOUT)
        url = f"{self.base_url}{endpoint}"
        return self.session.put(url, data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        kwargs.setdefault("timeout", self.DEFAULT_TIMEOUT)
        url = f"{self.base_url}{endpoint}"
        return self.session.delete(url, **kwargs)