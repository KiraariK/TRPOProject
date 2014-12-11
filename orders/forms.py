from django import forms
from orders.models import Order


class TableForm(forms.Form):
    phone = forms.CharField(label=u'Телефон пользователя', max_length=128, help_text="Please enter the category name.")
    address = forms.CheckboxInput
    hall = forms.CheckboxInput
    table = forms.CheckboxInput
    data = forms.DateTimeField


class DeliveryForm(forms.Form):
    phone = forms.CharField(label='Телефон пользователя', max_length=128)
    address = forms.CheckboxInput
    data = forms.DateTimeField


class PickUpForm(forms.Form):
    phone = forms.CharField(label='Телефон', max_length=128)

