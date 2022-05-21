# api_final
api final

Проект «API для Yatube»

# Описание

Проект API для практической работы yatube.

#Ключевые моменты:
Применены вьюсеты.
Для аутентификации использованы JWT-токены.
У неаутентифицированных пользователей доступ к API только на чтение. Исключение — эндпоинт /follow/.
Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.

# Примеры
Для доступа к API необходим токен: 
Нужно выполнить POST-запрос localhost:8000/api/v1/token/ передав поля username и password. API вернет JWT-токен

#Методы:
/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)
При отправке запроса передавайте токен в заголовке Authorization: Bearer <токен>
## Installation
#Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке.

#Cоздать и активировать виртуальное окружение:
python3 -m venv env
source env/bin/activate

#Установить зависимости из файла requirements.txt:
python3 -m pip install --upgrade pip
pip install -r requirements.txt

#Выполнить миграции:
python3 manage.py migrate

#Запустить проект:
python3 manage.py runserver
