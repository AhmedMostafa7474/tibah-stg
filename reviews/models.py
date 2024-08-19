from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
    course_key = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    username  = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True,upload_to='user-image')
    title = models.CharField(max_length=300,null=True,blank=True)
    message = models.TextField()
    rate = models.DecimalField(max_digits=4, decimal_places=2, validators=[
            MinValueValidator(1.00),
            MaxValueValidator(5.00)
        ])
    def __str__(self):
        return self.username + " " + self.course_key