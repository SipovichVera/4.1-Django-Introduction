from rest_framework import serializers

from .models import *


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.CharField(max_length=MaxLenght.MAX_EMPLOYEE_NAME_LENGTH)
    # surname = serializers.CharField(max_length=MaxLenght.MAX_EMPLOYEE_SURENAME_LENGTH)
    # job_position = serializers.CharField(max_length=MaxLenght.MAX_EMPLOYEE_JOB_POSITION_LENGTH)
    # is_manager = serializers.BooleanField()
    # is_admin = serializers.BooleanField()
    # phone_number = serializers.PositiveIntegerField(unique=True)
    # comp_id = serializers.ForeignKey()
    # personal_data_id = serializers.OneToOneField()

    # serialize one to one relationship
    date_of_birth = serializers.DateField(source='personal_data_id.date_of_birth')
    home_address = serializers.CharField(source='personal_data_id.home_address')
    salary = serializers.IntegerField(source='personal_data_id.salary')

    class Meta:
        model = Employee
        fields = ['name', 'surname', 'job_position', 
                  'is_manager', 'is_admin', 'phone_number']  # add date_of_birth etc?

    def create(self, validated_data):
        return Employee(**validated_data)


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['name', 'web_site', 'email']

    def create(self, validated_data):
        return Bank(**validated_data)


class CompanySerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=MaxLenght.MAX_COMPANY_NAME_LENGTH, unique=True)
    # web_site = serializers.URLField(max_length=MaxLenght.MAX_COMPANY_WEBSITE_LENGTH)
    # email = serializers.EmailField(max_length=MaxLenght.MAX_COMPANY_EMAIL_LENGTH, null=True)
    # post_index = serializers.PositiveIntegerField()
    # logo = serializers.ImageField(upload_to="photos/%Y/%m/%d/")
    # bank_id = serializers.ManyToManyField('Bank')

    employee = EmployeeSerializer(many=True)
    bank = BankSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = ['name', 'web_site', 'email', 'post_index', 'bank', 'employee']

    def create(self, validated_data):
        return Company(**validated_data)


class PersonalDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalData
        fields = ['date_of_birth', 'home_address', 'salary', ]

    def create(self, validated_data):
        return PersonalData(**validated_data)
