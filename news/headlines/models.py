from django.db import models

class Title(models.Model):
	title_text = models.CharField(max_length=300)
	pub_date = models.CharField(max_length=200)
	news_url = models.URLField(max_length=200)
	description = models.TextField()
	news_category = models.CharField(max_length=100)

	def __repr__(self):
		return str([self.title_text, 
					self.pub_date, 
					self.news_url, 
					self.description, 
					self.news_category]
				)
