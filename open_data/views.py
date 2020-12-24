from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
# from django.contrib.auth.decorators import login_required

from .models import restaurant

from itertools import islice
# import datetime
import csv
# import collections
# import geocoder
# from geojson import Point, Feature, FeatureCollection
from pathlib import Path

# Create your views here.

# def import_restaurant(request):
#     base_path = Path(__file__).parent
#     file_path = (base_path / "Restaurants.csv").resolve()
#     try:
#         with open(file_path, encoding="utf-8", newline="") as csvfile:
#             rows = list(csv.reader(csvfile))
#             for row in islice(rows, 1, None):
#                 is_restaurant = restaurant.objects.filter(restaurant_name=row[0])
#                 if not is_restaurant:
#                     row = restaurant(restaurant_name=row[0], restaurant_address=row[1], country_id=row[2], city_id=row[3])
#                     row.save()
#         messages.error(request, '更新成功') 
#     except Exception as e:
#         messages.error(request, '更新失敗') 
#     return HttpResponseRedirect("http://127.0.0.1:8000")

 
def import_PHrestaurant(request):
    base_path = Path(__file__).parent
    file_path = (base_path / "Restaurants_Philippines.csv").resolve()
    try:
        with open(file_path, encoding="utf-8", newline="") as csvfile:
            rows = list(csv.reader(csvfile))
            for row in islice(rows, 1, None):
                is_restaurant = restaurant.objects.filter(restaurant_name=row[0])
                if not is_restaurant:
                    row = restaurant(restaurant_name=row[0], restaurant_address=row[1], country_id=row[2], city_id=row[3])
                    row.save()
        messages.error(request, '菲律賓餐廳～更新成功^0^') 
    except Exception as e:
        messages.error(request, '更新失敗:(') 
    return HttpResponseRedirect("http://127.0.0.1:8000")


def import_MYrestaurant(request):
    base_path = Path(__file__).parent
    file_path = (base_path / "Restaurants_Malaysia.csv").resolve()
    try:
        with open(file_path, encoding="utf-8", newline="") as csvfile:
            rows = list(csv.reader(csvfile))
            for row in islice(rows, 1, None):
                is_restaurant = restaurant.objects.filter(restaurant_name=row[0])
                if not is_restaurant:
                    row = restaurant(restaurant_name=row[0], restaurant_address=row[1], country_id=row[2], city_id=row[3])
                    row.save()
        messages.error(request, '馬來西亞餐廳～更新成功=)') 
    except Exception as e:
        messages.error(request, '更新失敗ˊˋ') 
    return HttpResponseRedirect("http://127.0.0.1:8000")


def import_TWrestaurant(request):
    base_path = Path(__file__).parent
    file_path = (base_path / "Restaurants_Taiwan.csv").resolve()
    try:
        with open(file_path, encoding="utf-8", newline="") as csvfile:
            rows = list(csv.reader(csvfile))
            for row in islice(rows, 1, None):
                is_restaurant = restaurant.objects.filter(restaurant_name=row[0])
                if not is_restaurant:
                    row = restaurant(restaurant_name=row[0], restaurant_address=row[1], country_id=row[2], city_id=row[3])
                    row.save()
        messages.error(request, '台灣餐廳～更新成功XD') 
    except Exception as e:
        messages.error(request, '更新失敗= =') 
    return HttpResponseRedirect("http://127.0.0.1:8000")


    # try:
    #     with open(file_path, encoding="utf-8-sig", newline="") as csvfile:
    #         rows = list(csv.reader(csvfile))
    #         for row in islice(rows, 0, None):
    #             is_restaurant = restaurant.objects.filter(restaurant_name=row[0])
    #             if not is_restaurant:
    #                 row = restaurant.objects.create(restaurant_name=row[0], restaurant_address=row[1], country_id=row[2], city_id=row[3])
    #                 row.save()
    #             # is_restaurant = restaurant.objects.filter(restaurant_name=row[0])
    #             # if not is_restaurant:
    #             #     row = restaurant(restaurant_name=row[0], restaurant_address=row[1], country_id=row[2], city_id=row[3])
    #             #     row.save()
    #         messages.add_message(request, messages.SUCCESS, '成功更新')
    # except Exception as e:
    #     messages.add_message(request, messages.ERROR, e)
    
    
    # return HttpResponseRedirect(reverse('open_data:import_restaurant'))

# http://127.0.0.1:8000/open_data/import_restaurant