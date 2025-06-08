from rest_framework import viewsets
from feed.models import FeedItem
from feed.serializers import FeedItemSerializer
from rest_framework.permissions import IsAuthenticated


class FeedItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FeedItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FeedItem.objects.filter(user=self.request.user)
