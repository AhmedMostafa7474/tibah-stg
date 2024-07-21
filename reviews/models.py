from django.db import models

# Create your models here.
class Review(models.Model):
    course_key = models.CharField(max_length=200,null=True,blank=True)
    course_name = models.CharField(max_length=200,null=True,blank=True)
    username  = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='user-image')
    title = models.CharField(max_length=300,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    rate = models.DecimalField(max_digits=4, decimal_places=2,null=True,blank=True)
    def __str__(self):
        return self.username + " " + self.course_key