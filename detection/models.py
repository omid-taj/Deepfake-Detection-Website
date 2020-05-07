from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class File(models.Model):
    url = models.CharField('url', max_length=200)
    result = models.CharField('res_url', max_length=200, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    name = models.CharField('name', max_length=200, blank=True, null=True)