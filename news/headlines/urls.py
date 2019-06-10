from django.urls import path
from . import views
from headlines.rss_feeds.top import TopFeed
from headlines.rss_feeds.world import WorldFeed
from headlines.rss_feeds.tech import TechFeed
from headlines.rss_feeds.sports import SportsFeed
from headlines.rss_feeds.science import ScienceFeed
from headlines.rss_feeds.india import IndiaFeed
from headlines.rss_feeds.cricket import CricketFeed
from headlines.rss_feeds.business import BusinessFeed

urlpatterns = [
	path('', views.fetch, name='all_news'),
	path('update/', views.store, name='get_headlines'),
	path('feeds/top/', TopFeed()),
	path('feeds/world/', WorldFeed()),
	path('feeds/tech/', TechFeed()),
	path('feeds/sports/', SportsFeed()),
	path('feeds/science/', ScienceFeed()),
	path('feeds/india/', IndiaFeed()),
	path('feeds/cricket/', CricketFeed()),
	path('feeds/business/', BusinessFeed())
]
