from django.contrib import admin
from django.urls import path, include
import biwtapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', biwtapp.views.home, name='home'),
    path('about/', biwtapp.views.about, name='about'),
    path('biwtsignup', biwtapp.views.signup, name='signup'),
    path('biwtlogin', biwtapp.views.login, name='login'),
    path('logout/', biwtapp.views.logout, name='logout'),
    path('contact/', biwtapp.views.contact, name='contact')
]
