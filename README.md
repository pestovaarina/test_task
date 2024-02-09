## Инструкция по запуску:
1. Клонировать репозиторий себе на компьютер
```
git clone git@github.com:pestovaarina/test_task.git
``` 
2. Создать и активировать виртуальное окружение
- На Windows
```
python -m venv venv
source venv/Scripts/activate
``` 
- На Mac
```
python -m venv venv
source venv/bin/activate
``` 
3. Установить зависимости из файла requirements.txt
```
python -m pip install --upgrade pip
pip install -r requirements.txt
``` 
4. Создать и выполнить миграции:
```
python manage.py makemigrations
python manage.py migrate
``` 
5. Создать суперпользователя:
``` 
python manage.py createsuperuser
```
6. Запустить проект:
``` 
python manage.py runserver
``` 
7. Документация к проекту доступна по адресу http://127.0.0.1:8000/api/docs/
8. Просмотр постов доступен всем. Публикация, изменение и удаление постов доступны только зарегистрированным пользователям.
Изменять и удалять посты может только автор этих постов.
