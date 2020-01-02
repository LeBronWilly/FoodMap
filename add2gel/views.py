from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from open_data.models import Company, ConvenienceStore, show
import googlemaps


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


def batch_transfer(requests):
    try:
        company = Company.objects
        convenience_store = ConvenienceStore.objects
        showinfo = show.objects
        tb = requests.GET['table']
        gmaps = googlemaps.Client(key='AIzaSyAgvvjFFN4uKJg3Pw7yDQNfdB4S26OJSXE')

        if tb == 'company':
            betran = company.filter(joblatitude='0.0')

            for list in betran:
                if list.jobaddress != '':
                    latlng = gmaps.geocode(list.jobaddress)
                    list.joblatitude = latlng[0]['geometry']['location']['lat']
                    list.joblongitude = latlng[0]['geometry']['location']['lng']
                    list.save()

        elif tb == 'convenience_store':
            betran = convenience_store.filter(convenience_latitude='0.0')

            for list in betran:
                    if list.convenience_address != '':
                        latlng = gmaps.geocode(list.convenience_address)
                        list.convenience_latitude = latlng[0]['geometry']['location']['lat']
                        list.convenience_longitude = latlng[0]['geometry']['location']['lng']
                        list.save()

        elif tb == 'showinfo':
            betran = showinfo.filter(latitude='0.0')

            for list in betran:
                if list.location != '':
                    latlng = gmaps.geocode(list.location)
                    list.latitude = latlng[0]['geometry']['location']['lat']
                    list.longitude = latlng[0]['geometry']['location']['lng']
                    list.save()

        else:
            return HttpResponse('GET tag info error.')

        return render_to_response('transfer_finish.html')

    except Exception as e:
        print(str(e))
