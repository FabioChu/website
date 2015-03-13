from django.db import models
from django.utils.encoding import smart_unicode #utf-8
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	institution = models.CharField(max_length=120)
 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
  	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

 	def __unicode__(self):
 		return smart_unicode(self.user.email)