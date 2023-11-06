from django.contrib import admin
from .models import Project, Skill, Resume,Hobby

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Hobby)
admin.site.register(Resume)
# Register your models here.