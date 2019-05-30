from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
class ListeArticles(ListView):
	template_name = "actuality/article_list.html"


class login():
	pass	
