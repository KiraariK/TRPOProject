from datetime import datetime, timedelta
from django import forms
from establishments.models import EstablishmentBranch, BranchHall, DinnerWagon


class TableForm(forms.Form):
    address = forms.ChoiceField(
        label='Адрес заведения',
        error_messages=
        {
            'required': 'Поле адреса заведения не может быть пустым'
        },
        required=True
    )
    hall = forms.ChoiceField(
        label='Тип зала заведения',
        error_messages=
        {
            'required': 'Поле типа зала заведения не может быть пустым'
        },
        required=True
    )
    table = forms.ChoiceField(
        label='Количество мест за столиком',
        error_messages=
        {
            'required': 'Поле столика заведения не может быть пустым'
        },
        help_text='Если поле пустое, то свободных столиков нет',
        required=True
    )
    datetime = forms.DateTimeField(
        label='Дата и время заказа',
        input_formats=['%d-%m-%y %H:%M', '%d-%m-%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'placeholder': '15-12-14 19:00'}),
        error_messages=
        {
            'required': 'Поле времени заказа не может быть пустым',
            'invalid': 'Неверный формат записи времени заказа'
        },
        help_text='Выбирая дату помните, что для обработки заказа требуется не менее двух часов.',
        required=True
    )
    phone = forms.CharField(
        label='Ваш контактный телефон',
        widget=forms.TextInput(attrs={'placeholder': '9004001020'}),
        max_length=10,
        error_messages=
        {
            'required': 'Поле номера телефона не может быть пустым'
        },
        help_text='Необходим для обработки и подтверждения заказа сотрудниками заведения.',
        required=True
    )

    def clean_datetime(self):
        date_time = self.cleaned_data['datetime']
        # TODO учитывать временные зоны (date_time содержит дату с учетом временой зоны) сейчас - абсолютоное время
        execution_date_time = datetime(
            date_time.year,
            date_time.month,
            date_time.day,
            date_time.hour,
            date_time.minute
        )
        date_time_border = datetime.now() + timedelta(hours=2)
        if execution_date_time <= date_time_border:
            raise forms.ValidationError('Невозможно оформить заказ на выбранное время')
        return execution_date_time

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        symbols_list = list(phone)
        for symbol in symbols_list:
            try:
                int_value = int(symbol)
                if int_value < 0:
                    raise forms.ValidationError('Неверный номер телефона')
            except ValueError:
                raise forms.ValidationError('Неверный номер телефона')
        return phone

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

            # TODO: исправить баг: оценивание забронированности столиков происходит без учета даты и времени заказов
            # как пофиксить:
            # 1. изменить модель столика - убрать is_reserved
            # 2. изменить форму заказа столика - 2 шага: 1. Выбрать филиал, зал, дату (submit) 2. Столик, телефон
            # 3. изменить разметку html формы
            # 4. изменить конструктор формы
            # 5. изменить view формы, чтобы правильно вызывать конструктор
            if branch_id != -1 and hall_type != -1:
                # изменился зал: для заданного branch_id выгрузить зал hall_type и его столики
                # если branch_id != -1 и hall_type != -1, то загружаем зал филиала branch_id и его столики
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
            elif branch_id != -1 and hall_type == -1:
                # изменилось заведение: для заданного branch_id выгрузить первый попавшийся зал и его столики
                # загружаем залы branch_id и сттолики по умолчанию
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
                # ничего не изменилось
                # загружаем все по умолчанию
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


class DeliveryForm(forms.Form):
    phone = forms.CharField(label='Телефон пользователя', max_length=128)
    address = forms.ChoiceField
    data = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))


class PickUpForm(forms.Form):
    phone = forms.CharField(label='Телефон', max_length=128)
