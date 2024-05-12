# BULLETIN BOARD

Данная работа представляет собой backend-часть для сайта объявлений.  

## Возможности:

#### Авторизация и аутентификация пользователей.
#### Распределение ролей между пользователями (пользователь и админ).
#### CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
#### Под каждым объявлением пользователи могут оставлять отзывы.
#### В заголовке сайта можно осуществлять поиск объявлений по названию.

## Запуск проекта через Docker:

#### 1. Установить и запустить на локальном или удаленном компьютере Docker.
#### 2. Клонировать репозиторий.
#### 3. Установить виртуальное окружение: 
####   python -m venv env
#### 4. Запустить виртуальное окружение: 
####   env\Scripts\activate
#### 5. Установить зависимости проекта, указанные в файле requirements.txt:
####   pip install -r requirements.txt
#### 6. Создать файл .env и ввести свои настройки как указано в файле .env.sample
#### 7. Создать и запустить контейнеры приложений в Docker с помощью команд: 
####   docker-compose build
####   docker-compose up

## Для авто-заполнения таблицы можете воспользоваться командами:

#### python manage.py csu (создание супер-пользователя)
#### python manage.py loadall (создание пользователей, объявлений и комментариев)
