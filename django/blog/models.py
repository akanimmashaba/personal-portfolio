from django.db import models
from resume.models import TimeStamp
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(TimeStamp):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()
    image = CloudinaryField('post')