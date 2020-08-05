# Smartomato_api

## For now works only auth!

## Use it!
```python
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

```
<p align="left">
	<img src="/static/img/example.jpg">
</p>