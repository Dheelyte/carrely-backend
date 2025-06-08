from rest_framework.response import Response
from rest_framework import viewsets, permissions
from carrels.models import SharedContent, ContentComment, ContentUpvote, Carrel
from carrels.serializers import (
    SharedContentSerializer, SharedContentCreateSerializer, ContentCommentSerializer, ContentUpvoteSerializer, CarrelSerializer
)


class CarrelViewSet(viewsets.ModelViewSet):
    queryset = Carrel.objects.all()
    serializer_class = CarrelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class SharedContentViewSet(viewsets.ModelViewSet):
    queryset = SharedContent.objects.select_related('poster', 'carrel').prefetch_related('comments', 'upvotes')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SharedContentCreateSerializer
        return SharedContentSerializer

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class ContentCommentViewSet(viewsets.ModelViewSet):
    queryset = ContentComment.objects.select_related('user', 'content')
    serializer_class = ContentCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContentUpvoteViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        content_id = request.data.get('content')
        if not content_id:
            return Response({'error': 'content is required'}, status=400)

        content = SharedContent.objects.filter(id=content_id).first()
        if not content:
            return Response({'error': 'Content not found'}, status=404)

        upvote, created = ContentUpvote.objects.get_or_create(content=content, user=request.user)
        if created:
            return Response({'message': 'Upvoted'}, status=201)
        return Response({'message': 'Already upvoted'}, status=200)

    def destroy(self, request, pk=None):
        try:
            upvote = ContentUpvote.objects.get(id=pk, user=request.user)
            upvote.delete()
            return Response({'message': 'Upvote removed'}, status=204)
        except ContentUpvote.DoesNotExist:
            return Response({'error': 'Upvote not found'}, status=404)

    def list(self, request):
        user_upvotes = ContentUpvote.objects.filter(user=request.user)
        serializer = ContentUpvoteSerializer(user_upvotes, many=True)
        return Response(serializer.data)
