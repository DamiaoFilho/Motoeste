from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('index/', index),
    path('clientForms/', SignUpView_Client.as_view(), name='clientForms'),
    path('login/', SignInView.as_view(), name='login'),
    path('taxiForms/', SignUpView_Taxi, name='taxiForms'),
    path('', init.as_view()),
    path('createRide/', createRides, name='createRides'),
    path('activeRide/', activeRide, name='activeRide'),
    path('endRide', endRide, name='endRide'),
    path('logout/', end, name='end'),
    path('history/', history, name='history')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)