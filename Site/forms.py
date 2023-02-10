from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class UserForm(UserCreationForm):
        
	first_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
	last_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )
                

class motoForms(forms.ModelForm):
    model = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Modelo'}))
    brand = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Marca'}))
    color = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Cor'}))
    year = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': '*Ano'}))
    picture_moto = forms.ImageField()

    class Meta:
        model = Motorcycle
        fields = ('model', 'brand', 'color', 'year', 'picture_moto')

class Cliente_forms(UserCreationForm):

  username = forms.CharField(label="name", max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Nome completo'}))
  age = forms.IntegerField(label="age", max_value=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Idade'}))
  cpf = forms.CharField(label="CPF", max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'CPF'}))
  email = forms.EmailField(label="E-mail", max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Email'}))  
  picture = forms.ImageField()
  balance = forms.DecimalField(max_digits=100, decimal_places=2)

  class Meta:
    model = Client
    fields = ['username','age','cpf','email', 'picture', 'balance']

class Moto_taxi_forms(UserCreationForm):

  username = forms.CharField(label="name", max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Nome completo'}))
  age = forms.IntegerField(label="age", max_value=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Idade'}))
  cpf = forms.CharField(label="CPF", max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'CPF'}))
  email = forms.EmailField(label="E-mail", max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder' : 'Email'}))  
  picture = forms.ImageField()
  balance = forms.DecimalField(max_digits=100, decimal_places=2)
  cnh = forms.CharField(label="cnh", max_length=50, required=True)
  

  class Meta:
    model = MotoTaxi
    fields = ['username','age','cpf','email', 'picture','cnh', 'balance']

class AuthForm(AuthenticationForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha','class':'password'}))


class rideForm(forms.ModelForm):
    value = forms.DecimalField(max_digits=100, decimal_places=2)
    distance = forms.DecimalField(max_digits=100, decimal_places=2)
    start = forms.CharField(max_length=100)
    end = forms.CharField(max_length=100)
    motoTax = forms.ModelChoiceField(MotoTaxi.objects.filter(status=False))

    class Meta:
        model = Ride
        fields = ['value', 'distance', 'start', 'end', 'motoTax']
