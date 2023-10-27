from django.urls import path

from . import views

# adcioname nam space do app

app_name = "home"

urlpatterns = [
    # colocando o nomne da pagina home
    path("", views.home, name="home"),
]
