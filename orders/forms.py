from django import forms
from orders.models import Order


class TableForm(forms.ModelForm):
    phone = forms.CharField(max_length=128, help_text="Please enter the category name.")
    address = forms.CheckboxInput
    hall = forms.CheckboxInput
    table = forms.CheckboxInput
    data = forms.DateTimeField
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Order