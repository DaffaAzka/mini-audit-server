
from django.db import transaction
from comments.services import create_comment

@transaction.atomic
def approve_audit_period(audit_period, comment, user):
    comment = comment.strip()
    if comment != "":
        user_role = user.groups.first().name if user.groups.exists() else "User"

        create_comment(
            user=user, 
            role=user_role, 
            context='audit_period', 
            context_id=audit_period.id, 
            content=comment
        )
        
        audit_period.status = 1
        audit_period.save()
        return audit_period
    else:
        raise ValueError("Comment cannot be empty when approving an audit period.")
