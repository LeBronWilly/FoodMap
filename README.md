# Information Modeling Team12
Only three table

##Environment
<br>
Python x.x.x (3.8.6測試ok)
<br>
Django 2.2.6

##Install
```Python
pip install Pillow
pip install requests
pip install django==2.2.6
pip install django-import-export
pip install django-model-utils
pip install djangorestframework
pip install geocoder
pip install geojson
```

##Run
```Python
python manage.py runserver
```

##If Modify Model, Then Command Below, and Runserver
```Python
python manage.py makemigrations
python manage.py migrate
```

##若上面的Migration Command沒用時
1. 把出錯的migrations資料夾裡面的東西刪掉(0001_initial.py & __init__.py)
2. 然後一樣執行上面的Command

##匯入餐廳OpenData：http://localhost:8000/open_data/import_restaurant


