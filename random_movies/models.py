from django.db import models
from django.contrib.auth.models import User
class Movie(models.Model):
    title=models.CharField(max_length=2500)
    url=models.CharField(max_length=2500)
    avail_on=models.CharField(max_length=2500)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.title