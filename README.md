# Проект «API для Yatube»

## Описание
Проект API для практической работы.

## Технологии
* Python 3.8
* Django
* Django REST Framework

## Требования 
Django==2.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.2
Pillow==8.3.1
PyJWT==2.1.0
requests==2.26.0

Ключевые моменты:
Применены вьюсеты.
Для аутентификации использованы JWT-токены.
У неаутентифицированных пользователей доступ к API только на чтение. Исключение — эндпоинт /follow/.
Аутентифицированным пользователям разрешено изменение и удаление своего контента, в остальных случаях доступ предоставляется только для чтения.

# Примеры
Для доступа к API необходим токен.

Методы:
/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)
При отправке запроса передавайте токен в заголовке Authorization: Bearer <токен>

## Installation
Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке.

#Cоздать и активировать виртуальное окружение:
python3 -m venv venv
source env/bin/activate

Установить зависимости из файла requirements.txt:
pip install -r requirements.txt

#Выполнить миграции:
python manage.py makemigrations
python manage.py migrate

#Запустить проект:
python manage.py runserver
