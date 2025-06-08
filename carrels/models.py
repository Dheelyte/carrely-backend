from django.db import models
from user.models import User

class Carrel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.JSONField(default=list)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='carrels/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CarrelMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carrel = models.ForeignKey(Carrel, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('member', 'Member')], default='member')

    class Meta:
        unique_together = ('user', 'carrel')


class SharedContent(models.Model):
    carrel = models.ForeignKey(Carrel, on_delete=models.CASCADE, related_name='contents')
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/', null=True, blank=True)
    link = models.URLField(blank=True)
    content_type = models.CharField(max_length=50, choices=[
        ('pdf', 'PDF'), ('video', 'Video'), ('course', 'Course')
    ])
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContentComment(models.Model):
    content = models.ForeignKey(SharedContent, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class ContentUpvote(models.Model):
    content = models.ForeignKey(SharedContent, on_delete=models.CASCADE, related_name='upvotes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('content', 'user')  # prevent multiple upvotes by same user
