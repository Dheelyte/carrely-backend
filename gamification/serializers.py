from rest_framework import serializers
from gamification.models import UserStreak, Badge, UserBadge


class UserStreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStreak
        fields = ['id', 'user', 'start_date', 'end_date', 'length', 'is_active']
        read_only_fields = ['user', 'start_date', 'end_date', 'length', 'is_active']


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['id', 'name', 'description', 'icon']


class UserBadgeSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(read_only=True)

    class Meta:
        model = UserBadge
        fields = ['id', 'user', 'badge',]
        read_only_fields = ['user', 'badge',]
