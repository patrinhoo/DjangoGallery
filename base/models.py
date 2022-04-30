from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.title
        