# Notes Console

Приложение представляет собой менеджер заметок, где пользователь может создавать, хранить, искать и удалять заметки. Для хранения данных используется база данных - SQLite.


## Установка и настройка
Установите нужные зависимости:
```
pip install -r requirements.txt
```
Запустите приложение:
```
python run.py
```

### Требования 
![Python 3.8+](https://cdn.icon-icons.com/icons2/2699/PNG/96/python_vertical_logo_icon_168039.png)


## Структура проекта
```
.flake8
[console]
    ├── [database]
        ├── db.py
        └── __init__.py
    ├── menu.py
    ├── [models]
        ├── note.py
        └── __init__.py
    ├── notes.db
    ├── [utils]
        ├── utils.py
        └── __init__.py
    └── __init__.py
README.md
requirements.txt
run.py
```
