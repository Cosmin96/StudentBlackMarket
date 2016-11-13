from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from mainapp.models import Product
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core import validators
# Create your views here.
def index(request):
	return render(request, 'mainapp/index.html')

def newobject(request):
	return render(request, 'mainapp/newobject.html')


def signout(request):
	if 'regist' in request.session:
		del request.session['regist']
	logout(request)
	return HttpResponseRedirect(reverse('SBM:index'))

def addproduct(request):
	if 'regist' in request.session:
		del request.session['regist']

	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('SBM:authentication'))

	title = request.POST['title']
	if title is '':
		request.session['errormessage'] = 'A title is required!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))

	category = request.POST['category']
	price = request.POST['price']
	location = request.POST['location']
	description = request.POST['description']

	user = request.user
	product = Product(title = title, category = category, price = price, location = location, description = description, creator = user)
	product.save()

	return HttpResponseRedirect(reverse('mainapp:index'))