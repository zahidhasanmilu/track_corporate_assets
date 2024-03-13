from django.urls import path
from assetapp.views import CompanyListCreateView, EmployeeListCreateView, EmployeeDetails,AssetsList,Assets_Details


urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='companies'),

    # These lines of code are defining employee URL patterns for the Django application.
    path('employee/', EmployeeListCreateView.as_view(), name='employee'),
    path('employee/<int:pk>/', EmployeeDetails.as_view(), name='employee_details'),
    
   # These lines of code are defining asset URL patterns for the Django application.
    path('asset/', AssetsList.as_view(), name='assets'),
    path('asset/<int:pk>/', Assets_Details.as_view(), name='asset_details'),
    
    

]
