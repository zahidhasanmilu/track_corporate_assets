from rest_framework import serializers
from assetapp.models import Company, Employee, Assets, AssetLog


# The CompanySerializer class is a Django REST framework serializer for the Company model with all
# fields included.
class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


# The `EmployeeSerializer` class is a Django REST framework serializer for the `Employee` model with
# all fields included.
class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


# The `AssetsSerializer` class is a Django REST framework serializer for the `Assets` model with all
# fields included.
class AssetsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assets
        fields = '__all__'


# The `AssetLogSerializer` class is a Django REST framework serializer for the `AssetLog` model with
# all fields included.
class AssetLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetLog
        fields = '__all__'
