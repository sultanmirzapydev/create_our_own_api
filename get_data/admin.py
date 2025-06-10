from django.contrib import admin
import csv
from django.http import HttpResponse
# Register your models here.
from .models import DataModel




    

@admin.action(description="select to get csv file")
def export_csv( modeladmin, request, queryset):
        print(type(queryset))
        col_names = [field.name for field in modeladmin.model._meta.fields ][:4]
        res = HttpResponse(content_type = 'text/csv')
        res['content-Disposition'] = 'attachment; filename={}.csv'.format(modeladmin.model._meta)
        writer = csv.writer(res)
        writer.writerow(col_names)
        for item in queryset:
            writer.writerow([getattr(item, field) for field in col_names])

        return res
    
class ApiDataAdmin(admin.ModelAdmin):
    
    actions = [export_csv]

admin.site.register(DataModel, ApiDataAdmin)