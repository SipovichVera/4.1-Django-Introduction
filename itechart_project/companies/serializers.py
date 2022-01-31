from rest_framework import serializers

from .models import Company, Bank, Employee, PersonalData 


class CompanySerializer(serializers.ModelSerializer):

    bank = serializers.IntegerField(read_only=True, source='bank_id')

    class Meta:
        model = Company
        fields = ['name', 'web_site', 'email', 'post_index', 'bank',
                  'time_create', 'time_update']

    def create(self, validated_data):
        company = Company.objects.create(**validated_data)
        return company


class EmployeeSerializer(serializers.ModelSerializer):

    # serialize one to one relationship
    comp = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.values('pk')
        )

    class Meta:
        model = Employee
        fields = ['name', 'surname', 'job_position', 
                  'is_manager', 'is_admin', 'phone_number', 
                  'comp', 'time_create', 'time_update']

    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        return employee


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ['name', 'web_site', 'email', 'time_create', 'time_update']

    def create(self, validated_data):
        return Bank.objects.create(**validated_data)


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
    