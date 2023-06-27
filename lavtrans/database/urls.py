from django.urls import include, path
from rest_framework import routers
from .views import CarViewSet, DriverViewSet, cars, car_edit, add_car, drivers, add_driver, driver_edit, car_info

router = routers.DefaultRouter()

router.register(r'Cars', CarViewSet)
router.register(r'Drivers', DriverViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', cars, name='cars'),
    path('add-car/', add_car, name='add_car'),
    path('<int:pk>/car-edit/', car_edit, name='car_edit'),
    path('<int:pk>/car_info/', car_info, name='car_info'),
    path('drivers/', drivers, name='drivers'),
    path('add-driver/', add_driver, name='add_driver'),
    path('<int:pk>/driver-edit/', driver_edit, name='driver_edit'),
]
