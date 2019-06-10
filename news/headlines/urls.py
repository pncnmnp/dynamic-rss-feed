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
	path('feeds/top/', TopFeed(), name='feed_top'),
	path('feeds/world/', WorldFeed(), name='feed_world'),
	path('feeds/tech/', TechFeed(), name='feed_tech'),
	path('feeds/sports/', SportsFeed(), name='feed_sports'),
	path('feeds/science/', ScienceFeed(), name='feed_science'),
	path('feeds/india/', IndiaFeed(), name='feed_india'),
	path('feeds/cricket/', CricketFeed(), name='feed_cricket'),
	path('feeds/business/', BusinessFeed(), name='feed_business')
]
