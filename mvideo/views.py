from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from mvideo.models import Supplier
from mvideo.serializers import SupplierSerializerCreate, SupplierSerializerUpdate, SupplierSerializer


class SupplierListAPIView(ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializerCreate
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['contact__country']


class SupplierCreateAPIView(CreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializerCreate
    permission_classes = [IsAuthenticated]


class SupplierUpdateAPIView(UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializerUpdate
    permission_classes = [IsAuthenticated]


class SupplierDestroyAPIView(DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class SupplierRetrieveAPIView(RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

