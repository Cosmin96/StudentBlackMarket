from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from SBM.models import Product
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core import validators
from django.views.decorators.csrf import csrf_protect

def index(request):
	return render(request, 'SBM/index.html')


def authentication(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('SBM:index'))
	return render(request, 'SBM/login-signup.html')

def signout(request):
	if 'regist' in request.session:
		del request.session['regist']

	logout(request)
	return HttpResponseRedirect(reverse('SBM:index'))


def signup(request):
	if 'regist' in request.session:
		del request.session['regist']

	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('SBM:mainpage'))
	
	firstname = request.POST['firstname']
	lastname = request.POST['lastname']
	user = request.POST['user']
	email = request.POST['email']
	password = request.POST['password']
	repassword = request.POST['repassword']
	
	if not(user and email and password and repassword and firstname and lastname):
		request.session['errormessage'] = 'Please complete all field in registration form!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))
	
	if password != repassword:
		request.session['errormessage'] = 'The passwords inserted do not match!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))

	if len(password) < 6:
		request.session['errormessage'] = 'Passwords must be at least 6 characters long!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))
	
	try:
		validators.validate_email(email)
	except:
		request.session['errormessage'] = 'Email is not valid!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))
	
	if User.objects.filter(email=email).exists():
		request.session['errormessage'] = 'Email already used!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))

	user = User.objects.create_user(user, email, password)
	user.first_name = firstname
	user.last_name = lastname
	user.save()
	request.session['regist'] = 'YES'
	return HttpResponseRedirect(reverse('SBM:authentication'))

def signin(request):
	if 'regist' in request.session:
		del request.session['regist']

	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('SBM:index'))
	email = request.POST['email']
	password =  request.POST['password']

	try:
		user1 = User.objects.get(email = email)
	except User.DoesNotExist:
		request.session['errormessage'] = 'Credentials are wrong!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))
	
	user1 = User.objects.get(email = email)

	user = authenticate(username = user1.username, password = password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('SBM:index'))
	else:
		request.session['errormessage'] = 'Credentials are wrong!'
		return HttpResponseRedirect(reverse('SBM:errormsg'))

def errormsg(request):
	if 'regist' in request.session:
		del request.session['regist']

	errormessage = request.session['errormessage']
	request.session['errormessage'] = None
	
	context = {'errormessage' : errormessage}
	return render(request, 'SBM/errormessage.html', context)