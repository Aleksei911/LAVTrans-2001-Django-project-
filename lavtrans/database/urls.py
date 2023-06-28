from django.urls import include, path
from rest_framework import routers
from .views import CarViewSet, DriverViewSet, cars, car_edit, add_car, drivers, add_driver, driver_edit, car_info, \
    event_info, add_car_event

router = routers.DefaultRouter()

router.register(r'Cars', CarViewSet)
router.register(r'Drivers', DriverViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', cars, name='cars'),
    path('add_car/', add_car, name='add_car'),
    path('<int:pk>/car_edit/', car_edit, name='car_edit'),
    path('<int:pk>/car_info/', car_info, name='car_info'),
    path('drivers/', drivers, name='drivers'),
    path('add_driver/', add_driver, name='add_driver'),
    path('<int:pk>/driver_edit/', driver_edit, name='driver_edit'),
    path('<int:pk>/event_info/', event_info, name='event_info'),
    path('add_car_event/', add_car_event, name='add_car_event'),
]
