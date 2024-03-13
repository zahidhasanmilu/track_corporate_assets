from django.contrib import admin
from assetapp.models import Company, Employee, Assets, AssetLog


# The class CompanyAdmin defines a Django admin model with a list display setting for the 'name'
# field.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']


# This Python class defines an EmployeeAdmin model with specified fields for display in the admin
# interface.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['company', 'name', 'department']


# The class `AssetsAdmin` defines a Django admin model with specified fields for displaying asset
# information.
class AssetsAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'brand', 'current_condition',
                    'manufacturer', 'serial_number', 'issued', 'purchased_date']


# The `AssetLogAdmin` class defines the display fields for the Asset Log admin panel.
class AssetLogAdmin(admin.ModelAdmin):
    list_display = ['asset', 'employee', 'checkout_date',
                    'return_date', 'checkout_condition']


# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Assets, AssetsAdmin)
admin.site.register(AssetLog, AssetLogAdmin)
