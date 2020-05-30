from django.db import models


# Create your models here.
class Job(models.Model):
    # Image Property
    image = models.ImageField(upload_to='images/')
    # Summary Property
    summary = models.CharField(max_length=200)
