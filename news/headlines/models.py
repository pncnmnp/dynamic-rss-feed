from django.db import models

class Title(models.Model):
	title_text = models.CharField(max_length=300)
	pub_date = models.CharField(max_length=200)
	news_url = models.URLField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.title_text
