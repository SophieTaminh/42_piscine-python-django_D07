from django.urls import path
from django.conf.urls import  url, include
from django.views.generic import ListView

from . import views
from .models import Article

urlpatterns = [
	#url de l'accueil
	 url(r'^$', ListView.as_view(model=Article,)),
]