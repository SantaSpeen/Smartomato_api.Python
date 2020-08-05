from smartomato import SmartTomatoAuth

LOGIN = ""
PASSWORD = ""

auth = SmartTomatoAuth(LOGIN, PASSWORD)

login = auth.login()
print(login)

is_login = auth.is_login()
print(is_login)

status = auth.status()
print(status)

logout = auth.logout()
print(logout)
