from django.urls import path
from .views import *

urlpatterns = [
    path('indexClient/', index_client),
    path('indexTaxi/', index_taxi),
    path('clientForms/', clientForms, name='clientForms'),
    path('login/', login, name='login'),
    path('taxiForms/', taxiForms, name='taxiForms')
]