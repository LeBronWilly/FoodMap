from django.shortcuts import render
from django.utils import timezone
from .models import  SearchRecord
# Create your views here.
from django.shortcuts import render_to_response
from django.views.generic import TemplateView


def search_record(request):
    # address = 111
    # range = 222
    record = SearchRecord.objects.all()
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
    return render(request, 'search_record.html', locals())



