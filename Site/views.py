from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.contrib.auth import authenticate
from .forms import *
from .models import *
from django.http.response import HttpResponse
from django.contrib.auth import login as django_login
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index_client(request):
    return render(request, 'base_client.html')

def index_taxi(request):
    return render(request, 'base_taxi.html')


from django.http import JsonResponse


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
        return JsonResponse(data)
    


class SignUpView_Taxi(FormView):
    '''
    Generic FormView with our mixin for user sign-up with reCAPTURE security
    '''

    template_name = "moto_taxi_forms.html"
    form_class = UserForm
    success_url = "/"


    #over write the mixin logic to get, check and save reCAPTURE score
    def form_valid(self, form):

        obj = form.save()
        obj.save()
        up = obj.MotoTaxi
        up.save()

        django_login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')
        #change result & message on success
        result = "Success"
        message = "Thank you for signing up"

        data = {'result': result, 'message': message}
        return JsonResponse(data)



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
		return JsonResponse(data)

def taxiForms(request):
    return render(request, 'moto_taxi_forms.html')

class clientForms(CreateView):
    template_name = 'cliente_forms.html'
    model = Client
    form_class = Cliente_forms
    success_url = '/login/'

class taxiForms(CreateView):
    template_name = 'moto_taxi_forms.html'
    model = MotoTaxi
    form_class = Moto_taxi_forms
    success_url = '/login/'