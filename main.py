from smartomato import SmartTomato

LOGIN = ""
PASSWORD = ""

smartomato = SmartTomato(json_session_save=True, json_session_patch="./jsons/session.json")
smartomato.login(LOGIN, PASSWORD)

try:
    r = smartomato.get.organizations()
    print(r)
finally:
    print("\nLogout..")
    smartomato.logout()
