from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Camper, Booking
from .forms import AvailabilityForm
from booking.booking_functions.availability import check_availability
from . import views







class CamperList(ListView):
    model = Camper

class BookingList(ListView):
    model = Booking

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'booking/availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        camper_list = Camper.objects.filter(campertype = data['camper_type'])
        
        available_camper = []
        for camper in camper_list:
            if check_availability(camper, data['pickup'], data['dropoff']):
                available_camper.append(camper)

        if len(available_camper) >0:
            camper = available_camper[0]
            booking = Booking.objects.create(
            user = self.request.user, 
            camper = camper, 
            pickup = data['pickup'],
            dropoff = data['dropoff'],

            )
            booking.save()
            return HttpResponse(booking)

        else:
            return HttpResponse('This camper is alredy booked for that time')
        


