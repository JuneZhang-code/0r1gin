from django.db import models

# Create your models here.
class Designerimage(models.Model):
      image = models.ImageField(upload_to='Newsletter/images/')

class Designeraccount(models.Model):
    name= models.CharField(max_length=100)
    collectiondescription = models.TextField()
    email= models.CharField(max_length=100)
    logoimage = models.ImageField(upload_to='Newsletter/images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
