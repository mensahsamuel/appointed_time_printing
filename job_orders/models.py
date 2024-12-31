from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class JobOrder(models.Model):
    job_order_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    department = models.CharField(max_length=50, choices=[
        ('Screen Printing', 'Screen Printing'),
        ('Embroidery', 'Embroidery'),
        ('Large Format', 'Large Format'),
    ])
    description = models.TextField()
    customer_material = models.BooleanField(default=False)
    company_material = models.BooleanField(default=False)
    quantity = models.IntegerField()
    date_of_collection = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    receipt_number = models.CharField(max_length=50)

    STATUS_CHOICES = [
        ('PENDING_MD', 'Pending MD Approval'),
        ('PENDING_FM', 'Pending FM Approval'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('IN_PRODUCTION', 'In Production'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING_MD')
    md_approved_at = models.DateTimeField(null=True, blank=True)
    md_approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='md_approved_job_orders')
    fm_approved_at = models.DateTimeField(null=True, blank=True)
    fm_approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='fm_approved_job_orders')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_job_orders')

    def __str__(self):
        return self.job_order_number