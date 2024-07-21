from django.urls import path
from . import views

urlpatterns = [
    
    path('all/',views.ProjectView.as_view(), name='all'),
    path('',views.SingleProjectView.as_view(), name='single-project'),
]