# DjangoTeamwork12
Only three table

##Environment
<br>
Python x.x.x
<br>
Django 2.2.6

##Install
```Python
pip install django-import-export
pip install Pillow
pip install requests
pip install django-model-utils
pip install djangorestframework
pip install geocoder
pip install geojson
```

##Run
```Python
python manage.py runserver
```

##If Modify Model, Then Command Below
```Python
python manage.py makemigrations
python manage.py migrate
```

##上面的Command沒用時
1. 把出錯的migrations資料夾裡面的東西刪掉(0001_initial.py & __init__.py)
2. 然後一樣執行上面的Command



