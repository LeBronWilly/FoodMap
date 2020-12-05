from django.http import HttpResponse
from django.shortcuts import render
from open_data.models import Company, ConvenienceStore, show, Restaurant
from collection.models import favoriteshow, favoritecompany, favoritestore
from django.db.models import Q
from areas.models import Country
from areas.models import City
# Create your views here.


def index(request):
    countrys = Country.objects.all().distinct()

    city_all = City.objects.all().distinct()
    # citys_2 = City.objects.filter(country_id=2).distinct()
    # citys_3 = City.objects.filter(country_id=3).distinct()

    chose_country = request.POST.get('chose_country')
    chose_city = request.POST.get('city')
    select_restaurant = Restaurant.objects.filter(country_id=chose_country, city_id=chose_city).distinct()


    print(chose_country,chose_city)

    # chose_area = request.POST.get('chose_area')

    district = request.POST.get('district')
    country = request.POST.get('chose_country')

    county = request.POST.get('county')
    # print(county,district,chose_area)
    # if county and district:
    #     Restaurants_all = Restaurant.objects.all()
    #     Restaurant_filter = Restaurants_all.filter(Q(restaurant_address__icontains=county) &
    #                             Q(restaurant_address__icontains=district)).distinct()

    if request.user.is_authenticated:
        user_id = request.user.id

        # address = request.POST.get('address')
        # rge = request.POST.get('range')

        # county = request.POST.get('county')
        # district = request.POST.get('district')

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

        get_show_id_c = request.POST.get('show_id_c')
        get_show_name_c = request.POST.get('show_name_c')
        if get_show_id_c and get_show_name_c:
            print("加入收藏id= " + str(get_show_id_c))
            print("加入收藏name= " + str(get_show_name_c))
            favorite_show = favoriteshow(favorite_user_id=user_id, favorite_id=get_show_id_c)
            favorite_show.save()

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

        return render(request, 'index.html', locals())
    else:
        user_id = 0
        # county = request.POST.get('county')
        # district = request.POST.get('district')

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

