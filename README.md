# FoodMap

##Data Table:
<br>
使用者、收藏、餐廳、國家、城市

##Environment
<br>
Python 3.8.6
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

##匯入餐廳OpenData到資料庫：
<br>
匯入菲律賓餐廳：http://127.0.0.1:8000/open_data/import_PHrestaurant
<br>
匯入馬來西亞餐廳：http://127.0.0.1:8000/open_data/import_MYrestaurant
<br>
匯入台灣餐廳（北部地區）：http://127.0.0.1:8000/open_data/import_TWrestaurant
<br>
匯入台灣餐廳（全台）：http://127.0.0.1:8000/open_data/import_TWrestaurant_all
