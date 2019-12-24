from django.shortcuts import render
from search_record.models import SearchRecord

# Create your views here.


def index(request):
    if request.user.is_authenticated:
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
        address = request.POST.get('address')
        rge = request.POST.get('range')
        return render(request, 'index.html', locals())


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')




