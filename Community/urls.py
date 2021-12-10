from django.urls import path
from django.conf.urls import include, url

from . import views
urlpatterns = [

    path('',views.community,name='community'),
    #button
    path('invest/', views.invest, name='invest'),
    path('started/', views.started, name='started'),
    path('question/', views.question, name='question'),
    path('interest/', views.interest, name='interest'),
    path('Initiate/', include('Initiate.urls')),


]
