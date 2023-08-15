from django.urls import path
from . import views
from django.conf import settings
 

urlpatterns = [

  
    
    path('', views.sendemail, name="sendemail"),
    path('verifyotp/', views.verifyotp, name="verifyotp"),
    
   

]

