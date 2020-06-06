from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Парсинг пользователей из users.csv'

    def handle(self, *args, **kwargs):
        pass
        

class CsvParser:

    def __init__(self, path, delimiter=','):
        self.path = path
        self.delimiter = delimiter

    def parse(self):
        with open(self.path) as csv_file:
            return []