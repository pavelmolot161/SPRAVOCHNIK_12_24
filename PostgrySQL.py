### - Создание PostgrySQL по шагам

### - 08.01.25

### - 1) установка Django: - (.venv) D:\Rabota_12_24\Django_PostgreSQL_01_25 git:[main
#                                                            >>> pip install django
### - 2) Создание проекта: - (.venv) D:\Rabota_12_24\Django_PostgreSQL_01_25 git:[main
#                                                            >>> django-admin startproject Project_django_postge .
#                          - в конце проекта, через пробел поставить (.) , РАБОТАЕТ
### - 3) Создаем папку templates
### - 4) Создаем приложение App_django
#                                                            >>> python manage.py startapp App_django_postge

### - 5) Переход в директорию проекта:
#                                                            >>> cd D:\Rabota_12_24\Django_Paginator_01_25

### - 6) Создание файла зависимостей:
#            (.venv) D:\Rabota_12_24\Django_PostgreSQL_01_25 git:[main] >>> pip freeze > requirements.txt
#     6.a) вывод зависимостей в консоль:
#                                                                       >>> pip freeze

### - 7) В файле settings.py:                                                                                      (-)
#             в строке TEMPLATES = [] дополняем значение 'DIRS': [] == 'DIRS': [BASE_DIR / "templates"],
#             в строке INSTALLED_APPS = [] в конце дописываем имя нашего приложения 'App_django_postge'

### - 8) создали модель в models.py class User(models.Model):

### - 9) Дополнение файла admin.py:
#                                   from django.contrib import admin
 #                                  from .models import *
  #                                 admin.site.register(User)


### - 10) Миграции не были выполнены: Возможно, Вы не применили миграции для Вашего приложения. Убедитесь,
# что Вы выполнили команды:
#                                          >>> python manage.py makemigrations    ### - Создаем миграцию
#                                          >>> python manage.py migrate           ### - Применяем миграцию

### - 11) Устанавливаем пакет PostgreSQL версии 16.3 через сайт PostgreSQL Download

### - 12) Устанавливаем через терминал psycopg2. Это основной драйвер для подключения Django к PostgreSQL.
# Он обеспечивает взаимодействие между Django и базой данных PostgreSQL.

#                                          >>> pip install psycopg2-binary
### - 13) Установили pgAdmin4 через виндовс

### - 14) Создание базы данных

### - 15) Создание DB через - Использование PowerShell
            # В PowerShell Вам нужно использовать обратные кавычки или заключить всю команду в одинарные кавычки. Однако проще всего выполнить команду через двойные кавычки, как показано ниже:
            #
            # PowerShell

        ### - >>> & "D:\NE_TROGAT_biblioteki_pakety\PostgreSQL\16\bin\psql.exe" -U postgres -c "CREATE DATABASE db.shop_db;"

            # Пояснение:
            # & используется для вызова программы в PowerShell, когда путь к программе указан в кавычках.
            # "D:\NE_TROGAT_biblioteki_pakety\PostgreSQL\16\bin\psql.exe" — это путь к psql.exe.
            # -U postgres — указывает пользователя для подключения.
            # -c "CREATE DATABASE db.shop_db;" — эта часть содержит SQL-команду для выполнения.

### - 16) Создание текстового файла db.shop_db но пока не понятно нужен он или нет - ???

### - 17) Создадим суперпользователя, который имеет доступ ко всем административным функциям нашего приложения:
#                                           >>> python manage.py createsuperuser / если не создан
                                # python manage.py createsuperuser
                                # Username (leave blank to use 'firebat'): testPavel
                                # Email address:
                                # Password:
                                # Password (again):
                                # This password is too common.
                                # This password is entirely numeric.
                                # Bypass password validation and create user anyway? [y/N]: y
                                # Superuser created successfully.

### - 18) Регистрируем модель в файле admin.py
#                               admin.site.register(Post)      ### - не консоль

### - 19) ЗАПУСK серверa разработки:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py runserver
