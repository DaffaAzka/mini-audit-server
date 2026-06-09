from django.db import models
from django.contrib.auth.models import User
from audit_periods.models import AuditPeriod
from django.core.validators import MinValueValidator

# Create your models here.
class AuditTeam(models.Model): 
    class UserRole(models.IntegerChoices):
        SPV = 1, "Supervisor"
        LEADER = 2, "Leader"
        MEMBER = 3, "Member"
        
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams')
    role = models.IntegerField(choices=UserRole.choices, default=UserRole.MEMBER)
    mandays = models.IntegerField(default=1, validators=[MinValueValidator(1)])    
    audit_period = models.ForeignKey(AuditPeriod, on_delete=models.CASCADE, related_name='teams')
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()} ({self.audit_period})"    