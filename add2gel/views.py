from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from DBMgr.models import Company, ConvenienceStore, show


# Create your views here.
def add2gel(requests):
    company = Company.objects.all()
    convenience_store = ConvenienceStore.objects.all()
    showinfo = show.objects.all()

    table_selected: ''
    column_before: ''

    return render(requests, 'add2gel.html', locals())


def transfer(requests):
    try:
        company = Company.objects
        convenience_store = ConvenienceStore.objects
        showinfo = show.objects
        tb = requests.GET['table']
        dataid = requests.GET['id']
        lat = requests.GET['lat']
        lng = requests.GET['lng']

        if tb == 'company':
            t = company.get(id=dataid)
            t.joblatitude = lat
            t.joblongitude = lng
        elif tb == 'convenience_store':
            t = convenience_store.get(id=dataid)
            t.convenience_latitude = lat
            t.convenience_longitude = lng
        elif tb == 'showinfo':
            t = showinfo.get(id=dataid)
            t.latitude = lat
            t.longitude = lng
        else:
            return HttpResponse('ERROR!')

        t.save()

        return render_to_response('Transfer_finish.html')
    except Exception as e:
        print(str(e))
