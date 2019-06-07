from django.urls import path
from . import views

urlpatterns = [
	path('', views.fetch, name='all_news'),
	path('update/', views.store, name='get_headlines')
]