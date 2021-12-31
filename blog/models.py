from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse

#Each class is a table in the database
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() #unrestricted length
    date_posted = models.DateTimeField(default=timezone.now) #No parenthesis, pass in actual function as default value
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If a user is deleted, delete their post as well

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

