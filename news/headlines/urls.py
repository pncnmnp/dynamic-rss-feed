from django.urls import path
from . import views

urlpatterns = [
	path('', views.store, name='get_headlines'),
	path('all/', views.fetch, name='all_news')
]