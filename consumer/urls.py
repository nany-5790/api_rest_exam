from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('v2/get/parcel/tracking.json/', views.get_parcel_tracking),
    path('v2/', include(router.urls)),
]
