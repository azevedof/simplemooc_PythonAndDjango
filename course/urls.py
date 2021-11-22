from django.urls import path
from simplemooc.course.views import index
from simplemooc.course.views import details


urlpatterns = [
    path('', index, name='index'),
    #path('<int:pk>/', details, name='details'),
    path('<slug:slug>/', details, name='details'),


]
