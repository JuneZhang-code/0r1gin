from django.urls import path

from . import views
urlpatterns = [

    path('',views.allproject,name='allproject'),

    #button
    path('initiate/', views.initiate, name='initiate'),
    path('support/', views.support, name='support'),
    path('preorder/', views.preorder, name='preorder'),
    path('checkout/', views.checkout, name='checkout'),
    path('viewproject/<int:project_pk>', views.viewproject, name='viewproject'),



]
