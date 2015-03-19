from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class scpTool(models.Model):
	ip_remoto 		= models.CharField(max_length=120, default = '172.20.5.20')
	tamanho 		= models.CharField(max_length=120, default = '1G')
	limite			= models.CharField(max_length=120, default = '1')
	pasta_ori		= models.CharField(max_length=120, default = '~/Documents')
	pasta_des 		= models.CharField(max_length=120, default = '/dados/area-teste')
	pasta_resultado = models.CharField(max_length=120, default = 'Resultados')

 	def __unicode__(self):
 		return smart_unicode(ip_remoto)

class gridftpTool(models.Model):
	ip_remoto 		= models.CharField(max_length=120, default = '172.20.5.20')
	tamanho 		= models.CharField(max_length=120, default = '1G')
	limite			= models.CharField(max_length=120, default = '1')
	pasta_ori		= models.CharField(max_length=120, default = '~/Documents')
	pasta_des 		= models.CharField(max_length=120, default = '/dados/area-teste')
	fluxo	 		= models.CharField(max_length=120, default = '1')
	pasta_resultado = models.CharField(max_length=120, default = 'Resultados')
	
 	def __unicode__(self):
 		return smart_unicode(ip_remoto)

class wgetTool(models.Model):
	ip_remoto 		= models.CharField(max_length=120, default = '172.20.5.20')
	tamanho 		= models.CharField(max_length=120, default = '1G')
	limite			= models.CharField(max_length=120, default = '1')
	pasta_des 		= models.CharField(max_length=120, default = '/dados/area-teste')
	pasta_resultado = models.CharField(max_length=120, default = 'Resultados')
	
 	def __unicode__(self):
 		return smart_unicode(ip_remoto)

class Scp(models.Model):
	data 		= models.CharField(max_length=120)
	velocidade  = models.CharField(max_length=120)
	tamanho 	= models.CharField(max_length=120)
	objects 	= models.Manager()