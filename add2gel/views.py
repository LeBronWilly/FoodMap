from django.shortcuts import render
from DBMgr.models import Company, ConvenienceStore, show


# Create your views here.
def add2gel(requests):
    company = Company.objects.all()
    convenience_store = ConvenienceStore.objects.all()
    showinfo = show.objects.all()

    table_selected: ''
    column_before: ''

    return render(requests, 'add2gel.html', locals())
