from django.conf.urls import url

from . import views

app_name='mainapp'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signout/$', views.signout, name='signout'),
	url(r'^addproduct/$', views.addproduct, name='addproduct'),
	url(r'^newobject/$', views.newobject, name='newobject'),
	url(r'^newrequest/$', views.newrequest, name='newrequest'),
	url(r'^newprofile/$', views.newprofile, name='newprofile'),
	url(r'^changedata/$', views.changedata, name='changedata'),
	url(r'^applyfilters/$', views.applyfilters, name='applyfilters'),
	url(r'^addreq/$', views.addreq, name='addreq'),
	url(r'^reqpage/$', views.reqpage, name='reqpage'),
]

