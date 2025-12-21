from django.urls import path
from .views import Employees

urlpatterns = [
    path("employees/", Employees.as_view(), name="employee")
]
