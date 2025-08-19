import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fullgame.models import Teams

class Command(BaseCommand):
    help = 'Bulk create players from a CSV file'

    def handle(self, *args, **options):
        
        team_to_create = [{"name": "Arsenal", "rating":85},
                          {"name": "Aston Villa", "rating":85},
                          {"name": "Bournemouth", "rating":85},
                          {"name": "Brentford", "rating":85},
                          {"name": "Brighton", "rating":85},
                          {"name": "Chelsea", "rating":85},
                          {"name": "Crystal Palace", "rating":85},
                          {"name": "Everton", "rating":85},
                          {"name": "Fulham", "rating":85},
                          {"name": "Ipswich Town", "rating":85},
                          {"name": "Leicester City", "rating":85},
                          {"name": "Liverpool", "rating":85},
                          {"name": "Manchester City", "rating":85},
                          {"name": "Manchester United", "rating":85},
                          {"name": "Newcastle", "rating":85},
                          {"name": "Nottingham Forest", "rating":85},
                          {"name": "Southampton", "rating":85},
                          {"name": "Tottenham", "rating":85},
                          {"name": "West Ham", "rating":85},
                          {"name": "Wolverhampton Wanderers", "rating":85}
        ]
        # Bulk create the players in the database
        for team_data  in team_to_create:
            team = Teams(**team_data)
            team.save()

        

        

        self.stdout.write(self.style.SUCCESS('Successfully created players'))
