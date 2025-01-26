import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fullgame.models import Players, Teams

class Command(BaseCommand):
    help = 'Bulk remove players from their team'

    def handle(self, *args, **options):
        bam = Players.objects.all()
        for i in bam:
            if (i.team != None):
                
                print(i.firstname)
                print(i.lastname)
                print(i.id)
                print(i.team)
                i.team = None
                i.save()
                print(i.team)

        blam = Teams.objects.all()
        for b in blam:
            if(b.selected == True):
                print(b.name)
            
        teams = Teams.objects.all()
        for tim in teams:
            if tim.selected:
                tim.selected = False
                tim.save()