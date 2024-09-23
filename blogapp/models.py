from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content =  models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('mypost')

    def __str__(self):
        return self.title
