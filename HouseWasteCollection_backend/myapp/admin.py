from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Customer)
admin.site.register(CollectionSchedule)
admin.site.register(ExtraPickupRequest)
admin.site.register(Payment)
admin.site.register(Employee)
admin.site.register(EmployeeAssignment)
