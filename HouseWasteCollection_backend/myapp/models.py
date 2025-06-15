from django.db import models

# Create your models here.

#1
class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    house_no = models.CharField()
    district = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone} - {self.email}"
    
    
#  2   
class CollectionSchedule(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    next_collection = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer.full_name} - {self.day_of_week}"
    
    

# 3    
class ExtraPickupRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Completed', 'Completed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    extra_charge = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Request by {self.customer.full_name} on {self.request_date.date()} - {self.status}"
    
    
    
    
# 4
class Payment(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('Monthly', 'Monthly'),
        ('ExtraPickup', 'ExtraPickup'),
    ]

    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Pending', 'Pending'),
    ]

    # customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='payments')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.customer.full_name} - {self.payment_type} - {self.status} - {self.amount}"




# 5
class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True,)
    phone = models.CharField(max_length=20)
    assigned_area = models.CharField(max_length=100)  # Can be district, route, etc.
    hire_date = models.DateTimeField()

    def __str__(self):
        return f"{self.full_name} - {self.assigned_area}"
    
    
    


# 6
class EmployeeAssignment(models.Model):
    # employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='assignments')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True, related_name='employee_assignments')
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True,)
    zone = models.CharField(max_length=100, blank=True)
    assignment_date = models.DateField()

    def __str__(self):
        target = self.customer.full_name if self.customer else f"Zone: {self.zone}"
        return f"{self.employee.full_name} assigned to {target} on {self.assignment_date}"




