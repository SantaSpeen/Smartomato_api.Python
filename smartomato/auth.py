import traceback

import requests

from local_libs import JsonHandler
from smartomato.Exceptions import AuthorizationFailed

json_session: JsonHandler


class SmartTomatoAuth:

    AUTH_URL = "http://smartomato.ru/api/session"

    def __init__(self,
                 login: str,
                 password: str,
                 session=requests.Session(),
                 save_session: bool = False,
                 session_patch: str = "./jsons/session.json"):
        global json_session
        if save_session:
            json_session = JsonHandler(patch=session_patch, file=True)
        self._login = login
        self._password = password
        self.S = session
        self.save_session = save_session
        self.login_form = f"?login={login}&password={password}"

        self.have_token = False

    @classmethod
    def out_handler(cls, out: requests.models.Response) -> dict:
        try:
            return out.json()
        except:
            print(traceback.format_exc())
            raise AuthorizationFailed("Incorrect login or password..")

    def login(self) -> dict:
        out = self.out_handler(self.S.post(self.AUTH_URL + self.login_form))
        if self.save_session:
            json_session.save(out)
        if out.get("meta"):
            self.S.headers.update({"Authorization": f'Token token="{out["meta"]["token"]}"'})
            self.have_token = True
        return out

    def status(self) -> dict:
        if self.have_token:
            out = self.S.get(self.AUTH_URL)
            return self.out_handler(out)
        return {}

    def is_login(self) -> bool:
        if self.have_token:
            if self.status().get("meta"):
                return True
        return False

    def logout(self) -> bool:
        if self.have_token:
            self.S.delete(self.AUTH_URL)
            if self.save_session:
                json_session.save({})
            return True
        return False
