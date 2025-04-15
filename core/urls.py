from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import EmployeeViewSet, DepartmentViewSet, AttendanceViewSet, PerformanceViewSet

# Swagger Imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# DRF Router
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'performance', PerformanceViewSet, basename='performance')

# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Employee Dashboard API",
        default_version='v1',
        description="API for employee analytics and visualizations",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
