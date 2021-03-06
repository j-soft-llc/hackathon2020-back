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
    

# Лидеры
Запрос требует авторизации

**/leaders/** и **/leaders/id/** Возвращают список лидеров и одного лидера соответственно.

    {
      "сompetencies": [
        {
          "id": 1,
          "name": "Категория1",
          "vote_count": 83
        },
        {
          "id": 2,
          "name": "Категория 2",
          "vote_count": 59
        },
        {
          "id": 3,
          "name": "Категория 3",
          "vote_count": 192
        }
      ],
      "location": {
        "name": "Варавино-Фактория",
        "lat": "",
        "long": ""
      },
      "avatar_link": "https://sun9-68.userapi.com/lkSq4CcUprbvWx4bAB2LWuHBlC1DaRUEtP8Mtg/FascrZ9jdTw.jpg",
      "first_name": "Имя",
      "middle_name": "Отчество",
      "second_name": "Фамилия",
      "age": 37,
      "profession": null,
      "vk_id": "316000",
      "id": 31
    }

**vote_count - фейковое количество голосов**

# Инициативы
Запрос требует авторизации

**/leaders/initiative/** - Возвращает список инициатив.
**/leaders/initiative/id/** - Возвращают инициативу с соответствующим id.

**/leaders/user_initiative/user_id=id** - Возвращает инициативы пользователя с соответствующим id (Если не указывать get-параметр, то текущего пользователя).




    [
        {
            "id": 1,
            "initiative_text": "Test",
            "leader": null,
            "category": null,
            "initiative_type": "appeal",
            "owner": null,
            "photo": [
                {
                    "photo": "http://127.0.0.1:8000/media/uploads/initiative/3e7365d4e13c4f889bc156eb05057bab.jpg"
                },
                {
                    "photo": "http://127.0.0.1:8000/media/uploads/initiative/63a58cb7385d4c9e892dcfe07994f571.jpg"
                }
            ]
        },
        {
            "id": 2,
            "initiative_text": "Test 2",
            "leader": null,
            "category": null,
            "initiative_type": "appeal",
            "owner": 1,
            "photo": []
        },
        {
            "id": 3,
            "initiative_text": "Test 3",
            "leader": null,
            "category": null,
            "initiative_type": "appeal",
            "owner": 1,
            "photo": [
                {
                    "photo": "http://127.0.0.1:8000/media/uploads/initiative/475bd687b27944da93804c002faa8b4d.jpg"
                }
            ]
        },
        {
            "id": 4,
            "initiative_text": "Test 4",
            "leader": 2,
            "category": 1,
            "initiative_type": "appeal",
            "owner": 2,
            "photo": []
        }
    ]

**initiative_type** - Тип инициативы
1. appeal - Обращение
2. complaint - Жалоба