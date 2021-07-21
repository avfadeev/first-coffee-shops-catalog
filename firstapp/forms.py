from django import forms
from firstapp.models import Order, Coffee


class OrderForm(forms.ModelForm):
    coffee = forms.ModelChoiceField(queryset=Coffee.objects.all(), widget=forms.HiddenInput)

    class Meta:
        model = Order
        fields = ('coffee', 'name', 'phone')
