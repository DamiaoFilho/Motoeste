from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(MotoTaxi)
admin.site.register(Rating)
admin.site.register(Ride)