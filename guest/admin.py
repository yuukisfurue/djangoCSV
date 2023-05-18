from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportMixin
from import_export.formats import base_formats
from guest.models import Guest


# Register your models here.
class GuestResource(resources.ModelResource):
    class Meta:
        model = Guest
    fields = ['id','name','prefecture','gender','employmentstatus','company','jyob','stay','affiliation','postion','annual','lastyear']
    import_id_fields = ['id']

class GuestAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'prefecture',
        'gender',
        'employmentstatus',
        'company',
        'jyob',
        'stay',
        'affiliation',                        
        'postion',
        'annual',
        'lastyear'
      )

    resource_class = GuestResource
    formats = [base_formats.CSV]

    list_display = ('id','name','prefecture','gender','employmentstatus','company','jyob','stay','affiliation','postion','annual','lastyear')
    list_per_page = 10 # No of records per page 

admin.site.register(Guest, GuestAdmin)
