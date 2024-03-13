from django.urls import path
from assetapp.views import CompanyListCreateView
urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='companies'),

    


]
