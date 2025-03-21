""" django1 URL Configuration

    URL configuration for django1 project.

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
import django
django.setup()

from django.contrib import admin
from django.urls import path, include 

from django.conf.urls import handler404, handler500
from core import views

from core.views import index, contato, produto


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'), 
    
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]  
   
handler404 = views.error_404
handler500 = views.error_500

