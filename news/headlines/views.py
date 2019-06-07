import pickle
from django.shortcuts import render
from json import load
from . import fetch_news
from .models import Title
from django.http import HttpResponse

def store(request):
	news_obj = fetch_news.Fetch_News()
	news_content = dict()
	if news_obj.check_news() == False:
		news_content = news_obj.get_pickle()
	else:
		news_content = news_obj.news_content

	category_path = './headlines/datasets/categories.json'
	categories = load(open(category_path))

	for category in categories:
		index = 0
		while(True):
			try:
				news_instance = Title.objects.create(
					title_text=news_content[category][index]['title'],
					pub_date=news_content[category][index]['date'],
					news_url=news_content[category][index]['links'],
					description=news_content[category][index]['desc']
				)
				index += 1
			except:
				break

	return HttpResponse("here news will be fetched")

def fetch(request):
	return HttpResponse("here news will be displayed")
