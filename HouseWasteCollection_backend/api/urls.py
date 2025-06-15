from django.urls import path
from myapp import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('customers/', views.manage_customers),
    path('customers/<int:id>', views.manage_customers),
    
    path('collectionSchedules/', views.manage_collectionSchedule),
    path('collectionSchedules/<int:id>', views.manage_collectionSchedule),
    
    path('extraPickupRequests/', views.manage_extraPickupRequest),
    path('extraPickupRequests/<int:id>', views.manage_extraPickupRequest),
    
    path('payments/', views.manage_payment),
    path('payments/<int:id>', views.manage_payment),
    
    path('employees/', views.manage_employee),
    path('employees/<int:id>', views.manage_employee),
    
    path('employeeAssignment/', views.manage_employeeAssignment),
    path('employeeAssignment/<int:id>', views.manage_employeeAssignment),
    
]
