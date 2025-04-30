from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Anytime you update this we need to do a "Migration", use 'python manage.py makemigrations' -> 'python manage.py migrate'
class InsertItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Item(models.Model):
    listEntry = models.ForeignKey(InsertItem, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    textEntry = models.CharField(max_length=500)

    def __str__(self):
        return self.text