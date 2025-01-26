import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from fullgame.models import Players, Teams, Formation


def add_arguments(self, parser):
        parser.add_argument('team_id', type=int, help="ID of the team to assign roles.")

def handle(self, *args, **kwargs):
    team_id = kwargs['team_id']

    try:
            # Fetch the specified team
        team = Teams.objects.get(id=team_id)
        self.stdout.write(f"Assigning roles for team: {team.name}")

         # Fetch players sorted by overall rating
        players = Players.objects.all().order_by('-overall')

         # Define your role allocation logic
        starting_xi = 11
        bench_size = 7

        # Clear any existing formations for the team (optional)
        Formation.objects.filter(team=team).delete()

        for i, player in enumerate(players):
            if i < starting_xi:
                role = 'starting'
            elif i < starting_xi + bench_size:
                role = 'bench'
            else:
                role = 'reserve'

         # Create a Formation entry for the player
        Formation.objects.create(team=team, player=player, role=role)

        self.stdout.write(self.style.SUCCESS("Roles successfully assigned!"))

    except Teams.DoesNotExist:
        self.stdout.write(self.style.ERROR(f"Team with ID {team_id} does not exist."))