from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg

from core.models import Employee
from core.serializers import EmployeeSerializer

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=['get'])
    def average_salary(self, request):
        avg_salary = Employee.objects.aggregate(avg=Avg('salary'))
        return Response({"average_salary": avg_salary['avg']})
