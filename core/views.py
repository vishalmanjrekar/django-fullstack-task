import random

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


from core.models import Employee, Department, Attendance, Performance
from core.serializers import EmployeeSerializer
from .serializers import DepartmentSerializer, AttendanceSerializer, PerformanceSerializer

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department', 'designation']  # filter by exact match
    search_fields = ['name', 'email']  # search by keyword
    ordering_fields = ['salary', 'join_date']  # order by these fields

    @action(detail=False, methods=['get'])
    def average_salary(self, request):
        avg_salary = Employee.objects.aggregate(avg=Avg('salary'))
        return Response({"average_salary": avg_salary['avg']})


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['location']
    search_fields = ['name']


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'date', 'status']
    search_fields = ['status']


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'review_date']
    search_fields = ['comments']
    ordering_fields = ['rating', 'review_date']


class EmployeePerformanceSummary(APIView):
    """
    Returns performance summary data for employees to be visualized in a chart.
    """
    permission_classes = [AllowAny]
    def get(self, request):
        performances = Performance.objects.all()
        performance_data = {
            'labels': [f"{performance.employee.name}" for performance in performances],
            'performance_scores': [performance.rating for performance in performances]  # For demo purposes
        }
        return Response(performance_data)


class EmployeePerformanceSummaryChart(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'charts/performance_chart.html')