import requests

from .Exceptions import UnknownRequestType, ApiError
from .auth import SmartTomatoAuth


class APIMethod:
    __slots__ = ['_api_session', '_method_name']

    def __init__(self, api_session, method_name):
        self._api_session = api_session
        self._method_name: str = method_name

    def __getattr__(self, method_name):
        AvailableTypesRequestType = ["get", "post", "put", "delete"]
        if self._method_name.lower() not in AvailableTypesRequestType:
            raise UnknownRequestType("Unknown Request Type: " + self._method_name)
        return APIMethod(self._api_session, {"rq_type": self._method_name, "resource": method_name})

    def __call__(self, **method_kwargs):
        return self._api_session(self._method_name, **method_kwargs)


class SmartTomato:

    API_URL = "http://smartomato.ru/api/"

    def __init__(self, json_session_save: bool = False, json_session_patch: str = "./session.json") -> None:
        self.session: requests.Session = requests.Session()
        self.session.headers['Content-Type']: str = "application/json"

        self.auth: SmartTomatoAuth = SmartTomatoAuth("", "")

        self.json_session_save: bool = json_session_save
        self.json_session_patch: str = json_session_patch

    def __call__(self, method, **kwargs) -> any:
        url, kw = self.create_link(method, **kwargs)
        response = self.response_make(method, url, kw)
        return self.response_handler(response, method["rq_type"])

    def __getattr__(self, method) -> APIMethod:

        return APIMethod(self, method)

    def login(self, login: str, password: str):
        self.auth = SmartTomatoAuth(login, password, self.session, self.json_session_save, self.json_session_patch)
        self.auth.login()

    def create_link(self, method: dict, **kw) -> tuple:
        resource = method.get("resource")
        to_request = self.API_URL + resource
        if kw.get("id"):
            to_request += "/" + str(kw["id"])
            kw.pop("id")
            if kw.get("action"):
                to_request += "/" + str(kw["action"])
                kw.pop('action')
        return to_request, kw

    def response_make(self, method, url, kw):
        rq_type = method['rq_type']
        if rq_type == "get":
            args = "?"
            for k in kw:
                args += "&" + k + "=" + str(kw[str(k)])

            return self.session.get(url + args)

        elif rq_type == "post":
            return self.session.post(url, kw)
        elif rq_type == "put":
            return self.session.put(url, kw)
        elif rq_type == "delete":
            return self.session.delete(url)

    @classmethod
    def response_handler(cls, r: requests.Response, rq_type: str):
        r_code = r.status_code
        if r_code == 200:
            return r.json()
        elif r_code == 404:
            raise ApiError(f"Could not get request: '{rq_type.upper()} {r.url.replace('http://smartomato.ru', '')}'")
        else:
            return r.text

    def logout(self):

        self.auth.logout()
