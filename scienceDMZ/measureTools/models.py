from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class scpTool(models.Model):
	ip_remoto 		= models.CharField(max_length=120)
	tamanho 		= models.CharField(max_length=120)
	limite			= models.CharField(max_length=120)
	pasta_ori		= models.CharField(max_length=120)
	pasta_des 		= models.CharField(max_length=120)
	pasta_resultado = models.CharField(max_length=120)

 	def __unicode__(self):
 		return smart_unicode(ip_remoto)
