from django.urls import include, path
from rest_framework.routers import DefaultRouter
from gamification.views import UserStreakViewSet, UserBadgeViewSet

router = DefaultRouter()
router.register(r'streaks', UserStreakViewSet, basename='streak')
router.register(r'badges', UserBadgeViewSet, basename='badge')

urlpatterns = [
    path('api/', include(router.urls)),
]
