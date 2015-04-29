from django import forms
from myapp.models import Customer
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'birthdate', 'address', 'parent_guardian_name', 'home_phone', 'email', 'emergency_contact', 'medical_conditions', 'height_inches', 'weight_pounds', 'is_locked', 'other_phones']
        widgets = {'birthdate': DateInput()}
