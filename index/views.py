from django.shortcuts import render

# Create your views here.


def index(request):
    address = request.POST.get('address')
    rge = request.POST.get('range')
    return render(request, 'index.html',
                  {'address': address,
                   'range': rge})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')




