# Smartomato_api

## Use it!

* Import:
```python
from smartomato import SmartTomato
```
* Init api:
```python
smartomato = SmartTomato(json_session_save=True, json_session_patch="./jsons/session.json")
```
| Params            | Type | Default | Necessarily  |  Description |
| ------            | ---- | ------- | :----------: | ------------- |
| json_session_save | bool | False   | 	    🔴      | Save or not save session file |
| json_session_patch| str  | "./session.json" | if json_session_save is True - ✔️ | File to save session |

* Login
```python
smartomato.login(login, password)
```
| Params            | Type | Default | Necessarily  |  Description |
| ------            | :--: | :-----: | :----------: | ------------ |
| login		    | str  | -	     | ✔️	    | Your login    |
| password	    | str  | - 	     | ✔️	    | Your password |

* Write your code:
  * Use `try` - `finally`:
    * In `try` do your code
    * In `finally` do `smartomato.logout()`
    
## Example: 

```python
from smartomato import SmartTomato

LOGIN = ""
PASSWORD = ""

smartomato = SmartTomato(json_session_save=True, json_session_patch="./jsons/session.json")
smartomato.login(LOGIN, PASSWORD)

try:
    # [Your's code]
     r = smartomato.get.organizations()
    print(r)
finally:
    print("\nLogout..")
    smartomato.logout()
```
