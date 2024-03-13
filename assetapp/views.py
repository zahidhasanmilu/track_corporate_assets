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


# AssetsList With generic Api views
class AssetsList(ListCreateAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer


# AssetsList With APIView
'''
# The `AssetsList` class in Python defines GET and POST methods for retrieving and creating assets
# data using a serializer.

class AssetsList(APIView):
    def get(self, request):
        student = Assets.objects.all()
        serializer = AssetsSerializer(student, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = AssetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'data': serializer.errors})
'''


# Assets_Details With generic Api views
class Assets_Details(RetrieveUpdateDestroyAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer


# Assets_Details With APIView
'''

# The `Assets_Details` class in Python defines methods for retrieving, updating, and deleting asset
# details using Django REST framework.

class Assets_Details(APIView):
    def get_student(self, pk):
        try:
            return Assets.objects.get(pk=pk)

        except Assets.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        single_asset = self.get_student(pk)
        serializer = AssetsSerializer(single_asset)
        return Response({'data': serializer.data})

    def put(self, request, pk):
        single_asset = self.get_student(pk)
        serializer = AssetsSerializer(single_asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            return Response({'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        single_asset = self.get_student(pk)
        single_asset.delete()
        return Response({'data': "student delete successfull"})
'''

class AssetsLogListCreateView(APIView):

    def get(self, request):
        assets = AssetLog.objects.all()
        serializer = AssetLogSerializer(assets, many=True)
        return Response(serializer.data)

    def post(self, request):
        asset_id = request.data.get('asset')
        assets = AssetLog.objects.get(pk=asset_id)
        if assets.issued:
            return Response({"detail": "Assets is already issued"}, status=status.HTTP_400_BAD_REQUEST)

        assets.issued = True
        assets.save()

        serializer = AssetLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssetsLogDetail(RetrieveUpdateDestroyAPIView):
    queryset = AssetLog.objects.all()
    serializer_class = AssetLogSerializer
