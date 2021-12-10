from django.db import models

# Create your models here.
class Ambassadorimage(models.Model):
      image = models.ImageField(upload_to='Newsletter/images/')
