from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from mainapp.models import Product, Request
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core import validators
# Create your views here.
def index(request):
	if 'regist' in request.session:
		del request.session['regist']

	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('mainapp:authentication'))
	try:
		product = Product.objects.all()#.filter(owner = request.user)
	except Product.DoesNotExist:
		reflist = None

	user_counter = User.objects.count()
	product_counter = Product.objects.count()
	request_counter = Request.objects.count()

	context = {'products' : product , 'user_counter' : user_counter, 'product_counter' : product_counter, 'request_counter' : request_counter}
	return render(request, 'mainapp/index.html', context)

def reqpage(request):
	if 'regist' in request.session:
		del request.session['regist']

	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('mainapp:authentication'))
	try:
		req = Request.objects.all()#.filter(owner = request.user)
	except Product.DoesNotExist:
		reflist = None

	user_counter = User.objects.count()
	product_counter = Product.objects.count()
	request_counter = Request.objects.count()

	context = {'reqs' : req , 'user_counter' : user_counter, 'product_counter' : product_counter, 'request_counter' : request_counter}
	return render(request, 'mainapp/reqpage.html', context)

def newobject(request):
	return render(request, 'mainapp/newobject.html')

def newrequest(request):
	return render(request, 'mainapp/newrequest.html')

def newprofile(request):
	return render(request, 'mainapp/newprofile.html')

def signout(request):
	if 'regist' in request.session:
		del request.session['regist']
	logout(request)
	return HttpResponseRedirect(reverse('SBM:index'))

def changedata(request):
	firstname = request.POST['firstname']
	lastname = request.POST['lastname']
	user = request.POST['user']
	email = request.POST['email']
	if not(user and email and firstname and lastname):
		request.session['errormessage'] = 'Please complete all field in registration form!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))
	
	try:
		validators.validate_email(email)
	except:
		request.session['errormessage'] = 'Email is not valid!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))

	user = User.objects.get(username = request.user)
	user.first_name = firstname
	user.last_name = lastname
	user.user = user
	user.email = email
	user.save()
	request.session['regist'] = 'YES'
	return HttpResponseRedirect(reverse('mainapp:index'))

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
	file = request.POST['file']

	user = request.user
	product = Product(name = title, category = category, price = price, location = location, description = description, creator = user, file = file)
	product.save()

	return HttpResponseRedirect(reverse('mainapp:index'))

def addreq(request):
	if 'regist' in request.session:
		del request.session['regist']

	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('SBM:authentication'))

	title = request.POST['title']
	if title is '':
		request.session['errormessage'] = 'A title is required!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))

	category = request.POST['category']
	location = request.POST['location']
	description = request.POST['description']

	user = request.user
	req = Request(name = title, category = category, location = location, description = description, creator = user)
	req.save()

	return HttpResponseRedirect(reverse('mainapp:reqpage'))

def applyfilters(request):
	category = request.POST['category']
	price = request.POST['price']
	title = request.POST['title']
	location = request.POST['location']
	try:
		if(price is '5 or below'):
			product = Product.objects.all().filter(category = category, price__lte = 5, name = title, location = location)
		elif(price is '5-20'):
			product = Product.objects.all().filter(category = category, price__gt = 5, price__lte = 20, name = title, location = location)
		elif(price is '20-100'):
			product = Product.objects.all().filter(category = category, price__gt = 20, price__lte = 100, name = title, location = location)
		elif(price is '100 or above'):
			product = Product.objects.all().filter(category = category, price_gt = 100, name = title, location = location)
		elif(price is 'Any'):
			product = Product.objects.all().filter(category = category, name = title, location = location)
	except:
		request.session['errormessage'] = 'No such product found'
		return HttpResponseRedirect(reverse('SBM:errormsg'))

	product = Product.objects.all().filter(category = category, name = title, location = location)
	context = {'products': product}
	return render(request, 'mainapp/index.html', context)