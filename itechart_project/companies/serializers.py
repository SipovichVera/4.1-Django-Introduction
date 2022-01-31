from email.policy import default
from msilib.schema import AppId
from re import A
from django.forms import IntegerField
from rest_framework import serializers

from .models import *


class CompanySerializer(serializers.ModelSerializer):
    # logo = serializers.ImageField(required=True)

    # employee = EmployeeSerializer(many=True)
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
    comp = serializers.PrimaryKeyRelatedField(queryset=Company.objects.values('pk'))

    class Meta:
        model = Employee
        fields = ['name', 'surname', 'job_position', 
                  'is_manager', 'is_admin', 'phone_number', 
                  'comp', 'time_create', 'time_update']
                #   'date_of_birth', 'home_address', 'salary']

    def create(self, validated_data):
        # comp = Company.objects.filter(pk=validated_data['comp'])  
        employee = Employee.objects.create(**validated_data)
        # employee.comp.add(comp)
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
    