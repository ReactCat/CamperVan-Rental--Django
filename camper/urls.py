from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('camper1', views.camper1, name='camper1'),
    path('camper2', views.camper2, name='camper2'),
    path('inquiry', views.inquiry, name='inquiry'),

]