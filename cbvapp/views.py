from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee, EmployeeSerializer
from django.http import Http404


# Create your views here.
class EmployeeListView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request):
        employeeSerializer = EmployeeSerializer(data=request.data)
        if employeeSerializer.is_valid():
            employeeSerializer.save()
            return Response(employeeSerializer.data)
        return Response(employeeSerializer.errors)


class EmployeeDetailView(APIView):

    def get_course(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_course(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_course(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_course(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
