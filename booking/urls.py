"""  RENTAL APP  URL Configuration """
from django.urls import path
from . import views
from .views import BookingList, CamperList, BookingView




app_name='booking'

urlpatterns = [

    path('camper_list/', CamperList.as_view(), name='CamperList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view'),

]