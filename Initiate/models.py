from django.db import models

# Create your models here.

class Initiate(models.Model):
    name= models.CharField(max_length=100)
    projectdescription = models.TextField()
    logoimage = models.ImageField(upload_to='Newsletter/images/')
    productimage = models.ImageField(upload_to='Newsletter/images/')
    profilelink = models.CharField(max_length=100)
    story = models.TextField()
    goal = models.CharField(max_length=100)
    productdescription = models.TextField()
    biddingprice= models.CharField(max_length=100)
    productquantity= models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ShippingAddress(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phonenumber= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    zipcode= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    data_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
