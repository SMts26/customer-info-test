from django.db import models

# Create your models here.
# Anytime you update this we need to do a "Migration", use 'python manage.py makemigrations' -> 'python manage.py migrate'
class InsertItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
