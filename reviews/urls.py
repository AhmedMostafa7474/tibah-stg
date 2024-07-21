from django.urls import path
from . import views

urlpatterns = [
        path('<str:id>/',views.ReviewView.as_view(), name='reviews'),
        path('',views.ReviewView.as_view(), name='reviews'),

]