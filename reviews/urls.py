from django.urls import path
from . import views

urlpatterns = [
        path('review/<str:id>/',views.ReviewView.as_view(), name='reviews'),
        path('postreview/',views.ReviewView.as_view(), name='reviews'),
        path('all/',views.AllReviewsView.as_view(), name='reviews'),
        path('contactus/',views.ContactUSView.as_view(), name='ContactUSView'),
]