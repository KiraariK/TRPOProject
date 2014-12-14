from django import forms

IMP_CHOICES = (
    ('1', 'imp 1'),
    ('2', 'imp 2'),
    ('3', 'imp 3'),
    ('4', 'imp 4'),
)


class TableForm(forms.Form):
    phone = forms.CharField(label='Телефон пользователя', max_length=128)
    address = forms.ChoiceField(label='Адрес пользователя',choices=IMP_CHOICES)
    hall = forms.ChoiceField(label='Выберите зал')
    table = forms.ChoiceField(label='Выберите столик')
    data = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'type': 'date'
                                }))


class DeliveryForm(forms.Form):
    phone = forms.CharField(label='Телефон пользователя', max_length=128)
    address = forms.ChoiceField
    data = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'type': 'date'
                                }))



class PickUpForm(forms.Form):
    phone = forms.CharField(label='Телефон', max_length=128)
