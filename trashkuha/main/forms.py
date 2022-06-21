from django import forms
from django.forms import ModelForm
from .models import booking
import datetime
class bookingform(ModelForm):
	class Meta:
		model = booking
		fields = ('first_name','last_name', 'address', 'phone', 'category', 'description', 'quantity', 'collection_date')
		labels = {
			'first_name': '',
			'last_name': '',
			'address': '',
			'phone': '',
			'category': 'Category',
			'description': '',
			'quantity': 'Quantity',
			'collection_date': '',			
		}
		widgets = {
			'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone No.'}),
			'category': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex. Plastic'}),
			'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
			'quantity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex.1'}),
			'collection_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
}
		
