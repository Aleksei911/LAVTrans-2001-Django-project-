from django.contrib import admin
from .models import Car, Driver, InsuranceEvent, ImagesInsuranceEvent, Owner, TechPassport, TechPassportScans, \
    PassportDriver, DriverScans


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


class TechPassportScansAdmin(admin.ModelAdmin):
    list_display = ['techpassport']
    list_filter = ['techpassport']
    search_fields = ['techpassport']


class DriverScansAdmin(admin.ModelAdmin):
    list_display = ['passport']
    list_filter = ['passport']
    search_fields = ['passport']


class InsuranceEventAdmin(admin.ModelAdmin):
    list_display = ['car', 'driver']
    inlines = [ImagesInsuranceEventInline]
    list_filter = ['car', 'driver']
    search_fields = ['car', 'driver']


class TechPassportAdmin(admin.ModelAdmin):
    list_display = ['car']
    list_filter = ['car']
    search_fields = ['car']


class PassportDriverAdmin(admin.ModelAdmin):
    list_display = ['driver']
    list_filter = ['driver']
    search_fields = ['driver']


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


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(InsuranceEvent, InsuranceEventAdmin)
admin.site.register(ImagesInsuranceEvent, ImagesInsuranceEventAdmin)
admin.site.register(TechPassport, TechPassportAdmin)
admin.site.register(TechPassportScans, TechPassportScansAdmin)
admin.site.register(PassportDriver, PassportDriverAdmin)
admin.site.register(DriverScans, DriverScansAdmin)
