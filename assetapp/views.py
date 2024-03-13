from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from assetapp.models import Company, Employee, Assets, AssetLog
from assetapp.serializers import CompanySerializer, EmployeeSerializer, AssetsSerializer, AssetLogSerializer

from django.db import IntegrityError


class CompanyListCreateView(APIView):
    def get(self, request):
        student = Company.objects.all()
        serializer = CompanySerializer(student, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'data': serializer.errors})


# This class is a view in Django REST framework that handles listing and creating Employee objects.
class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# The class `EmployeeDetails` is a Django REST framework view that allows retrieving, updating, and
# deleting instances of the `Employee` model using the `EmployeeSerializer`.
class EmployeeDetails(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
