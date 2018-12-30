from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from core.models import Shoe
from django.core.files import File

def get_path(file):
    return os.path.join(settings.BASE_DIR, 'initial_data', file)

class Command(BaseCommand):
    help = "Load dogs from initial_data/shoes.csv"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print("Deleting shoes...")
        Shoe.objects.all().delete()
        with open(get_path('shoes.csv'), 'r') as file:
            reader = csv.DictReader(file)
            i = 0
            for row in reader:
                i += 1
                shoe = Shoe(
                    name=row['name'],
                    description=row['description'],
                    color=row['color'],
                    size=row['size'],
                    is_jordan=row['is_jordan'],
                    is_van=row['is_van'],
                    is_yeezy=row['is_yeezy'],
                    is_airmax=row['is_airmax'],
                    is_airforce=row['is_airforce'],
                    slug=row['slug'],
        
                )
                shoe.picture.save(row['picture'],
                                  File(open(get_path(row['picture']), 'rb')))
                # if shoe not in Shoe.objects.all():
                shoe.save()
        print(f"{i} shoes loaded!")
