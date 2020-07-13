from django.db import models

# Create your models here.
STATUS=(
	('Ordered','Ordered'),
	('Deliveried','Deliveried'),
	)
class Product(models.Model):
	image			= models.ImageField()
	name			= models.CharField(max_length=200)
	discription		= models.CharField(max_length=260)
	price	= models.IntegerField()

	def __str__(self):
		return self.name

class Order(models.Model):
	product 	= models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity	= models.IntegerField(default=1)
	user_phone	= models.CharField(max_length=10)
	status		= models.CharField(max_length=10,choices=STATUS,default="Ordered")

	def __str__(self):
		return self.product.name