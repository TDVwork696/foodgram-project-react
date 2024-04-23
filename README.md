# Проект «foodgram-project»

![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

## О проекте:
Проект foodgram-project позволяет пользователям выкладывать рецепты готовых блюд, которые содержат в себе все нужные ингредиенты, время приготовления и описания блюда. Также в проекте можно добавлять нужные ингредиенты в корзину, чтобы совершать покупки более эффективно. В проекте можно подписываться на любимых авторов и выбирать избранные блюда.

## Использованные технологии:
- Язык програмирования - Python 3.9.10
- Фреймворк DRF
- СУБД - postgresql
- Docker

## Инструкция для развёртывания проекта:
- cd infra
- sudo docker compose -f docker-compose.yml up -d 
- sudo docker compose -f docker-compose.yml exec backend python manage.py migrate 
- sudo docker compose -f docker-compose.yml exec backend python manage.py collectstatic
- sudo docker compose -f docker-compose.yml exec backend cp -r /app/collected_static/. /backend_static/static/ 
- sudo docker compose -f docker-compose.yml exec backend python manage.py import_csv_to_db
## В проекте используются переменные окружения, чтобы использовать их ознакомтесь с файлом:
example.env

## Доступные endpiont:
### - Регистрация нового пользователя:
https://foodgramtdv.zapto.org/signup

### - Вход в систему:
https://foodgramtdv.zapto.org/signin

### - Смена пароля:
https://foodgramtdv.zapto.org/change-password

### - Главная страница со всеми рецептами:
https://foodgramtdv.zapto.org/recipes

### - Добавление нового рецепта:
https://foodgramtdv.zapto.org/recipes/create

### - Полное описание рецпта:
https://foodgramtdv.zapto.org/recipes/<id>

### - Редактирование рецепта:
https://foodgramtdv.zapto.org/recipes/<id>/edit

### - Подписки на избранных пользователей:
https://foodgramtdv.zapto.org/subscriptions

### - Избранные блюда:
https://foodgramtdv.zapto.org/favorites

### - Список необходимых покупок:
https://foodgramtdv.zapto.org/cart

## Об авторах:
https://github.com/TDVwork696
