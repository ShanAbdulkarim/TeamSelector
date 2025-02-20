from django.shortcuts import render, get_object_or_404, redirect
from .models import Players, Teams, SavedGame
from .forms import teampicker
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import json

# These variables are global and used throughout multiple views in the progam.
import random
team_number = 0
pick = 0
beams = ["Arsenal", "Aston Villa", "Brighton", "Bournemouth", "Brentford", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich Town", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Southampton", "Tottenham Hotspur", "West Ham United", "Wolverhampton Wanderers"]

random.shuffle(beams)



# This is for the main page that asks you whether or not you want to load or start a new game.
def index(request):
    return render(request, "index.html")


#This is the view that runs your teamselect page.
def teamselect(request):
    global team_number
    global pick

    context = {}
    context['form'] = teampicker()
    player = Players.objects.all()
    team = Teams.objects.all()
#These two loops make sure that the teams are reset
    for tim in team:
        tim.selected = False
        tim.save()
#These two loops make sure that the players are reset
    for pl in player:
        pl.team = None
        pl.save()
    team_number = 0
    pick = 0
    return render(request, 'teamselect.html', context)


#This page runs the page that shows you which teams you have selected.
def verified(request):
    selected = []
    teams = Teams.objects.all()
    if request.method == 'POST':
        form = teampicker(request.POST)
        if form.is_valid():
            selected = form.cleaned_data['teams']
        else:
            print("Your forms invalid buddy", form.errors)
        teams = Teams.objects.all()
#this loop obtains exactly which teams are selected and makes that the case in the database. 
        for select in selected:
            for tim in teams:
                if select.strip().lower() == tim.name.strip().lower():
                    tim.selected = True
                tim.save()



    return render(request, 'verify.html', {"selected":selected, 'teams':teams})


#This is the page that actually conducts the playerselecting process
def home(request):

    firstteam = beams[0]
    allteams = Teams.objects.all()
#The sort_by is used to decide what the players displayed for selection are all ordered by.
    sort_by = request.GET.get('sort_by', 'overall') 
#The sort_order is used to decide whether the value goes from large to small or small to large
    sort_order = request.GET.get('sort_order', 'desc')
#The change_players variable allows the webpage to know whether or not on this page load we are going to actually take a player from
#no team to a team.
    change_players = request.GET.get('change_players', 'false')
    pl = Players.objects.all()
    tim = Teams.objects.get(name=firstteam)

    global team_number
    global pick
    round = 0
    selected_player = None
    teamThatPreviouslySelected = None
    currteam = None
    thesecondcodeisrunning = False

#This code is used when a player clicks on a category to change the way the players are listed.
    players = None
    if sort_order == 'asc':
        players = Players.objects.all().order_by(sort_by)
    else:
        players = Players.objects.all().order_by(f'-{sort_by}')
    
    try:
        currteam = Teams.objects.get(name=beams[team_number-1])
    except (IndexError, Teams.DoesNotExist):
        currteam = None

    if request.GET.get('sort_by'):
            print(beams[team_number])
            return render(
                request,"base.html",{'pl': players,'sort_by': sort_by,'sort_order': sort_order,'current_team': currteam,'allteams': allteams,'selected_player': selected_player,'teamthatselected': teamThatPreviouslySelected,'compteam':beams[team_number]},
            )
    gamestate = False
    team = None
    #Player Movement code
    if change_players == 'True':
        print("This page should not be running when this is false")
        team_name = beams[team_number]
        team_selecting_name = beams[team_number-1]
        player_id = request.GET.get('player_id')
        team = Teams.objects.get(name=team_selecting_name)
        if team.selected == True:
            try:
                player = Players.objects.get(id=player_id)
                team_selecting_name = beams[team_number-1]
                team = Teams.objects.get(name=team_selecting_name) 
                player.team = team 
                player.save()
                selected_player = player
            except Players.DoesNotExist:
                    print("Player not found.")
            except Teams.DoesNotExist:
                    print("Team not found.")

            #End the draft code
        
        if team_name != 'UserTeam': 
                best_player = None
                players = Players.objects.all()
                thesecondcodeisrunning = True
                team_name = beams[team_number]  
                gk = 0
                cb = 0
                fullback = 0
                winger = 0
                midfielder = 0
                striker = 0
                total = 0
                exclude = False
                
                try:
                    team = Teams.objects.get(name=team_name)
                    if team.selected == False:
                        print("THis works")
                    # Get the best available player
                        for p in players:
                            if p.team == team:
                                if p.position == "GK":
                                    gk = gk + 1
                                elif p.position == "CB":
                                    cb = cb + 1
                                elif p.position == "RB" or p.position == "LB":
                                    fullback = fullback + 1
                                elif p.position == "CAM" or p.position == "CM" or p.position == "CDM":
                                    midfielder = midfielder + 1
                                elif p.position == "RM" or p.position == "LM" or p.position == "LW" or p.position == "RW":
                                    winger = winger + 1
                                elif p.position == "ST":
                                    striker = striker + 1
                                total = total + 1
                        positions = []
                        if total <= 20:
                            if gk == 2:
                                positions.append("GK")
                                exclude = True
                            if cb == 4:
                                positions.append("CB")
                                exclude = True                                    
                            if fullback == 4:
                                positions.append("LB")
                                positions.append("RB")
                                exclude = True
                            if winger == 4:
                                positions.append("LW")
                                positions.append("RW")
                                positions.append("LM")
                                positions.append("RM")
                                exclude = True
                            if striker == 2:
                                positions.append("ST")
                                exclude = True
                            if midfielder == 6:
                                positions.append("CAM")
                                positions.append("CM")
                                positions.append("CDM")
                                exclude = True
                            print(exclude)
                            if exclude == True:
                                print("THis works")
                                if round >= 20: 
                                    best_player = Players.objects.filter(team__isnull=True).order_by('-tradevalue').first()
                                else:
                                    best_player = Players.objects.filter(team__isnull=True).exclude(position__in = positions).order_by('-tradevalue').first()
                                print(beams[team_number])
                                print(positions)
                                print(round)
                            else:
                                best_player = Players.objects.filter(team__isnull=True).order_by('-tradevalue').first()
                                print(round)
                        else:
                            best_player = Players.objects.filter(team__isnull=True).order_by('-tradevalue').first()
                            if gk == 0:
                                best_player = Players.objects.filter(position = "GK").order_by('-tradevalue').first()
                            print("Random")
                            print(round)

                        if best_player:
                            best_player.team = team
                            best_player.save()
                            print("BamAdebayo")
                            selected_player = best_player
                            teamThatPreviouslySelected = team

                    # Move to the next team
                            
                    team_number = (team_number + 1) % len(beams)

                except Teams.DoesNotExist:
                    print(f"Team {team_name} not found.")
        for man in pl:
            if man.team == tim:
                round = round + 1
                if round == 24:
                    gamestate = True
                    return redirect("completed")
    pick = team_number
    if pick == 0:
        pick = 20

    return render(request, "base.html", {'pick':pick,'round':round,'compteam':beams[team_number],'gamestate':gamestate,'second':thesecondcodeisrunning,'teamnum':team_number,'pl':players, 'sort_by': sort_by, 'sort_order': sort_order, 'current_team': team, 'allteams':allteams, 'selected_player':selected_player, 'teamthatselected':teamThatPreviouslySelected})



def gamecomplete(request):
    team = Teams.objects.all()
    player = Players.objects.order_by('position')
    custom_order = ['GK', 'LB','Lb', 'CB', 'RB','CDM','LM','CM','RM','CAM','LW','CF','ST','RW']
    player = sorted(Players.objects.all(), key=lambda p: custom_order.index(p.position))
    print("It is malfunctioning")
    return render(request, 'teams.html', {'teams': team,"player":player})



@login_required
def saveorlogin(request):
    teams = Teams.objects.all()
    ind = 1
    savers = SavedGame.objects.all()
    for saved in savers:
        ind = ind + 1
    savedName = f"Saved Game {ind}"
    
    if not request.user.is_authenticated:
        print("It worked but you need to login")
        return redirect('login')

    if request.method == 'POST':
        gamename = request.POST.get("gamename", savedName)
        teams = Teams.objects.all()
        selectedteams = Teams.objects.filter(selected=True)
        remainingteams = Teams.objects.filter(selected=False)
        selectedplayers = Players.objects.filter(team__in=teams)
        remainingplayers = Players.objects.filter(team=None)
        
        selectedteams = Teams.objects.filter(selected=True)
        for tim in selectedteams:
            tim.selected == True
            tim.save()
        # Structure the data
        teamsdata = {
            "selectedteams": [
                {
                    "team_name": team.name,
                    "players": [
                        {
                            "firstname": player.firstname,
                            "lastname": player.lastname,
                            "position": player.position,
                        }
                        for player in selectedplayers if player.team == team
                    ],
                }
                for team in selectedteams
            ],
            "remainingteams": [
                {
                    "team_name": team.name,
                    "players": [
                        {
                            "firstname": player.firstname,
                            "lastname": player.lastname,
                            "position": player.position,
                        }
                        for player in selectedplayers if player.team == team
                    ],
                }
                for team in remainingteams
            ],
            "remainingplayers": [
                {
                    "firstname": player.firstname,
                    "lastname": player.lastname,
                    "position": player.position,
                }
                for player in remainingplayers
            ]
        }

        # Save the game to the database
        savedgame = SavedGame.objects.create(
            user=request.user,
            gamename=gamename,
            teams=json.dumps(teamsdata),  # Store as a JSON string
        )
 

        # Redirect to a confirmation page
        print("It worked and was saved")
        return redirect('savedgames')  # Replace with the actual URL name for the saved games page
    print("Proof")
    game = request.GET.get('game', 0)
    if game != 0:
        deletedgame = SavedGame.objects.get(id=game)
        deletedgame.delete()


    print("I'm not sure what happened tbh")
    return render(request, 'savedgames.html', {"teams": teams, "players": Players.objects.all(), "savedgames":SavedGame.objects.all()})



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('savedgames')  # Replace 'home' with your desired redirect URL
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')



def SavedGames(request):
    savedgames = SavedGame.objects.all()
    
    return render(request, 'savedgames.html', {"savedgames": savedgames})



def deletesaved(request):
    savedgames = SavedGame.objects.all()

    return render(request, 'savedgames.html', {"savedgames": savedgames})



def loadsaved(request, savedgameid):
    savedgame = get_object_or_404(SavedGame, id=savedgameid)  # Get the saved game from the database
    print("worked")
    teamsdata = savedgame.teams

    # Parse the JSON data (assuming it is stored as a JSON string)
    teamsdata = json.loads(teamsdata)

    # Update the teams and players in the database to match the saved data
    for bin in teamsdata['selectedteams']:
        print(f"Processing team: {bin['team_name']}")
        team = Teams.objects.get(name=bin['team_name'])
        
        # Update players in the team
        for playerdata in bin['players']:
            print(f"Assigning player: {playerdata['firstname']} {playerdata['lastname']} to team {team.name}")
            player = Players.objects.get(firstname=playerdata['firstname'], lastname=playerdata['lastname'])
            player.team = team
            player.save()

    for bin in teamsdata['remainingteams']:
        print(f"Processing team: {bin['team_name']}")
        team = Teams.objects.get(name=bin['team_name'])
        
        # Update players in the team
        for playerdata in bin['players']:
            print(f"Assigning player: {playerdata['firstname']} {playerdata['lastname']} to team {team.name}")
            player = Players.objects.get(firstname=playerdata['firstname'], lastname=playerdata['lastname'])
            player.team = team
            player.save()


    return redirect('completed')
