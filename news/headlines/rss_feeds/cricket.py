from django.contrib.syndication.views import Feed
from django.urls import reverse
from headlines.models import Title

class CricketFeed(Feed):
	title = "The Orient Chronicles"
	link = "/headlines/"
	description = "Top cricket based news."

	def items(self):
		return Title.objects.filter(news_category__startswith='cricket').order_by("-pub_date")[:10]

	def item_title(self, item):
		return item.title_text

	def item_description(self, item):
		return item.title_text

	def item_link(self, item):
		return item.news_url
