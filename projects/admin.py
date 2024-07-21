from django.contrib import admin

from projects.models import Project
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ProjectAdmin(ImportExportModelAdmin):
    search_fields = ['title','title_ar']
admin.site.register(Project,ProjectAdmin)
