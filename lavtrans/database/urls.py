from django.urls import include, path
from rest_framework import routers
from .views import CarViewSet, DriverViewSet, cars, car_edit, add_car, drivers, add_driver, driver_edit

router = routers.DefaultRouter()

router.register(r'Cars', CarViewSet)
router.register(r'Drivers', DriverViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('ts/', cars, name='cars'),
    path('add-card/', add_car, name='add_car'),
    path('<int:pk>/car-edit/', car_edit, name='car_edit'),
    path('voditeli/', drivers, name='drivers'),
    path('add-driver/', add_driver, name='add_driver'),
    path('<int:pk>/driver-edit/', driver_edit, name='driver_edit'),
]
