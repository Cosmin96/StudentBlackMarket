from django.conf.urls import url

from . import views

app_name='mainapp'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signout/$', views.signout, name='signout'),
	url(r'^addproduct/$', views.addproduct, name='addproduct'),
	url(r'^newobject/$', views.newobject, name='newobject'),
	url(r'^newrequest/$', views.newrequest, name='newrequest'),
]
