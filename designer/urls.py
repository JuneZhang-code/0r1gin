from django.urls import path
from django.conf.urls import include, url

from . import views
urlpatterns = [

    path('',views.designer,name='designer'),
    #button
    path('createaccount/', views.createaccount, name='createaccount'),
    path('tx/', views.tx, name='tx'),


]
