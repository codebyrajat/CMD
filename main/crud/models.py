from django.db import models

class Employee(models.Model):
    client_id = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=10)
    received_date = models.DateField()
    inventory_received = models.CharField(max_length=100)
    reported_issues = models.TextField()
    client_notes = models.TextField()
    assigned_technician = models.CharField(max_length=100)
    estimated_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.client_name
    