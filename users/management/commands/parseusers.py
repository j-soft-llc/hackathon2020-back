from django.core.management.base import BaseCommand
from django.conf import settings
from users.models import User


class Command(BaseCommand):
    help = 'Парсинг пользователей из users.csv'

    def handle(self, *args, **kwargs):
        # Создаем csv парсер
        csv = CsvParser(settings.BASE_DIR + '/users.csv')
        users_data = list(csv.parse())[1:]
        # Получаем список имеющихся пользователей
        isset_usernames = [user.username for user in User.objects.all()]
        # Убираем имеющиеся
        users_data = [user for user in users_data if user[1] not in isset_usernames]
        # Создаем массив с новыми пользователями
        users = []
        for user_data in users_data:
            user = User(
                username=user_data[1],
                avatar_link=user_data[0],
                vk_id=user_data[1],
                instagram_id=user_data[2],
                first_name=user_data[3],
                second_name=user_data[4],
                age=int(user_data[6]),
            )
            user.set_password('password')
            users.append(user)
        # Добавляем пользователей
        User.objects.bulk_create(users)
        self.stdout.write('Добавлено %i' % len(users))


class CsvParser:

    def __init__(self, path, delimiter=','):
        self.path = path
        self.delimiter = delimiter

    def parse(self):
        with open(self.path) as csv_file:
            for line in csv_file:
                yield line.split(',')
