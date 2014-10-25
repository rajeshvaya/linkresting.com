from urlparse import urlparse

from django.db import models
from django.contrib.auth.models import User

class Story(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(unique=True)
	moderator =	models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created time")
	updated_at = models.DateTimeField(auto_now=True)

	@property
	def domain(self):
		return urlparse(self.url).netloc

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural='stories'