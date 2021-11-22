from django.conf.urls import include, url
from django.urls import path
from simplemooc.core.views import contatogleison
from simplemooc.core.views import home



urlpatterns = [ 
    path('', home, name='home'),
    path('contatogleison/', contatogleison, name='contatogleison'),
]