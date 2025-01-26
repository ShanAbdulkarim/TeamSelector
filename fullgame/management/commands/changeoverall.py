import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fullgame.models import Players, Teams


class Command(BaseCommand):
    help = 'Change Players Ratings'

    def handle(self, *args, **options):
        player = Players.objects.get(firstname="Emilliano", lastname="Martinez")
        player.overall = 87
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Robin", lastname="Olsen")
        player.overall = 76
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Ezri", lastname="Konsa")
        player.overall = 81
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Pau", lastname="Torres") 
        player.overall = 81
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Diego", lastname="Carlos") 
        player.overall = 78
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Tyrone", lastname="Mings") 
        player.overall = 77
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Lucas", lastname="Digne") 
        player.overall = 78
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Matty", lastname="Cash") 
        player.overall = 76
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Ian", lastname="Maatsen")
        player.overall = 77
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Lamine", lastname="Bogarde")
        player.overall = 67
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Kosta", lastname="Nedeljkovic")
        player.overall = 69
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Amadou", lastname="Onana") 
        player.overall = 82
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Boubacar", lastname="Kamara") 
        player.overall = 81
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="John", lastname="McGinn") 
        player.overall = 82
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Youri", lastname="Tielemans") 
        player.overall = 79
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Ross", lastname="Barkley") 
        player.overall = 78
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Leon", lastname="Bailey") 
        player.overall = 80
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Emiliano", lastname="Buendia") 
        player.overall = 77
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Morgan", lastname="Rogers") 
        player.overall = 78
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Jaden", lastname="Philogene") 
        player.overall = 76
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Oliver", lastname="Watkins") 
        player.overall = 85
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Jhon", lastname="Duran") 
        player.overall = 81
        player.save()
        print(player.overall)
