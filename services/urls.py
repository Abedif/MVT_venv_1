
from django.urls import path
from .views import *

app_name = 'services' 


urlpatterns =[
    path('' , services , name= 'services') ,
    path('service_details/' , service_details , name= 'service_details') ,
    path('comment/' , comment , name='comment')
]
