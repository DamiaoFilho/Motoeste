from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, TemplateView, UpdateView, ListView
from django.contrib.auth import authenticate
from .forms import *
from .models import *
from django.http.response import HttpResponse
from django.contrib.auth import login as django_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def getUser(request):
    try:
        return Client.objects.get(username=request.user.username)
    except:
        return MotoTaxi.objects.get(username=request.user.username)

@login_required
def index(request):
    try:
        user = Client.objects.get(username=request.user.username)
        return render(request, 'base_client.html', context={'commom': user})
    except:
        user = MotoTaxi.objects.get(username=request.user.username)
        return render(request, 'base_taxi.html', context={'commom': user})



from django.http import JsonResponse

@login_required
def activeRide(request):
    user = getUser(request)
    print(user)
    try:
        ride = Ride.objects.get(motoTax=user.id, status=True)
        return render(request, 'active_rides.html', context={'ride':ride})
    except:
        return redirect('/index/')       
    



class SignUpView_Client(FormView):
    '''
    Generic FormView with our mixin for user sign-up with reCAPTURE security
    '''

    template_name = "cliente_forms.html"
    form_class = Cliente_forms
    success_url = "/"


    #over write the mixin logic to get, check and save reCAPTURE score
    def form_valid(self, form):

        obj = form.save()
        obj.save()
        django_login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')
        #change result & message on success
        result = "Success"
        message = "Thank you for signing up"

        data = {'result': result, 'message': message}
        return redirect('/login/')


class init(TemplateView):
     template_name = 'init.html'



def SignUpView_Taxi(request):
    if request.method == "GET":
        taxiForm = Moto_taxi_forms()
        motoForm = motoForms()
        return render(request, 'moto_taxi_forms.html', context={'form':taxiForm, 'motoForm': motoForm})
    else:
        taxiForm = Moto_taxi_forms(request.POST, request.FILES)
        motoForm = motoForms(request.POST, request.FILES)

        if taxiForm.is_valid() and motoForm.is_valid():
            moto = motoForm.save()
            taxi = taxiForm.save(False)

            taxi.motorcycle = moto
            taxi.save()

            return redirect('/login/')
        
        return render(request, 'moto_taxi_forms.html', context={'form':taxiForm, 'motoForm': motoForm})



@login_required
def createRides(request):
    if request.method == "GET":
        form = rideForm()
        user = Client.objects.get(username=request.user.username)
        return render(request, 'create_ride.html', context={'form':form, 'commom':user})
    else:
        form = rideForm(request.POST)
        if form.is_valid():
            user = Client.objects.get(username=request.user.username)
            obj = form.save(False)
            obj.cliente = user

            if obj.motoTax.status==False and user.status==False:
                if user.transfer(obj.value, obj.motoTax):
                    obj.motoTax.status = True
                    user.status = True
                    user.save()
                    obj.motoTax.save()
                    obj.save()
                    return redirect('/index/')
                else:
                    return redirect('/index/')
            else:
                    return redirect('/index/')
        
        user = Client.objects.get(username=request.user.username)
        return render(request, 'create_ride.html', context={'form':form, 'commom':user})


@login_required
def update(request):
    if request.method == "GET":
        form = rideForm()
        user = Client.objects.get(username=request.user.username)
        return render(request, 'create_ride.html', context={'form':form, 'commom':user})
    else:
        form = rideForm(request.POST)
        if form.is_valid():
            user = Client.objects.get(username=request.user.username)
            obj = form.save(False)
            obj.cliente = user
            if user.balance.transfer(obj.value, obj.motoTax):
                obj.save()
                return redirect('/index/')
            else:
                return redirect('/index/')
        
        user = Client.objects.get(username=request.user.username)
        return render(request, 'create_ride.html', context={'form':form, 'commom':user})
        

class SignInView(FormView):
	'''
	Generic FormView with our mixin for user sign-in
	'''

	template_name = "login.html"
	form_class = AuthForm
	success_url = "/"

	def form_valid(self, form):
		
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		#attempt to authenticate user
		user = authenticate(self.request, username=username, password=password)
		if user is not None:
			django_login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
			result = "Success"
			message = 'You are now logged in'
		else:
			message = 'error'
		data = {'result': result, 'message': message}
		return redirect('/index/')

def endRide(request):
    user = getUser(request)
    ride = Ride.objects.get(motoTax=user.id, status=True)
    ride.status = False
    user.status = False
    ride.cliente.status = False

    ride.save()
    user.save()
    ride.cliente.save()
    return redirect('/index/')

@login_required
def end(request):
    logout(request)
    return redirect('/')


@login_required
def history(request):
    user = getUser(request)
    if isinstance(user, MotoTaxi):
        print("taxi")
        rides = Ride.objects.filter(motoTax=user.id) 
        return render(request, 'history_taxi.html', context={'rides':rides, 'commom': user})
    else:
        print("cliente")
        rides = Ride.objects.filter(cliente=user.id)
        return render(request, 'history_client.html', context={'rides':rides, 'commom': user})



