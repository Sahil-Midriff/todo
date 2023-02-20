from django.urls import path
from .views import *


urlpatterns = [
    
    path('',Home,name='home'),
    path('profile',Profile,name='profile'),
    path('showdetails/<int:id>',Showdetails,name='showdetails'),
    path('update/<str:id>',Update,name='update'),
    path('delete/<int:id>',Delete,name='delete'),
    path('search',Search,name='search'),
     
]