import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fullgame.models import Teams

class Command(BaseCommand):
    help = 'Bulk create players from a CSV file'

    def handle(self, *args, **options):
        
        team_to_create = [{"name": "Arsenal", "rating":85, "formation":4231},
                          {"name": "Aston Villa", "rating":85, "formation":442},
                          {"name": "Brighton", "rating":85, "formation":4231},
                          {"name": "Bournemouth", "rating":85, "formation":4231},
                          {"name": "Brentford", "rating":85, "formation":532},
                          {"name": "Chelsea", "rating":85, "formation":4231},
                          {"name": "Crystal Palace", "rating":85, "formation":523},
                          {"name": "Everton", "rating":85, "formation":4411},
                          {"name": "Fulham", "rating":85, "formation":4231},
                          {"name": "Ipswich Town", "rating":85, "formation":4231},
                          {"name": "Leicester City", "rating":85, "formation":4231},
                          {"name": "Liverpool", "rating":85, "formation":4231},
                          {"name": "Manchester City", "rating":85, "formation":433},
                          {"name": "Manchester United", "rating":85, "formation":523},
                          {"name": "Newcastle United", "rating":85, "formation":433},
                          {"name": "Nottingham Forest", "rating":85, "formation":4231},
                          {"name": "Southampton", "rating":85, "formation":541},
                          {"name": "Tottenham Hotspur", "rating":85, "formation":4231},
                          {"name": "West Ham United", "rating":85, "formation":4231},
                          {"name": "Wolverhampton Wanderers", "rating":85, "formation":532},
        ]
        # Bulk create the players in the database
        for team_data  in team_to_create:
            team = Teams(**team_data)
            team.save()

        

        
        self.stdout.write(self.style.SUCCESS('Successfully created players'))