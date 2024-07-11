from django import forms
from page.models import ReservationModel, SubscribeModel

class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationModel
        fields = ['contact_name', 'contact_email', 'contact_phone', 'num_of_people', 'date', 'contact_message']


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribeModel
        fields = ['email']