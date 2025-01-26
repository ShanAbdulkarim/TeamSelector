import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fullgame.models import Players

class Command(BaseCommand):
    help = 'Bulk create players from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to read player data from')

    def handle(self, *args, **options):
        # Construct the full path to the CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'fullgame','management', 'data', options['csv_file'])
        
        if not os.path.exists(csv_file_path):
            raise CommandError(f"The file {csv_file_path} does not exist.")
        
        players_to_create = []

        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        # Create a new player instance
                        print(row)
                        player = Players(
                            firstname=row['Firstname'],
                            lastname=row['Lastname'],
                            nation=row['Nation'],
                            height=int(row['Height']),
                            weight=int(row['Weight']),
                            age=int(row['Age']),
                            overall=int(row['Overall']),
                            position=row['Position'],
                            speed=int(row['Speed']),
                            shooting=int(row['Shooting']),
                            passing=int(row['Passing']),
                            dribbling=int(row['Dribbling']),
                            defending=int(row['Defending']),
                            physical=int(row['Physical']),
                            gkrating=int(row['Gkrating']),
                        )
                        players_to_create.append(player)
                    except KeyError as e:
                        raise CommandError(f"Missing expected column in CSV: {e}")
                    except ValueError as e:
                        raise CommandError(f"Invalid data type for field in row {row}: {e}")
        except IOError:
            raise CommandError(f"Error reading file {csv_file_path}")

        # Bulk create the players in the database
        for player in players_to_create:
            player.save()

        

        
        self.stdout.write(self.style.SUCCESS('Successfully created players'))