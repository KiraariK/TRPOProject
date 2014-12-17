from django import forms
from establishments.models import EstablishmentBranch, BranchHall, DinnerWagon


class TableForm(forms.Form):
    address = forms.ChoiceField(
        label='Адрес заведения',
        required=True
    )
    hall = forms.ChoiceField(
        label='Тип зала заведения',
        required=True
    )
    table = forms.ChoiceField(
        label='Количество мест за столиком',
        required=True
    )
    data_time = forms.DateTimeField(
        label='Дата посещения',
        input_formats=['%d-%m-%y %H:%M', '%d-%m-%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'placeholder': '15-12-14 19:00'}),
        help_text='Выбирая дату помните, что для обработки заказа требуется не менее двух часов.',
        required=True
    )
    phone = forms.CharField(
        label='Ваш контактный телефон',
        help_text='Необходим для обработки и подтверждения заказа сотрудниками заведения',
        widget=forms.TextInput(attrs={'placeholder': '9994441122'}),
        max_length=10,
        required=True
    )

    def __init__(self, establishment_id, branch_id, hall_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if EstablishmentBranch.objects.filter(establishment__id=establishment_id).exists():
            self.fields['address'] = forms.ChoiceField(
                choices=[(branch.id, branch.address) for branch in EstablishmentBranch.objects.filter(
                    establishment__id=establishment_id
                )],
                label='Адрес заведения',
                required=True
            )

            # если branch_id == -1 и hall_type = -1: загрузка данных по умолчанию
            if branch_id == -1 and hall_type == -1:
                default_branch = EstablishmentBranch.objects.filter(establishment__id=establishment_id).first()
                self.fields['hall'] = forms.ChoiceField(
                    choices=[(hall.type, hall.get_type_display()) for hall in BranchHall.objects.filter(
                        branch=default_branch
                    )],
                    label='Тип зала заведения',
                    required=True
                )

                default_hall = BranchHall.objects.filter(branch=default_branch).first()
                free_tables = DinnerWagon.objects.filter(hall=default_hall, is_reserved=False)
                if free_tables.exists():
                    table_types = []
                    for table in free_tables:
                        if table_types.count(table.seats) == 0:
                            table_types.append(table.seats)
                    self.fields['table'] = forms.ChoiceField(
                        choices=[(table_type, table_type) for table_type in table_types],
                        label='Количество мест за столиком',
                        required=True
                    )
            else:
                default_branch = EstablishmentBranch.objects.filter(
                    establishment__id=establishment_id,
                    id=branch_id
                ).first()
                self.fields['hall'] = forms.ChoiceField(
                    choices=[(hall.type, hall.get_type_display()) for hall in BranchHall.objects.filter(
                        branch=default_branch
                    )],
                    label='Тип зала заведения',
                    required=True
                )

                default_hall = BranchHall.objects.filter(
                    branch=default_branch,
                    type=hall_type
                ).first()
                free_tables = DinnerWagon.objects.filter(hall=default_hall, is_reserved=False)
                if free_tables.exists():
                    table_types = []
                    for table in free_tables:
                        if table_types.count(table.seats) == 0:
                            table_types.append(table.seats)
                    self.fields['table'] = forms.ChoiceField(
                        choices=[(table_type, table_type) for table_type in table_types],
                        label='Количество мест за столиком',
                        required=True
                    )


class DeliveryForm(forms.Form):
    phone = forms.CharField(label='Телефон пользователя', max_length=128)
    address = forms.ChoiceField
    data = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))


class PickUpForm(forms.Form):
    phone = forms.CharField(label='Телефон', max_length=128)
