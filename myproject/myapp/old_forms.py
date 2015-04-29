from myapp.models import Customer

from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class RegisterForm(forms.ModelForm):
    firstname = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    lastname = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    birthdate = forms.DateField(widget=DateInput())
    address = forms.CharField(label='Address', max_length=1000, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    parent_guardian_name = forms.CharField(label='Parent/Guardian name', max_length=200, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    home_phone = forms.CharField(label='Home phone', max_length=15, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    email = forms.EmailField(label='Email', max_length=250, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    emergency_contact = forms.CharField(label='Emergency Contact Name & Phone', max_length=1000, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    medical_conditions = forms.CharField(label='Medical Conditions', max_length=65535, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    height_inches = forms.CharField(label='Height in Inches', max_length=2, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    weight_pounds = forms.CharField(label='Weight in Pounds', max_length=3, widget=forms.TextInput(attrs={'class':'reg_form_field'}))
    other_phones = forms.CharField(label='Other Phones', max_length=1000, widget=forms.TextInput(attrs={'class':'reg_form_field'}))

    class Meta:
        model = Customer
