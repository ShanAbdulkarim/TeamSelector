import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fullgame.models import Players, Teams, Formations

class Command(BaseCommand):
    help = 'Bulk remove players from their team'

    def handle(self, *args, **options):

        formation_data = [
        {"formation_style": "3223", "name": 'Default Formation'},
        {"formation_style": "3412", "name": 'Default Formation'},
        {"formation_style": "352", "name": 'Default Formation'},
        {"formation_style": "3142", "name": 'Default Formation'},
        {"formation_style": "3421", "name": 'Default Formation'},
        {"formation_style": "343", "name": 'Default Formation'},
        {"formation_style": "4321", "name": 'Default Formation'},
        {"formation_style": "4231", "name": 'Default Formation'},
        {"formation_style": "442", "name": 'Default Formation'},
        {"formation_style": "442", "name": 'Diamond'},
        {"formation_style": "442", "name": 'Diamond Wide'},
        {"formation_style": "4222", "name": 'Default Formation'},
        {"formation_style": "4312", "name": 'Default Formation'},
        {"formation_style": "451", "name": 'Default Formation'},
        {"formation_style": "4141", "name": 'Default Formation'},
        {"formation_style": "4411", "name": 'Default Formation'},
        {"formation_style": "433", "name": 'Default Formation'},
        {"formation_style": "433", "name": 'Defense'},
        {"formation_style": "433", "name": 'Attack'},
        {"formation_style": "424", "name": 'Default Formation'},
        {"formation_style": "541", "name": 'Default Formation'},
        {"formation_style": "532", "name": 'Default Formation'},
        {"formation_style": "523", "name": 'Default Formation'},
        {"formation_style": "5212", "name": 'Default Formation'},
        ]

        for formation in formation_data:
            Formations.objects.create(
                name=formation["name"],
                formation_style=formation["formation_style"]
            )
