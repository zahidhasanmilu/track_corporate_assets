from django.urls import path
from assetapp.views import CompanyListCreateView, EmployeeListCreateView, EmployeeDetails


urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='companies'),

    # These lines of code are defining URL patterns for the Django application.
    path('employee/', EmployeeListCreateView.as_view(), name='employee'),
    path('employee/<int:pk>/', EmployeeDetails.as_view(), name='employee_details'),

]
