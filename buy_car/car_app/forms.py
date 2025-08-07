from django import forms
from .models import Car

citizen_choices = [
    ('INDIAN', 'INDIAN'),
    ('NRI', 'NRI'),
    ('OCI', 'OCI'),
    ('PIO', 'PIO'),
    ('FOREIGNER', 'FOREIGNER'),
]

car_model_choices = [
    ('TESLA_MODEL_S', 'TESLA_MODEL_S'),
    ('FORD_MUSTANG', 'FORD_MUSTANG'),
    ('TOYOTA_COROLLA', 'TOYOTA_COROLLA'),
    ('HONDA_CIVIC', 'HONDA_CIVIC'),
    ('BMW_X5', 'BMW_X5'),
    ('AUDI_A4', 'AUDI_A4'),
    ('MERCEDES_C_CLASS', 'MERCEDES_C_CLASS'),
]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'first_name':'BUYER FIRST NAME',
            'last_name':'BUYER LAST NAME',
            'citizen':'CITIZENSHIP',
            'car_model':'CAR MODEL',
            'car_make_year':'CAR MADE',
            'price':'CAR PRICE',
            'email':'BUYER EMAIL ID',
            'password':'PASSWORD'
        }
        widgets = {
            'first_name':forms.TextInput(attrs={
                'placeholder':'Enter First Name',
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Enter Last Name',
            }),
            'citizen':forms.RadioSelect(choices=citizen_choices),
            'car_model':forms.Select(choices=car_model_choices),
            'email':forms.EmailInput(attrs={
                'placeholder':'youremail@gmail.com'
            }),
            'password':forms.PasswordInput(attrs={
                'type':'password'
            })
        }

