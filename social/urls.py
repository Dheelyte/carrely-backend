from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FollowViewSet

router = DefaultRouter()
router.register(r'follows', FollowViewSet, basename='follow')

urlpatterns = [
    path('api/', include(router.urls)),
]
