from django.shortcuts import render
from django.utils import timezone
from .models import SearchRecord
from DBMgr.models import show, ConvenienceStore, Company, favoriteshow, favoritecompany, favoritestore
# Create your views here.

from django.views.generic import TemplateView
from itertools import chain


def search_record(request):
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
        show_filter = show.objects.filter(show_related__favorite_user_id=user_id)
        # print(show_filter)
        company_filter = Company.objects.filter(company_related__favorite_user_id=user_id)
        # print(company_filter)
        store_filter = ConvenienceStore.objects.filter(store_related__favorite_user_id=user_id)
        # print(store_filter)

        get_delete_number = request.POST.get('number')
        if get_delete_number:
            if "show" in get_delete_number:
                i = get_delete_number[4:]
                i_int = int(i)
                show_delete = favoriteshow.objects.filter(favorite_user_id=user_id, favorite_id=i)
                show_delete.delete()
            elif "company" in get_delete_number:
                i = get_delete_number[7:]
                i_int = int(i)
                company_delete = favoritecompany.objects.filter(favorite_user_id=user_id, favorite_id=i)
                company_delete.delete()
            elif "store" in get_delete_number:
                i = get_delete_number[5:]
                i_int = int(i)
                store_delete = favoritestore.objects.filter(favorite_user_id=user_id, favorite_id=i)
                store_delete.delete()
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

        return render(request, 'search_record.html', locals())

    else:
        return render(request, 'home.html', {'message': '未登入'})

# print(record[0].address)
# item_list = [{'address': 111, 'range': 222, 'time': 333},
#              {'address': 444, 'range': 555, 'time': 666}]

# get_time = timezone.now()
# time = timezone.localtime(get_time)
# time.strftime("%Y-%m-%d %H:%M:%S")

# return render(request, 'search_record.html',
#               {'address': address,
#                'range': range,
#                'time': time})
