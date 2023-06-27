from django.contrib import admin
from .models import Car, Driver, InsuranceEvent, ImagesInsuranceEvent


# Register your models here.
class InsuranceEventInline(admin.TabularInline):
    model = InsuranceEvent
    extra = 0


class ImagesInsuranceEventInline(admin.TabularInline):
    model = ImagesInsuranceEvent
    extra = 0


class ImagesInsuranceEventAdmin(admin.ModelAdmin):
    list_display = ['insurance_event']
    list_filter = ['insurance_event']
    search_fields = ['insurance_event']


class InsuranceEventAdmin(admin.ModelAdmin):
    list_display = ['car', 'driver']
    inlines = [ImagesInsuranceEventInline]
    list_filter = ['car', 'driver']
    search_fields = ['car', 'driver']


class DriverAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'name', 'middle_name']
    inlines = [InsuranceEventInline]
    list_filter = ['last_name', 'name']
    search_fields = ['last_name', 'name']


class CarAdmin(admin.ModelAdmin):
    list_display = ['number']
    inlines = [InsuranceEventInline]
    list_filter = ['number']
    search_fields = ['number']


admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(InsuranceEvent, InsuranceEventAdmin)
admin.site.register(ImagesInsuranceEvent, ImagesInsuranceEventAdmin)
