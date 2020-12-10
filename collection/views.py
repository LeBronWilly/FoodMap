from django.shortcuts import render
from django.utils import timezone
# from open_data.models import show, ConvenienceStore, Company
# from collection.models import favoriteshow, favoritecompany, favoritestore
from open_data.models import restaurant
from collection.models import favorite_restaurant
# Create your views here.

from django.views.generic import TemplateView
from itertools import chain


def collection(request):
    # address = 111
    # range = 222
    # if request.is_ajax():
    #     # # 直接获取所有的post请求数据
    #     # data = request.POST
    #     # 获取其中的某个键的值
    #     number_tmp = request.POST.get("number")
    #     number = int(number_tmp)
    #     print(number)
    #     SearchRecord.objects.filter(id=number).delete()
    #     # 将前端传来的数据再次传回前端，只是为了测试
    #     # response = JsonResponse({"host": host}
    #     # return response
    if request.user.is_authenticated:
        user_id = request.user.id

        restaurant_filter = restaurant.objects.filter(restaurant_related__favorite_user_id=user_id)


        get_delete_number = request.POST.get('number')
        # print(get_delete_number)

        if get_delete_number:
            # if "restaurant" in get_delete_number:
            i = get_delete_number
            print(i)
            i_int = int(i)
            restaurant_delete = favorite_restaurant.objects.filter(favorite_user_id=user_id, favorite_id=i)
            restaurant_delete.delete()
        #     elif "company" in get_delete_number:
        #         i = get_delete_number[7:]
        #         i_int = int(i)
        #         company_delete = favoritecompany.objects.filter(favorite_user_id=user_id, favorite_id=i)
        #         company_delete.delete()
        #     elif "store" in get_delete_number:
        #         i = get_delete_number[5:]
        #         i_int = int(i)
        #         store_delete = favoritestore.objects.filter(favorite_user_id=user_id, favorite_id=i)
        #         store_delete.delete()

        # show_delete = favoriteshow(favorite_id=get_delete_number)
        # show_delete.delete()
        # if 'show' in get_delete_number:
        #     int_get_delete_number = int(get_delete_number)
        #     show_delete = favoriteshow(favorite_id=get_delete_number)
        #     show_delete.delete()
        #     # company_delete = favoritecompany(favorite_id=get_delete_number)
        #     # store_delete = favoritestore(favorite_id=get_delete_number)
        #     #
        #     # company_delete.delete()
        #     # store_delete.delete()

        return render(request, 'collection.html', locals())

    else:
        return render(request, 'home.html', {'message': '未登入'})

# print(record[0].address)
# item_list = [{'address': 111, 'range': 222, 'time': 333},
#              {'address': 444, 'range': 555, 'time': 666}]

# get_time = timezone.now()
# time = timezone.localtime(get_time)
# time.strftime("%Y-%m-%d %H:%M:%S")

# return render(request, 'collection.html',
#               {'address': address,
#                'range': range,
#                'time': time})
