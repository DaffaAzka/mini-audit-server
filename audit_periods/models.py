from django.db import models

# Create your models here.
class AuditPeriod(models.Model):
    name = models.CharField(max_length=255)
    unit = models.ForeignKey('units.Unit', on_delete=models.CASCADE, related_name='audit_periods')
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name