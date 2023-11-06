from django.db import models
from datetime import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

from django.db import models




       


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  # Make this model abstract to prevent database table creation

class TechStack(TimeStamp):
    """
    a model for technology stacks that i have used before
    """
    name = models.CharField(max_length=50)
    image = CloudinaryField('tech')
    description = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    live_url = models.URLField()
    github_url = models.URLField()
    # tech = models.ManyToManyField(TechStack)
    image = CloudinaryField('project')

class Hobby(TimeStamp):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Skill(TimeStamp):
    name = models.CharField(max_length=50)
    proficiency = models.PositiveIntegerField()


class Resume(TimeStamp):
    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    image = CloudinaryField('selfie', folder='resume', blank=True, null=True)
    professional_summary = models.TextField()
    cv_url = models.URLField(blank=True)