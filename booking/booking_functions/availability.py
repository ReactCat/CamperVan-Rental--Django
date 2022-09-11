import datetime 
from booking.models import Camper, Booking


def check_availability(camper, pickup, dropoff):
    avail_list=[]
    booking_List = Booking.objects.filter(camper=camper)
    for booking in booking_List:
        if booking.pickup > dropoff or booking.dropoff < pickup:
            avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list)
