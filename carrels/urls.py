from django.urls import path, include
from rest_framework.routers import DefaultRouter
from carrels.views import CarrelViewSet, SharedContentViewSet, ContentCommentViewSet, ContentUpvoteViewSet


router = DefaultRouter()
router.register(r'carrels', CarrelViewSet, basename='carrel')
router.register(r'shared-content', SharedContentViewSet, basename='shared-content')
router.register(r'comments', ContentCommentViewSet, basename='content-comment')


# Custom upvote viewset using ViewSet instead of ModelViewSet
# If you prefer using actions, switch to a custom ViewSet+@action approach
upvote_list = ContentUpvoteViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
upvote_detail = ContentUpvoteViewSet.as_view({
    'delete': 'destroy',
})

urlpatterns = [
    path('', include(router.urls)),
    path('upvotes/', upvote_list, name='upvote-list'),
    path('upvotes/<int:pk>/', upvote_detail, name='upvote-detail'),
]
