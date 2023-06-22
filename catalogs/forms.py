from django.forms import ModelForm, Form
from .models import Listing
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class ListingForm(ModelForm):           #This form allows users tio insert data into our Listing Model
    class Meta:                         #Meta here is used to inherit our Listing class from models.py
        model = Listing
        fields = [
            'title',
            'price',
            'num_bedrooms',
            'num_bathrooms',
            'num_sittingrooms',
            'num_kitchens',
            'square_feet',
            'state', 
            'city',
            'address',
        ]

class SignupForm(UserCreationForm):
    class Meta:
        model = Account                                                    #User is inbuilt model in django
        fields = ('username', 'email', 'password', 'password1')