from api_steps.api_client import ApiClient


class BaseApi:
    def __init__(self, api_requests: ApiClient):
        self._requests = api_requests
