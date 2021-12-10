"""OR1GIN_STUDIO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from Newsletter import views
urlpatterns = [
    path('admin/', admin.site.urls),

    #Newsletter homepage
    path('',views.home,name='home'),
    path('betaprogram/',views.betaprogram,name='betaprogram'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('mentor/',views.mentor,name='mentor'),
    path('designerhome/',views.designerhome,name='designerhome'),




    #Community
    path('Community/', include('Community.urls')),

    #Initiate
    path('Initiate/', include('Initiate.urls')),

    #ambassador
    path('ambassador/', include('ambassador.urls')),

    #designer
    path('designer/', include('designer.urls')),

    #store
    path('store/', include('store.urls')),

    #carts
    path('carts/', include('carts.urls')),

    #accounts
    path('accounts/', include('accounts.urls')),

    #orders
    path('orders/', include('orders.urls')),




]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
