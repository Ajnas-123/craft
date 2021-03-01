from django.db import models

# Create your models here.

class user_tb(models.Model):
	firstname=models.CharField(max_length=30,default='')
	lastname=models.CharField(max_length=30,default='')
	password=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=30,default='')
	# phone=models.CharField(max_length=30,default='')


class admin_tb(models.Model):
	name=models.CharField(max_length=100,default='')
	password=models.CharField(max_length=100,default='')

class product_tb(models.Model):
	name=models.CharField(max_length=30,default='')
	user=models.ForeignKey(user_tb,on_delete=models.CASCADE)
	item=models.ImageField(upload_to='img',default='')
	description=models.CharField(max_length=1000,default='')
	category=models.CharField(max_length=30,default='')
	status=models.CharField(max_length=30,default='')

class review_tb(models.Model):
	user_id=models.ForeignKey(user_tb,on_delete=models.CASCADE)
	product_id=models.ForeignKey(product_tb,on_delete=models.CASCADE)
	review=models.CharField(max_length=30,default='')
	date = models.CharField(max_length=30,default='')

class contact_tb(models.Model):
	name=models.CharField(max_length=30,default='')
	# user=models.ForeignKey(user_tb,on_delete=models.CASCADE)
	email=models.CharField(max_length=30,default='')
	number=models.CharField(max_length=100,default='')
	subject=models.CharField(max_length=30,default='')
	message=models.CharField(max_length=50,default='')











	




	

