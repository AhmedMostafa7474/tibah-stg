import json
import math
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics
# from django.core.cache import cache

from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
# from django.views.decorators.cache import cache_page    
# Create your views here.

# def get_cache_key(request):
#     page = request.GET.get('page', '1')
#     print("YEEEEEEEE")
#     print(f'lionel_{page}')
#     return f'lionel_{page}'

class ProjectView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer

    # @method_decorator(
    #     cache_page(
    #         timeout=None,
    #         cache="default",
    #         key_prefix=get_cache_key(request=)
    #     )
    # )
    def get(self, request, *args, **kwargs):
        try:
            # cache_key = get_cache_key(request)
            # cached_data = cache.get(cache_key)

            # if cached_data:
            #     print(f"Cache hit for key: {cache_key}")
            #     return JsonResponse(cached_data, safe=False)
            Projects = Project.objects.all().order_by('id')
            total_count = Projects.count()
            num_pages = math.ceil(total_count / 10)  # Assuming page_size is 10
            paginator = PageNumberPagination()
            paginator.page_size = 10
            result_page = paginator.paginate_queryset(Projects, request)
            serializer = ProjectSerializer(result_page, many=True)
            paginated_response = paginator.get_paginated_response(serializer.data)
            paginated_response.data['num_pages'] = num_pages
            # cache.set(cache_key, paginated_response.data, timeout=None)  # Cache for 15 minutes

            return paginated_response
    
        except Project.DoesNotExist:
            return JsonResponse({'error': 'Projects not found.'}, status=404)
    
@method_decorator(csrf_exempt, name='dispatch')
class SingleProjectView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    def get(self, request):
        try:
            projectid = request.GET.get('id')   
            if not projectid:
                return JsonResponse({'error': 'Project ID is missing'}, status=400)
            project = Project.objects.get(id=projectid)
            serializer = ProjectSerializer(project)
        
            return JsonResponse(serializer.data, safe=False)
    
        except Project.DoesNotExist:
            return JsonResponse({'error': 'Project not found.'}, status=404)
    def post(self, request):
        
        data = request.data.copy()
        files = request.FILES
        data.update(files)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    def patch(self, request):
        try:
            projectid = request.GET.get('id')
            project = Project.objects.get(id=projectid)
        except Project.DoesNotExist:
            return JsonResponse({'error': 'Project not found.'}, status=404)

        data = request.data.copy()
        files = request.FILES
        data.update(files)
        serializer = ProjectSerializer(project, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    def delete(self, request):
        try:
            projectid = request.GET.get('id')
            project = Project.objects.get(id=projectid)
        except Project.DoesNotExist:
            return JsonResponse({'error': 'Project not found.'}, status=404)

        project.delete()
        return JsonResponse({'message': 'Project deleted successfully!'}, status=200)