from django.urls import path

from rest_framework.routers import DefaultRouter
from apps.users.views import USerViewSet

router = DefaultRouter()
router.register(r'users', USerViewSet, basename='users')

urlpatterns = [
    
]

urlpatterns += router.urls