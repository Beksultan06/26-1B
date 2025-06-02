from rest_framework.routers import DefaultRouter

from apps.settings.views import BaseAPI

router = DefaultRouter()
router.register(r'base', BaseAPI, basename='base')

urlpatterns = [
    
]

urlpatterns += router.urls