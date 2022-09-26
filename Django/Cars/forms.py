from django import forms
from cars.models import Cars

class CarsModelForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'
