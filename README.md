# hackathon2020-back

## Первичный запуск проекта

1.  Из папки **docker** копируем файл local_settings в  /udem/udem, и переименовываем в **local_settings.py**

2. В корне проекта запускаем docker-compose up

## Особенности вторичного запуска
В принципе их нет, миграции стартуют при старте, однако если добавили новую библиотеку, то необходимо пересобрать контейнер, запускаем **docker-compose up --build**

## Вход в контейнер

**docker exec -it hackathon2020-back_django_1 bash** - mange.py лежит внутри папки udem