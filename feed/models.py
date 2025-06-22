from django.contrib.auth.backends import get_user_model
from django.db import models
from carrels.models import SharedContent


User = get_user_model()


class FeedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(SharedContent, on_delete=models.CASCADE)
    recommended_score = models.FloatField(default=0.0)  # optional ML scoring
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
