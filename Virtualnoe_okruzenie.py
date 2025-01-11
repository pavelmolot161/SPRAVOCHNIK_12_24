############    Виртуальное окружение. Часть 1.    #########################################################


# import os
# print(os.getcwd())
'''обязательно обратить внимание на кавычки в пути к папке
так как терминал не воспринимает некоторые знаки например ()'''
from pprint import pprint

### - первая команда в терминале ### - PS D:\Project(HomeWork)> >>> cd 'D:\Project(HomeWork)\module_11'

'''во второй команде обязательно обратить внимание на то чтобы перед -m venv venv2, 
был обозначен язык програмирования , в нашем случае это python'''
### - вторая команда в терминале ### - PS D:\Project(HomeWork)\module_11> >>> python -m venv venv2

'''в третьей команде и последующих мы можем устанавливать библиотеки для работы в новом вертуальном окружении'''
### - третья команда в терминале ### - PS D:\Project(HomeWork)\module_11> >>> pip install pillow

'''в четвертой команде мы активируем созданное виртуального пространства'''
### - четвертая команда в терминале ### - PS D:\Project(HomeWork)\module_11> >>> venv2\Scripts\activate
    ### - (venv2) PS D:\Project(HomeWork)\module_11>  - говорит о создании нового виртуального пространства

'''в пятой команде (создаем файл с зависимостями) создаем список всех установленных библиотек и сохранить его в фай'''
### - PS D:\Project(HomeWork)\module_11> >>> pip freeze
    # contourpy==1.3.0
    # cycler==0.12.1
    # fonttools==4.54.1
    # kiwisolver==1.4.7
    # matplotlib==3.9.2
    # numpy==2.1.1
    # packaging==24.1
    # pandas==2.2.3
    # pillow==10.4.0
    # pyparsing==3.1.4
    # python-dateutil==2.9.0.post0
    # pytz==2024.2
    # six==1.16.0
    # tzdata==2024.2

''' В последующем можно узнать какой список пакетов установлен'''
### - PS D:\Project(HomeWork)\module_11\вебинар_11> >>> pip list
        # alabaster                     1.0.0
        # annotated-types               0.7.0
        # anyio                         4.6.0
        # appdirs                       1.4.4
        # babel                         2.16.0
        # certifi                       2024.8.30
        # charset-normalizer            3.3.2

''' Чтобы узнать что находится в каком либо пакете необходима использовать >>> pip show.(название пакета)'''
### - PS D:\Project(HomeWork)\module_11\вебинар_11> >>> pip show alabaster
        # Name: alabaster
        # Version: 1.0.0
        # Summary: A light, configurable Sphinx theme
        # Home-page:
        # Author:
        # Author-email:
        # License:
        # Location: C:\Users\FIREBAT\AppData\Local\Programs\Python\Python311\Lib\site-packages
        # Requires:
        # Required-by: Sphinx

''' в шестой команде создаем файл с именем requirements.txt (имя по умолчанию чтобы другие его нашли)'''
### - PS D:\Project(HomeWork)\module_11> >>> pip freeze > requirements.txt

''' В случае если наоборот нам нужно создать виртуальное окружение и загрузитиь чужой код и его библиотеки 
для этого кода (по другому файл зависимостей) '''
### - >>> pip install -r requirements.txt

#______________________________________________________________________________