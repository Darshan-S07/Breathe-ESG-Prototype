from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DataSource(models.Model):
    SOURCE_TYPES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    INGESTION_METHODS = [
        ('FILE', 'FILE'),
        ('API', 'API'),
    ]

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES)
    ingestion_method = models.CharField(max_length=20, choices=INGESTION_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)

class RawRecord(models.Model):
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    raw_payload = models.JSONField()
    
    status = models.CharField(
        max_length=20,
        choices=[('PARSED', 'PARSED'), ('FAILED', 'FAILED')],
        default='PARSED'
    )

    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class NormalizedRecord(models.Model):
    SCOPE_CHOICES = [
        ('SCOPE1', 'Scope 1'),
        ('SCOPE2', 'Scope 2'),
        ('SCOPE3', 'Scope 3'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]

    raw_record = models.ForeignKey(RawRecord, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    category = models.CharField(max_length=20, choices=SCOPE_CHOICES)
    activity_type = models.CharField(max_length=50)

    quantity = models.FloatField()

    unit = models.CharField(max_length=20)

    normalized_quantity = models.FloatField()

    normalized_unit = models.CharField(max_length=20)

    emission_factor = models.FloatField()

    emissions_value = models.FloatField()

    suspicious_flag = models.BooleanField(default=False)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)

class AuditLog(models.Model):
    record = models.ForeignKey(NormalizedRecord, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)

    old_value = models.JSONField(null=True, blank=True)
    new_value = models.JSONField(null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)

