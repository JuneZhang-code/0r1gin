from django.db import models


class Homeimage(models.Model):
      image = models.ImageField(upload_to='Newsletter/images/')
