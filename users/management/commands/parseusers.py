from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Парсинг пользователей из users.csv'

    def handle(self, *args, **kwargs):
        pass
        