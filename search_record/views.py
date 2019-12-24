from django.shortcuts import render
from django.utils import timezone
from .models import SearchRecord
# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import TemplateView


def search_record(request):
    # address = 111
    # range = 222
    if request.is_ajax():
        # # 直接获取所有的post请求数据
        # data = request.POST
        # 获取其中的某个键的值
        number_tmp = request.POST.get("number")
        number = int(number_tmp)
        print(number)
        SearchRecord.objects.filter(id=number).delete()
        # 将前端传来的数据再次传回前端，只是为了测试
        # response = JsonResponse({"host": host}
        # return response
    if request.user.username:
        username = request.user.username
        record = SearchRecord.objects.filter(username=username)
        return render(request, 'search_record.html', locals())
    else:
        return render(request, 'search_record.html')

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
