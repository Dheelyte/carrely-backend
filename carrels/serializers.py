from rest_framework import serializers
from carrels.models import SharedContent, ContentComment, ContentUpvote
from carrels.models import ContentUpvote
from user.serializers import UserSerializer


class ContentCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ContentComment
        fields = ('id', 'user', 'comment', 'created_at')
        read_only_fields = ('id', 'user', 'created_at')


class SharedContentSerializer(serializers.ModelSerializer):
    poster = UserSerializer(read_only=True)
    comments = ContentCommentSerializer(many=True, read_only=True)
    view_count = serializers.IntegerField(read_only=True)

    upvotes_count = serializers.SerializerMethodField()
    is_upvoted_by_me = serializers.SerializerMethodField()

    class Meta:
        model = SharedContent
        fields = (
            'id',
            'carrel',
            'poster',
            'title',
            'description',
            'file',
            'link',
            'content_type',
            'posted_at',
            'view_count',
            'comments',
            'upvotes_count',
            'is_upvoted_by_me',
        )
        read_only_fields = ('poster', 'posted_at', 'view_count')

    def get_upvotes_count(self, obj):
        return obj.upvotes.count()

    def get_is_upvoted_by_me(self, obj):
        user = self.context.get('request').user
        if user and user.is_authenticated:
            return obj.upvotes.filter(user=user).exists()
        return False



class SharedContentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SharedContent
        fields = (
            'carrel',
            'title',
            'description',
            'file',
            'link',
            'content_type',
        )


class ContentUpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentUpvote
        fields = ('id', 'created_at')
        read_only_fields = ('id', 'created_at')
