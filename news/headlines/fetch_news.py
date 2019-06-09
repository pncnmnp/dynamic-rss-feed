import feedparser
import pickle
from json import load
from datetime import datetime
from os import path
from nltk import FreqDist, tokenize

STOPWORD_FILE = './headlines/datasets/stopwords.json'

class Fetch_News:
	def __init__(self):
		self.news_content = {}
		self.directory = './headlines/datasets/past_news/'
		self.stopwords = set(load(open(STOPWORD_FILE)))
		self.file = str()
		self.top_stories = {}

	def get_filename(self):
		'''
        Sets the filename according to the current date.
		'''
		self.file = datetime.now().strftime("%d-%m-%Y") + '.pickle'

	def top_news(self, news_content):
		'''
        Finds the top news from news_content dict. and updates the 'top_stories' instance var.
        The news_content parameter must match the standard as that of 'news_content' instance var.
        The news_content is a 'dictionary' containing 'list' of news.
        Each index of 'list' contains a dictionary with keys:
        'title', 'date', 'links', 'desc'.
        The format of news_content param. is :
            news_content = {'category_1': [{'title': 'xyz', 'date': '123', 'links': 'abc', 'desc': 'efg'},
                                           {'title': 'abc', 'date': '345', 'links': 'opq', 'desc': 'jkl'}],
                            'category_2': [.....]
                           }
		'''
		no_of_top_words = 40
		word_threshold = 1
		for category in news_content.keys():
			self.top_stories[category] = list()
			# Finding all titles from the category
			all_titles = [news_content[category][i]['title'] 
							for i in range(len(news_content[category]))]

			# Finding frequency of ALL words in ALL titles
			freq = 	FreqDist(
						word.lower() for word in tokenize.word_tokenize(' '.join(all_titles)) 
							if word.lower() not in self.stopwords
					)
			# Highest Frequency Words
			hot_words = [word[0] for word in freq.most_common(no_of_top_words)]

			# Finding titles containing hot_words above a certain threshold
			hot_news = 	[title for title in all_titles if 
							len(set(title.split(' ')).intersection(set(hot_words))) > word_threshold]

			# Curating the top_news
			for top_story in hot_news:
				self.top_stories[category].append(news_content[category][all_titles.index(top_story)])

	def check_news(self):
		'''
        Checks: if the news is older than 'time_diff' hours or 
                if the news' file does not exists
                scrape news and return True,
                else return False.
        Currently 'time_diff' is 2 hrs. ( subject to change )
		'''
		time_diff = -1
		self.get_filename()
		if path.isfile(self.directory + self.file) == True:
			curr_hour = datetime.now().hour
			past_hour = datetime.fromtimestamp(
							path.getmtime(self.directory + self.file)
						).hour
			if curr_hour - past_hour > time_diff:
				print("HERE")
				self.scrape()
				return True
			return False

		else:
			self.scrape()
			return True

	def scrape(self):
		'''
        Scrapes news from urls mentioned in:
            './headlines/datasets/news_urls.json'
        And 'pickles' the result by calling method pickle_news()

        Pickled news is stored in the format:

        News content is stored in a 'dictionary' containing 'list' of news.
        Each index of 'list' contains a dictionary with keys:
            'title', 'date', 'links', 'desc'.
        The format of news_content param. is :
            news_content = {'category_1': [{'title': 'xyz', 'date': '123', 'links': 'abc', 'desc': 'efg'},
                                           {'title': 'abc', 'date': '345', 'links': 'opq', 'desc': 'jkl'}],
                            'category_2': [.....]
                           }
		'''
		url_link_path = './headlines/datasets/news_urls.json'
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

		# store scraped news in pickle format
		self.pickle_news()

	def pickle_news(self):
		'''
        'news_content' instance var. is stored in path mentioned by:
            'dictionary' + 'file' instance var.
		'''
		dbfile = open(self.directory + self.file, 'wb')
		pickle.dump(self.news_content, dbfile)
		dbfile.close()

	def get_pickle(self):
		'''
        Returns the pickled news stored in:
            'dictionary' + 'file' instance var.
        See scrape() for type of object returned.    
		'''
		dbfile = open(self.directory + self.file, 'rb')
		news = pickle.load(dbfile)
		dbfile.close()
		return news

if __name__ == '__main__':
	obj = Fetch_News()
	obj.check_news()
