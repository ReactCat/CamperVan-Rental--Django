""" CAMPER RENTAL SITE MAIN URL Configuration """
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('camper.urls')),
    path('', include('booking.urls'))
]
