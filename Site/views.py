from django.shortcuts import render
# Create your views here.



def index_client(request):
    return render(request, 'base_client.html')

def index_taxi(request):
    return render(request, 'base_taxi.html')


def login(request):
    return render(request, 'login.html')

def taxiForms(request):
    return render(request, 'moto_taxi_forms.html')

def clientForms(request):
    return render(request, 'cliente_forms.html')