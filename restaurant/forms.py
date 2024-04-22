from django.contrib.auth.models import User

from .models import Booking
from django.forms import ModelForm, Form
from django.forms.widgets import Textarea


class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'comment', 'guest_number']
        widgets = {
            'comment': Textarea()
        }
