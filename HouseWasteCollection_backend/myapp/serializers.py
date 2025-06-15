from rest_framework import serializers
from .models import *



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
class CollectionScheduleSerializer(serializers.ModelSerializer):
    
    customer = serializers.SlugRelatedField(
        queryset = Customer.objects.all(),
        slug_field = 'email'
    )
    class Meta:
        model = CollectionSchedule
        fields = '__all__'
        
        
        
class ExtraPickupRequestSerializer(serializers.ModelSerializer):
    
    customer = serializers.SlugRelatedField(
        queryset = Customer.objects.all(),
        slug_field = 'email'
    )
    class Meta:
        model = ExtraPickupRequest
        fields = '__all__'



class PaymentSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(
        queryset = Customer.objects.all(),
        slug_field = 'email'
    )
    class Meta:
        model = Payment
        fields = '__all__'




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'




class EmployeeAssignmentSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(
        queryset = Customer.objects.all(),
        slug_field = 'email'
    )
    
    employee = serializers.SlugRelatedField(
        queryset = Employee.objects.all(),
        slug_field = 'email'
    )
    class Meta:
        model = EmployeeAssignment
        fields = '__all__'

