
from django.urls import path , include

from .views import home , contact_us , about_us , comment , help , privacy 



urlpatterns = [
    path('' , home) ,
    path('contact_us/' , contact_us),
    path('comment/' , comment) ,
    path('help/' , help) ,
    path('privacy/' , privacy) ,
]