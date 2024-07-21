from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=300,null=True,blank=True)
    bio  = models.TextField(null=True,blank=True)
    achievements = models.TextField(null=True,blank=True)
    projectpartner = models.CharField(max_length=300,null=True,blank=True)
    applicants_num = models.IntegerField(null=True,blank=True)
    project_image = models.ImageField(null=True,blank=True,upload_to='projects-image')
    title_ar = models.CharField(max_length=300,null=True,blank=True)
    bio_ar  = models.TextField(null=True,blank=True)
    achievements_ar = models.TextField(null=True,blank=True)
    projectpartner_ar = models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.title