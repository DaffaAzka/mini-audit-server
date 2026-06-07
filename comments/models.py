from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')    
    role = models.CharField(max_length=255)  # This can be used to specify the role of the commenter (e.g., auditor, auditee, etc.)
    context = models.CharField(max_length=255)  # This can be used to specify the table or model the comment is related to
    context_id = models.IntegerField()  # This can be used to specify the context or ID of the related object (e.g., audit period ID, unit ID, etc.)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} at {self.created_at}'