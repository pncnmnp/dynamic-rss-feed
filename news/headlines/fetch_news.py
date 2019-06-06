import feedparser
from json import load

class fetch_news:
	def __init__(self):
		self.news_content = {}

	def scrape(self):
		url_link_path = './datasets/categories.json'
		urls = load(open(url_link_path))

		for category in urls:
			for source in urls[category]:
				feed = feedparser.parse(source)
				index = 0

				while(True):
					try:
						if category not in self.news_content:
							self.news_content[category] = list()
						self.news_content[category].append(
							{	'title': feed.entries[index].title,
								'date': feed.entries[index].published,
								'links': feed.entries[index].link,
								'desc': feed.entries[index].description
							}
						)
						index += 1
					except:
						break

if __name__ == '__main__':
	obj = fetch_news()
	obj.scrape()
