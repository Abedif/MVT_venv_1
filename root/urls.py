
from django.urls import path , include

from .views import home , contact , about_us

app_name = 'root'

urlpatterns = [
    path('' , home , name='home') ,
    path('contact/' , contact , name='contact'),
    path('about_us/' , about_us , name = 'about_us')
    
]