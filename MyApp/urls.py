from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home-page'),
    path('dashboard/',dashboard,name="dashboard"),

]
