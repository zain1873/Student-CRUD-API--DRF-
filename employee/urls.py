from django.urls import path
from .views import Employees, EmployeeDetail

urlpatterns = [
    path("employees/", Employees.as_view(), name="employee"),
    path("employees/<int:pk>/", EmployeeDetail.as_view(), name="EmployeeDetail")
]
