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
    list_display = [field.name for field in ImagesInsuranceEvent._meta.fields]


class InsuranceEventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InsuranceEvent._meta.fields]
    inlines = [ImagesInsuranceEventInline]


class DriverAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Driver._meta.fields]
    inlines = [InsuranceEventInline]


class CarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.fields]
    inlines = [InsuranceEventInline]


admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(InsuranceEvent)
admin.site.register(ImagesInsuranceEvent)
