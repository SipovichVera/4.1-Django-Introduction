from rest_framework import serializers 

from itechart_project.companies.models import Employee


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    job_position = serializers.CharField(max_length=100)
    is_manager = serializers.BooleanField()
    is_admin = serializers.BooleanField()
    comp = serializers.ForeignKey()
    phone_number = serializers.PositiveIntegerField()
    personal_data = serializers.OneToOneField()

    def create(self, validated_data):
        return Employee(**validated_data)


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, unique=True)
    web_site = serializers.URLField(max_length=200)
    email = serializers.EmailField(max_length=100, null=True)
    post_index = serializers.PositiveIntegerField()
    logo = serializers.ImageField(upload_to="photos/%Y/%m/%d/")
    bank = serializers.ManyToManyField('Bank')