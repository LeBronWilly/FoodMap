from django.shortcuts import render
from django.utils import timezone
from DBMgr.models import show, ConvenienceStore, Company, favoriteshow, favoritecompany, favoritestore
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
        get_show_id_c = request.POST.get('show_id_c')
        get_show_name_c = request.POST.get('show_name_c')
        if get_show_id_c and get_show_name_c:
            print("加入收藏id= " + str(get_show_id_c))
            print("加入收藏name= " + str(get_show_name_c))
            favorite_show = favoriteshow(favorite_user_id=user_id, favorite_id=get_show_id_c)
            favorite_show.save()

        # get_company_type_c = request.POST.get('type_c')
        get_company_id_c = request.POST.get('company_id_c')
        get_company_name_c = request.POST.get('company_name_c')
        if get_company_id_c and get_company_name_c:
            print("加入收藏id= " + str(get_company_id_c))
            print("加入收藏name= " + str(get_company_name_c))
            favorite_company = favoritecompany(favorite_user_id=user_id, favorite_id=get_company_id_c)
            favorite_company.save()

        get_store_id_c = request.POST.get('store_id_c')
        get_store_name_c = request.POST.get('store_name_c')
        if get_store_id_c and get_store_name_c:
            print("加入收藏id= " + str(get_store_id_c))
            print("加入收藏name= " + str(get_store_name_c))
            favorite_store = favoritestore(favorite_user_id=user_id, favorite_id=get_store_id_c)
            favorite_store.save()

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

# return render(request, 'collection.html',
#               {'address': address,
#                'range': range,
#                'time': time})
