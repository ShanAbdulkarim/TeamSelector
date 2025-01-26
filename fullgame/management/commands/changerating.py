import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fullgame.models import Players, Teams


class Command(BaseCommand):
    help = 'Change Players Ratings'

    def handle(self, *args, **options):
        player = Players.objects.get(firstname="Jose", lastname="Sa")
        player.tradevalue = 2
        player.overall = 78
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Sam", lastname="Johnstone")
        player.tradevalue = 2
        player.overall = 78
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Toti", lastname="Gomes")
        player.tradevalue = 2
        player.overall = 75
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Yerson", lastname="Mosquera") 
        player.tradevalue = 2
        player.overall = 76
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Nelson", lastname="Semedo") 
        player.tradevalue = 2
        player.overall = 75
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Rayan", lastname="Ait Nouri") 
        player.tradevalue = 2
        player.overall = 76
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Craig", lastname="Dawson") 
        player.tradevalue = 1.5
        player.overall = 75
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Matt", lastname="Doherty") 
        player.tradevalue = 2
        player.overall = 76
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Pedro", lastname="Lima")
        player.tradevalue = 1.5
        player.overall = 72
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Santiago", lastname="Bueno")
        player.tradevalue =2
        player.overall = 75
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Andre", lastname="Trinidade")
        player.tradevalue = 2.5
        player.overall = 77
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Mario", lastname="Lemina") 
        player.tradevalue = 4
        player.overall = 83
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Joao", lastname="Gomes") 
        player.tradevalue = 4
        player.overall = 82
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Boubacar", lastname="Traore") 
        player.tradevalue = 2
        player.overall = 75
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Jean-Ricner", lastname="Bellegarde") 
        player.tradevalue = 2.5
        player.overall = 78
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Carlos", lastname="Forbs") 
        player.tradevalue = 2
        player.overall = 73
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Rodrigo", lastname="Gomes") 
        player.tradevalue = 2
        player.overall = 75
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Pablo", lastname="Sarabia") 
        player.tradevalue = 1.5
        player.overall = 77
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Goncalo", lastname="Guedes") 
        player.tradevalue = 2
        player.overall = 76
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Hwang", lastname="Hee Chan") 
        player.tradevalue = 3
        player.overall = 79
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Jorgen", lastname="Strand Larsen") 
        player.tradevalue = 3.5
        player.overall = 81
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Matheus", lastname="Cunha") 
        player.tradevalue = 4.5
        player.overall = 84
        player.save()
        print(player.overall)
        player = Players.objects.get(firstname="Tommy", lastname="Doyle") 
        player.tradevalue = 2
        player.overall = 75
        player.save()
        print(player.overall)
