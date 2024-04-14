import contextlib
import csv
from os import path

from django.core.management.base import BaseCommand, CommandError

from recipes.models import Ingredient

PATH = "csv/"


class Import:

    model = None

    def __init__(self, name_file):
        self.file = path.join(PATH, name_file)
        self.list_models_instances = []

    def create_list(self, row):
        raise NotImplementedError(
            'Нужно реализовать этот метод в подклассах'
        )

    def import_data(self):
        with self.open_file() as file:
            next(file).rstrip().split(',')
            reader = csv.reader(file)
            for row in reader:
                self.create_list(row)
            self.model.objects.bulk_create(self.list_models_instances)

    @contextlib.contextmanager
    def open_file(self):
        self.file = open(self.file, mode='r')
        try:
            yield self.file
        finally:
            self.file.close()


class ImportIngredient(Import):

    model = Ingredient

    def create_list(self, row):
        name, measurement_unit = row
        self.list_models_instances.append(self.model(
            name=name,
            measurement_unit=measurement_unit)
        )


TABLE_FOR_IMPORT = {
    ImportIngredient: 'ingredients.csv',

}


class Command(BaseCommand):
    help = 'Import data from csv to db'

    def handle(self, *args, **options):
        try:
            for import_class, import_file in TABLE_FOR_IMPORT.items():
                import_class(import_file).import_data()

        except FileNotFoundError:
            raise CommandError(f'File not found {import_file}')
        except Exception as e:
            raise CommandError(f'Error processing file: {str(e)}')
