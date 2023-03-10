from django.urls import path
from . import views
app_name = "cricket"
urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("", views.home, name="home"),
    path("logout", views.logout_request, name="logout"),
    path('list', views.list_view, name='list_teams'),
    path('player_name', views.addplayer_name, name='player_name'),
    path("newmatch", views.addnewmatch, name="newmatch"),
]
