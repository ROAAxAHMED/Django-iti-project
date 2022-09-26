
from django import forms
from amazon.models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
