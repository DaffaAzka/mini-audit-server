
from .models import Comment

def create_comment(user, role, context, context_id, content):
    comment = Comment.objects.create(
        user=user,
        role=role,
        context=context,
        context_id=context_id,
        content=content
    )
    return comment

def get_comments_by_context(context, context_id):
    return Comment.objects.filter(context=context, context_id=context_id).order_by('-created_at')