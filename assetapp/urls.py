from django.urls import path
from assetapp.views import CompanyListCreateView,EmployeeListCreateView
urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='companies'),
    
    path('employee/', EmployeeListCreateView.as_view(), name='employee'),
    
]
