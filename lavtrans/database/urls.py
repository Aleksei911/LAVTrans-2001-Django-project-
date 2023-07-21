from django.urls import include, path
from rest_framework import routers
from .views import CarViewSet, DriverViewSet, cars, car_edit, add_car, drivers, add_driver, driver_edit, car_info, \
    event_info, add_car_event, event_edit, add_photo, driver_info, add_techpassport, techpassport_info

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
    path('<int:pk>/driver_info/', driver_info, name='driver_info'),
    path('<int:pk>/event_info/', event_info, name='event_info'),
    path('<int:pk>/add_car_event/', add_car_event, name='add_car_event'),
    path('<int:pk>/event_edit/', event_edit, name='event_edit'),
    path('<int:pk>/add_photo/', add_photo, name='add_photo'),
    path('<int:pk>/add_techpassport/', add_techpassport, name='add_techpassport'),
    path('<int:pk>/techpassport_info/', techpassport_info, name='techpassport_info'),
]
