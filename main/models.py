from django.db import models

# Create your models here.

class booking(models.Model):
	first_name = models.CharField('First Name', max_length=120)
	last_name = models.CharField('Last Name', max_length=120)
	address = models.CharField(max_length=300)
	phone = models.CharField('Contact Phone', max_length=25)
	category = models.CharField('Category', blank=True, max_length=25)
	description = models.TextField(blank=True)
	quantity = models.CharField("Quantity", blank=True, max_length=25)
	collection_date = models.DateTimeField('Collection Date')
	approved = models.BooleanField('Approved', default=False)
	
	def __str__(self):
		return self.first_name + ' ' + self.last_name

