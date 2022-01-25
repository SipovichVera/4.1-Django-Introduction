from rest_framework import serializers

from .models import *


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    # serialize one to one relationship
    # date_of_birth = serializers.DateField(source='personal_data_id.date_of_birth')
    # home_address = serializers.CharField(source='personal_data_id.home_address')
    # salary = serializers.IntegerField(source='personal_data_id.salary')

    class Meta:
        model = Employee
        fields = ['name', 'surname', 'job_position', 
                  'is_manager', 'is_admin', 'phone_number', 
                  'time_create', 'time_update']
                #   'date_of_birth', 'home_address', 'salary']

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['name', 'web_site', 'email', 'time_create', 'time_update']

    def create(self, validated_data):
        return Bank.objects.create(**validated_data)


class CompanySerializer(serializers.ModelSerializer):
    # logo = serializers.ImageField(required=True)

    # employee_id = EmployeeSerializer(many=True)
    employee_id = serializers.CharField(source='employee_id.employee_id')
    bank = BankSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = ['name', 'web_site', 'email', 'post_index', 'bank',
                  'employee_id', 'time_create', 'time_update']

    def create(self, validated_data):
        return Company.objects.create(**validated_data)


class PersonalDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalData
        fields = ['date_of_birth', 'home_address', 'salary', 
                  'time_create', 'time_update']

    def create(self, validated_data):
        return PersonalData.objects.create(**validated_data)


class EmployeeWithPersonalData(EmployeeSerializer):

    class Meta:
        model = PersonalData
        fields = ['date_of_birth', 'home_address', 'salary', 
                  'time_create', 'time_update']

    def create(self, validated_data):
        return PersonalData.objects.create(**validated_data)
    