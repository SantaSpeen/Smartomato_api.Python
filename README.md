# Smartomato_api

Language: RU, [EN](README_en.md)

## Use it!

* Импортируем:
```python
from smartomato import SmartTomato
```
* Инициализируем api:
```python
smartomato = SmartTomato(json_session_save=True, json_session_patch="./jsons/session.json")
```
| Параметр          | Тип  | По умолчанию | Обязательный параметр  | Описание |
| ------            | ---- | ------------ | :--------------------: | -------- |
| json_session_save | bool | False        | 	    🔴                | Сохранить ли файл сессии?  |
| json_session_patch| str  | "./session.json" | if json_session_save is True - ✔️ | Как и куда сохранить файл |

* Перед началом работ нужно залогинится (!)
```python
smartomato.login(login, password)
```
| Параметр          | Тип  | По умолчанию | Обязательный параметр  | Описание |
| ------            | ---- | ------------ | :--------------------: | -------- |
| login		           | str  | -	           | ✔️	                    | Your login    |
| password	         | str  | - 	          | ✔️	                    | Your password |

* Теперь пишите свой код:
  * Используйте `try` - `finally`:
    * В `try` пишите свой код
    * В `finally` должно быть `smartomato.logout()`
    
## Пример: 

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
