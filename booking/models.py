from django.db import models
from django.conf import settings 



class Camper(models.Model):
    CAMPER_CATEGORIES=(
        ('AMITY', 'Amity Camper'),
        ('ANTHONY', 'Anthony Camper'),
        
    )

    
    campertype = models.CharField(max_length=7, choices=CAMPER_CATEGORIES)
    

    def __str__(self):
        return f'{self.campertype}, Rental Campervan '


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    camper = models.ForeignKey(Camper, on_delete=models.CASCADE)
    pickup = models.DateTimeField()
    dropoff = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.camper} from {self.pickup} to {self.dropoff} '
