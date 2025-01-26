from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.index, name = "index"),
    path("teamselect.html", views.teamselect, name = "teamselect"),
    path("verify.html", views.verified, name = "verified"),
    path("base.html", views.home, name = "home"),
    path("teams.html", views.gamecomplete, name = "completed"),
    path('login.html', views.login, name='login'),
    path('savedgames.html', views.SavedGames, name='savedgames'),
    path('savedgames/<int:savedgameid>', views.deletesaved, name='deletesaved'),
    path('saveorlogin/', views.saveorlogin, name='saveorlogin'),
    path('loadsaved/<int:savedgameid>/',views.loadsaved, name = "loadsaved")
]
