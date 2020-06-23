from django.urls import path
from . import views

urlpatterns = [
    #ITSP
    path('', views.index, name='index'),

    #ITSP/200
    path('<int:team_id>/',views.detail, name='detail'),


]