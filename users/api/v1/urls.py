from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HygfhgfjViewSet

router = DefaultRouter()
router.register("hygfhgfj", HygfhgfjViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
