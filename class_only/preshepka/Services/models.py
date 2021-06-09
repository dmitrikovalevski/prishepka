from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    picture = models.ImageField(upload_to='service', null=True, blank=True)
    title = models.CharField(max_length=200,)
    descriptions = models.TextField()
    price = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

