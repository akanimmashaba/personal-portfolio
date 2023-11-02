from django.db import models
from resume.models import TimeStamp


# Create your models here.
class BlogPost(TimeStamp):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()