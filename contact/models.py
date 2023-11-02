from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)