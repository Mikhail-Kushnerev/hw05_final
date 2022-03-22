# Yatube

## Социальная сеть для блоггеров

Cоциальная сеть для публикации личных дневников, где для размещения собственных постов необходимо создать свой уникальный профиль. После регистрации авторизованному пользователю на сайте будут доступны  
следующие возможности:

- сочинение текстов;
- добавление к посту картинки;
- оставление комментариев под постами других пользователей;
- подписываться на единомышленников.
Незарегестрированные пользователям доступны только главная страница со всеми постами всех пользователей и перемещение по авторам/группам/постам.

Для сайта предусмотрена возможность модерация записей и блокировка пользователей на слаучай спама.

## Технологии

- Django 2.2.16
- CSS
- HTML
- Python 3.10
- SQLite3

## Установка

- Склонируйте проект:

```
git clone https://github.com/Mikhail-Kushnerev/Social-Network-Yatube
```

- Установите виртуальное окружение, активируйте его:

```
python -m venv venv

(Windows)
source venv/Scripts/activate
```

- Проинсталлируйте необходимые зависимости и выполните миграции:

```
pip install -r requirements.txt
cd yatube -> python manage.py migrate
```

- Запустите проект:

```
python manage.py runserver
```

[![CI](https://github.com/yandex-praktikum/hw05_final/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw05_final/actions/workflows/python-app.yml)
