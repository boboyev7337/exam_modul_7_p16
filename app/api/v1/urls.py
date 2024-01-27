from django.urls import path

from rest_framework import routers

from app.api.v1.views import UserPasswordManagerModelViewSet

router = routers.DefaultRouter()

router.register(r'user-password', UserPasswordManagerModelViewSet)

urlpatterns = []

urlpatterns += router.urls