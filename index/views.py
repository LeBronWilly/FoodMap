from django.http import HttpResponse
from django.shortcuts import render
from search_record.models import SearchRecord
from DBMgr.models import Company, ConvenienceStore, show
from django.db.models import Q


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        get_show_name = request.POST.get('show_name')
        get_company_name = request.POST.get('company_name')
        get_store_name = request.POST.get('store_name')
        print(get_show_name, get_company_name, get_store_name)
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

        username = request.user.username
        address = request.POST.get('address')
        rge = request.POST.get('range')
        get_number = request.POST.get('number')

        # 當登入後跳轉到首頁 地址和範圍都為空時，傳空值到template，
        # 沒傳值會報錯
        if not address:
            if not rge:
                return render(request, 'index.html', locals())
        else:
            search_record = SearchRecord(username=username,
                                         address=address,
                                         range=rge)
            search_record.save()
            if get_number:
                s2 = SearchRecord(id=get_number, username=username)
                s2.delete()
            return render(request, 'index.html', locals())
    else:
        get_show_name = request.POST.get('show_name')
        get_company_name = request.POST.get('company_name')
        get_store_name = request.POST.get('store_name')
        print(get_show_name, get_company_name, get_store_name)
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

        username = request.user.username
        address = request.POST.get('address')
        rge = request.POST.get('range')
        get_number = request.POST.get('number')
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
        # address = request.POST.get('address')
        #         # rge = request.POST.get('range')
        return render(request, 'index.html', locals())


def add2collection(request):
    if request.method == "POST":
        show_name = request.POST.get('showSelect')
        job_name = request.POST.get('jobSelect')
        store_name = request.POST.get('storeSelect')
        print(show_name, job_name, store_name)


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
