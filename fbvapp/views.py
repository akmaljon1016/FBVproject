from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course, CourseSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def courseListView(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        courseSerializer = CourseSerializer(courses, many=True)
        return Response(courseSerializer.data)
    elif request.method == 'POST':
        courseSerializer = CourseSerializer(data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        return Response(courseSerializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def courseDetailView(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        return Response(course)
    elif request.method == 'PUT':
        courseSerializer = CourseSerializer(course, data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)

        return Response(courseSerializer.errors)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
