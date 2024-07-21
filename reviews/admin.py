from django.contrib import admin

from reviews.models import Review
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ReviewAdmin(ImportExportModelAdmin):
    search_fields = ['course_key','course_name','username']
    list_filter = ('course_key','course_name','rate')
    list_display = ('course_key', 'course_name','username','message','rate')
    
admin.site.register(Review,ReviewAdmin)
