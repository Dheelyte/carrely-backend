from rest_framework import serializers
from feed.models import FeedItem
from carrels.serializers import SharedContentSerializer


class FeedItemSerializer(serializers.ModelSerializer):
    content = SharedContentSerializer(read_only=True)

    class Meta:
        model = FeedItem
        fields = ['id', 'user', 'content', 'created_at']
        read_only_fields = ['user', 'content', 'created_at']
