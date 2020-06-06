# hackathon2020-back

# Первичный запуск проекта

1.  Из папки **docker** копируем файл local_settings в /config, и переименовываем в **local_settings.py**

2. В корне проекта запускаем docker-compose up

## Особенности вторичного запуска
В принципе их нет, миграции стартуют при старте, однако если добавили новую библиотеку, то необходимо пересобрать контейнер, запускаем **docker-compose up --build**

## Вход в контейнер

**docker exec -it hackathon2020-back_django_1 bash** - mange.py лежит внутри папки udem


# REST API

## Авторизация

Авторизация происходит через заголовок **Authorization** токен указывается в формате **Token token_key**
пример **Authorization: Token b4e9c971b940ca7e74cad0173b5924ed2c5194ac**

## Получение токена

Пока есть два роута /auth/user/ и auth/leader/, которые по get запросу возвращают токены в формате **{'token': 'key'}**

# Категории

Все запросы требуют авторизации

## Получение абсолютно всех категорий
**/leaders/all_categories/**

       [
      {
        "id": 1,
        "name": "Коммуналка",
        "children": [
          {
            "id": 4,
            "name": "Водоснабжение"
          },
          {
            "id": 5,
            "name": "Тепло"
          }
        ]
      },
      {
        "id": 2,
        "name": "Благоустройство",
        "children": [
          {
            "id": 7,
            "name": "Дороги"
          }
        ]
      },
    ]

## Получение только категорий верхнего уровня
**/leaders/categories/**

    [
      {
        "id": 1,
        "name": "Коммуналка"
      },
      {
        "id": 2,
        "name": "Благоустройство"
      },
      {
        "id": 3,
        "name": "Соц. сфера"
      }
    ]

## Получение одной категории (вместе с дочерними)
**/leaders/category/1/**

    {
      "id": 1,
      "name": "Коммуналка",
      "children": [
        {
          "id": 4,
          "name": "Водоснабжение"
        },
        {
          "id": 5,
          "name": "Тепло"
        }
      ]
    }

# Области
Запрос требует авторизации

**/leaders/geo/**

    [
      {
        "id": 1,
        "name": "Киров",
        "children": [
          {
            "id": 2,
            "name": "Ленинский район",
            "children": [
              {
                "id": 3,
                "name": "Лесная д. 12",
                "children": []
              }
            ]
          }
        ]
      }
    ]