from rest_framework import viewsets, permissions
from gamification.models import UserStreak, UserBadge
from gamification.serializers import UserStreakSerializer, UserBadgeSerializer


class UserStreakViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserStreak.objects.all()
    serializer_class = UserStreakSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class UserBadgeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserBadge.objects.all()
    serializer_class = UserBadgeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
