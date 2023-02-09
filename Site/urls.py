from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index),
    path('clientForms/', SignUpView_Client.as_view(), name='clientForms'),
    path('login/', SignInView.as_view(), name='login'),
    path('taxiForms/', SignUpView_Taxi.as_view(), name='taxiForms'),
    path('motoForms/', motoForms.as_view(), name='motoForms')
]