from django import forms

class AvailabilityForm(forms.Form):

    CAMPER_CATEGORIES=(
        ('AMITY', 'Amity Camper'),
        ('ANTHONY', 'Anthony Camper'),
        
    )

    camper_type = forms.ChoiceField(choices=CAMPER_CATEGORIES, required=True)
    pickup = forms.DateTimeField(required = True, input_formats='%y-%m-%dT %H:%M')
    dropoff = forms.DateTimeField(required = True, input_formats='%y-%m-%dT %H:%M')
