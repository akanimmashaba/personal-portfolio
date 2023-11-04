from django.db import models
from datetime import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True  # Make this model abstract to prevent database table creation

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(TimeStamp, self).save(*args, **kwargs)

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
    project_url = models.URLField()
    tech = models.ManyToManyField(TechStack)
    image = CloudinaryField('project')

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    graduation_year = models.PositiveIntegerField()

class Hobby(TimeStamp):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Skill(TimeStamp):
    name = models.CharField(max_length=50)
    proficiency = models.PositiveIntegerField()

class Resume(TimeStamp):
    pass
    # first_name 
    # last_name
    # preferd_name
    # professional_summary
    