from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSets
from . import views

router = DefaultRouter()
router.register('products', ProductViewSets, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.home, name='home'),

]
