from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

#SignUp form
class SignupForm(forms.ModelForm):
    
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Enter password',
         'class':'w-full py-4 px-6 rounded-xl',  }))        # can customize the form to add css class to it

    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Confirm password'})) 

    class Meta:
        model = Account                                                   
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password')

    def __init__(self, *args,  **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter User Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email address'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter phone number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password1')

        if password != confirm_password:
            raise forms.ValidationError(
                'password does not match!'
            )

