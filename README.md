﻿TRPOProject!
===========
Доки и исходники по курсовой работе ТРПО.

Проект создан для PyCharm. В нем просто открываем папку проекта.

Лабы: http://portal.tpu.ru:7777/SHARED/i/I/study/trpo/lab
===========
Запуск проекта (при использовании PyCharm Community version):
- если вы внесли измение в модели, то выполняем в терминале, находясь в папке проекта: python manage.py makemigrations
- если выполнили предыдущий пункт, то выполняем: python manage.py migrate
- создается или обновляется база db.sqlite3, расположенная в папке проекта. Если она только создалась, то выполняем python manage.py createsuperuser
- заускаем сервер выполнив python manage.py runserver (он напишет адрес, на котором развернулся сайт - переходим туда)
