from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='portfolio')
    detailphoto1 = models.ImageField(upload_to='detail')
    detailphoto2 = models.ImageField(upload_to='detail')
    detailphoto3 = models.ImageField(upload_to='detail')
    slug = AutoSlugField(populate_from='name')
    def __str__(self):
        return self.name