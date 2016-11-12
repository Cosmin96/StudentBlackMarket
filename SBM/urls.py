from django.conf.urls import url

from . import views

app_name='SBM'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^authentication/$', views.authentication, name='authentication'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signin/$', views.signin, name='signin'),
	#url(r'^addproduct/$', views.addproduct, name='addproduct'),
	url(r'^errormsg/$', views.errormsg, name='errormsg'),
]