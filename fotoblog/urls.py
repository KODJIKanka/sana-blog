"""
URL configuration for fotoblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import authentication.views
import blog.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.connexion, name='login'),
    path('home/', authentication.views.home, name='home'),
    path('logout/', authentication.views.signout, name='logout'),
    path('groups/', blog.views.list_group, name='list-group' ),
   # path('articles/', blog.views.list_article, name='list-article' ),
    path('articles/<int:id>/', blog.views.detail_article, name='detail' ),
    path('sinup/', authentication.views.inscription, name='sinup'),
    path('kofi/', blog.views.kofi, name='kofi' ),
    
   


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
