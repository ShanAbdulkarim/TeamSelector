import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fullgame.models import Players, Teams


class Command(BaseCommand):
    help = 'Change Players Ratings'
    i = 0
    Teams = Teams.objects.all()
    for tim in Teams:
        print(tim.formation)