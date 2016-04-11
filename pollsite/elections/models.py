import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	key = models.CharField(max_length=64)
	
	def __unicode__(self):
		return self.user.username


class Candidate(models.Model):
	candidate_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.candidate_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
	candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text