from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^first$', views.index, name='index')
]