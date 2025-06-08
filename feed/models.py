from django.db import models
from user.models import User
from carrels.models import SharedContent

class FeedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(SharedContent, on_delete=models.CASCADE)
    recommended_score = models.FloatField(default=0.0)  # optional ML scoring
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
