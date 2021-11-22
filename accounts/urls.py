from django.urls import path
from django.contrib.auth import views as auth_views
from simplemooc.accounts.views import register



urlpatterns = [
   path('entrar/', auth_views.LoginView.as_view(), name='login'),
   path('sair/', auth_views.LogoutView.as_view(), {'nex_page':'core:home'}, name='logout'),
   path('cadastre-se/', register, name='register'),

]
