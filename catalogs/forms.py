from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):           #This form allows users tio insert data into our Listing Model
    class Meta:                         #Meta here is used to inherit our Listing class from models.py
        model = Listing
        fields = [
            'category',
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
            'image',
            'status',
        ]

