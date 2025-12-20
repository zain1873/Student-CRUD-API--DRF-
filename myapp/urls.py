from django.urls import path
from .views import StudentsView, StudentDetailView

urlpatterns = [
    path('students/', StudentsView, name='Students-View'),
    path('students/<int:pk>/', StudentDetailView, name='Student-detail-view'),
]
