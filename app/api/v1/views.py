from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from app.api.v1.serializers import UserPasswordManagerSerializer
from app.models import UserPasswordManager


class UserPasswordManagerModelViewSet(viewsets.ModelViewSet):
    queryset = UserPasswordManager.objects.all()
    serializer_class = UserPasswordManagerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['^name']
    filterset_fields = ['application_type']


class UserPasswordManagerAPIView(APIView):
    queryset = UserPasswordManager.objects.all()
    serializer_class = UserPasswordManagerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

