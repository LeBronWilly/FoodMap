from django.http import HttpResponse
from django.shortcuts import render
from DBMgr.models import Company, ConvenienceStore, show, favoriteshow, favoritecompany, favoritestore
from django.db.models import Q


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        user_id = request.user.id


        # address = request.POST.get('address')
        # rge = request.POST.get('range')

        county = request.POST.get('county')
        district = request.POST.get('district')

        company = Company.objects.all()
        Show = show.objects.all()
        store = ConvenienceStore.objects.all()
        if county and district:
            company_filter = company.filter(Q(jobaddress__icontains=county) &
                                            Q(jobaddress__icontains=district)).distinct()
            Show_filter = Show.filter(Q(location__icontains=county) &
                                      Q(location__icontains=district)).distinct()
            store_filter = store.filter(Q(convenience_address__icontains=county) &

                                        Q(convenience_address__icontains=district)).distinct()

        # get_type = request.POST.get('type')
        # get_show_id = request.POST.get('show_id')
        # get_show_name = request.POST.get('show_name')
        # if get_show_id and get_show_name:
        #     print("下拉id= " + str(get_show_id))
        #     print("下拉name= " + str(get_show_name))

        # get_show_type_c = request.POST.get('type_c')
        # get_show_id_c = request.POST.get('show_id_c')
        # get_show_name_c = request.POST.get('show_name_c')
        # if get_show_id_c and get_show_name_c:
        #     print("加入收藏id= " + str(get_show_id_c))
        #     print("加入收藏name= " + str(get_show_name_c))
        #     favorite_show = favoriteshow(favorite_user_id=user_id, favorite_id=get_show_id_c)
        #     favorite_show.save()
        #
        # # get_company_type_c = request.POST.get('type_c')
        # get_company_id_c = request.POST.get('company_id_c')
        # get_company_name_c = request.POST.get('company_name_c')
        # if get_company_id_c and get_company_name_c:
        #     print("加入收藏id= " + str(get_company_id_c))
        #     print("加入收藏name= " + str(get_company_name_c))
        #     favorite_company = favoritecompany(favorite_user_id=user_id, favorite_id=get_company_id_c)
        #     favorite_company.save()
        #
        # get_store_id_c = request.POST.get('store_id_c')
        # get_store_name_c = request.POST.get('store_name_c')
        # if get_store_id_c and get_store_name_c:
        #     print("加入收藏id= " + str(get_store_id_c))
        #     print("加入收藏name= " + str(get_store_name_c))
        #     favorite_store = favoritestore(favorite_user_id=user_id, favorite_id=get_store_id_c)
        #     favorite_store.save()
        #
        # return render(request, 'index.html', locals())

        # 當登入後跳轉到首頁 地址和範圍都為空時，傳空值到template，
        # 沒傳值會報錯
        # if not address:
        #     if not rge:
        #         return render(request, 'index.html', locals())
        # else:
        #     if get_type == 1:
        #         favorite_show = favoriteshow(favorite_id=get_show_id,
        #                                      favorite_user_id=user_id)
        #         favorite_show.save()
        #     elif get_type == 2:
        #         favorite_company = favoritecompany(favorite_id=get_show_id,
        #                                            favorite_user_id=user_id)
        #         favorite_company.save()
        #     elif get_type == 3:
        #         favorite_store = favoritestore(favorite_id=get_show_id,
        #                                        favorite_user_id=user_id)
        #         favorite_store.save()
        # collection = SearchRecord(username=username,
        #                              address=address,
        #                              range=rge)
        # collection.save()
        # if get_delete_number:
        #     s2 = SearchRecord(id=get_delete_number, username=username)
        #     s2.delete()
        # return render(request, 'index.html', locals())
        return render(request, 'index.html', locals())
    else:
        user_id = 0
        county = request.POST.get('county')
        district = request.POST.get('district')

        company = Company.objects.all()
        Show = show.objects.all()
        store = ConvenienceStore.objects.all()
        if county and district:
            company_filter = company.filter(Q(jobaddress__icontains=county) &
                                            Q(jobaddress__icontains=district)).distinct()
            Show_filter = Show.filter(Q(location__icontains=county) &
                                      Q(location__icontains=district)).distinct()
            store_filter = store.filter(Q(convenience_address__icontains=county) &

                                        Q(convenience_address__icontains=district)).distinct()

        get_show_id = request.POST.get('show_id')
        get_show_name = request.POST.get('show_name')
        if get_show_name:
            print("下拉id= " + str(get_show_id))
            print("下拉name= " + str(get_show_name))
            show_add = Show.filter(title=str(get_show_name)).values()[0]['location']

        get_company_id = request.POST.get('company_id')
        get_company_name = request.POST.get('company_name')
        if get_company_id and get_company_name:
            print("下拉id= " + str(get_company_id))
            print("下拉name= " + str(get_company_name))

        get_store_id = request.POST.get('store_id')
        get_store_name = request.POST.get('store_name')
        if get_store_id and get_store_name:
            print("下拉id= " + str(get_store_id))
            print("下拉name= " + str(get_store_name))

        return render(request, 'index.html', locals())

# def login(request):
#     return render(request, 'login.html')
#
#
# def register(request):
#     return render(request, 'register.html')
