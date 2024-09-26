import json
import math
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics
from django.db.models import Avg
from django.db.models import Count, Q

from reviews.models import Review,ContactUS
from reviews.serializers import ContactUsSerializer, ReviewSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser

@method_decorator(csrf_exempt, name='dispatch')
class AllReviewsView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    def get(self, request, *args, **kwargs):
        try:
            course_reviews = (
                Review.objects.values('course_key')
                .annotate(average_rate=Avg('rate'))
                .order_by('course_key')
            )

            response_data = [
                {
                    'courseid': review['course_key'],
                    'average_rate': review['average_rate'],
                }
                for review in course_reviews
            ]

            return JsonResponse(response_data,status=200,safe=False)
    
        except Review.DoesNotExist: 
            return JsonResponse({'error': 'Reviews not found.'}, status=404)
        
@method_decorator(csrf_exempt, name='dispatch')
class ReviewView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    def get(self, request, id, *args, **kwargs):
        try:
            courseid = id
            if not courseid:
                return JsonResponse({'error': 'courseid is missing'}, status=400)
            reviews = Review.objects.filter(course_key=courseid).order_by('id')
            total_count = reviews.count()
            num_pages = math.ceil(int(total_count) / int(10))
            paginator = PageNumberPagination()
            paginator.page_size = 10
            result_page = paginator.paginate_queryset(reviews, request)
            serializer = ReviewSerializer(result_page,many=True)
            paginated_response = paginator.get_paginated_response(serializer.data)
            paginated_response.data['num_pages'] = num_pages
            average_rate = reviews.aggregate(Avg('rate'))['rate__avg']
            review_counts = reviews.aggregate(
                _1=Count('rate', filter=Q(rate=1)),
                _2=Count('rate', filter=Q(rate=2)),
                _3=Count('rate', filter=Q(rate=3)),
                _4=Count('rate', filter=Q(rate=4)),
                _5=Count('rate', filter=Q(rate=5))
            )
            paginated_response.data['average_rate'] = average_rate
            paginated_response.data['review_counts'] = review_counts

            return paginated_response
    
        except Review.DoesNotExist:
            return JsonResponse({'error': 'Reviews not found.'}, status=404)
    def post(self, request):
        
        data = request.data.copy()
        files = request.FILES
        data.update(files)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    def patch(self, request):
        try:
            Reviewid = request.GET.get('id')
            review = Review.objects.get(id=Reviewid)
        except Review.DoesNotExist:
            return JsonResponse({'error': 'Review not found.'}, status=404)

        data = request.data.copy()
        files = request.FILES
        data.update(files)
        serializer = ReviewSerializer(review, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    def delete(self, request):
        try:
            Reviewid = request.GET.get('id')
            review = Review.objects.get(id=Reviewid)
        except Review.DoesNotExist:
            return JsonResponse({'error': 'Review not found.'}, status=404)

        review.delete()
        return JsonResponse({'message': 'Review deleted successfully!'}, status=200)
    
class ContactUSView(generics.ListCreateAPIView):
    serializer_class = ContactUsSerializer
    queryset = ContactUS.objects.all()