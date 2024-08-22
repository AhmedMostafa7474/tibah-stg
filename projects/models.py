import math
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=300)
    bio  = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    projectpartner = models.CharField(max_length=300,blank=True)
    applicants_num = models.IntegerField(blank=True)
    project_image = models.ImageField(upload_to='projects-image')
    title_ar = models.CharField(max_length=300,blank=True)
    bio_ar  = models.TextField(blank=True)
    achievements_ar = models.TextField(blank=True)
    projectpartner_ar = models.CharField(max_length=300,blank=True)
    def __str__(self):
        return self.title

# @receiver([post_save, post_delete], sender=Project)
# def clear_Project_cache(sender, **kwargs):
#     print("Cache Deletion Triggered")

#     try:
#         total_count = Project.objects.count()
#         num_pages = math.ceil(total_count / 10)

#         for page in range(1, num_pages + 1):
#             cache_key = f'lionel_{page}'
#             print(f"Checking cache key: {cache_key} - Value: {cache.get(cache_key)}")
#             cache.delete(cache_key)
#             print(f"Deleted cache key: {cache_key} - Value after deletion: {cache.get(cache_key)}")

#     except Exception as e:
#         print(f"Error clearing cache: {str(e)}")
