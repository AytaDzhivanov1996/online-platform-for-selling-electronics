from django.urls import path

from mvideo.views import SupplierListAPIView, SupplierCreateAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, \
    SupplierDestroyAPIView

urlpatterns = [
    path('suppliers/', SupplierListAPIView.as_view()),
    path('suppliers/create/', SupplierCreateAPIView.as_view()),
    path('suppliers/update/<int:pk>/', SupplierUpdateAPIView.as_view()),
    path('suppliers/destroy/<int:pk>/', SupplierDestroyAPIView.as_view()),
    path('suppliers/retrieve/<int:pk>/', SupplierRetrieveAPIView.as_view()),
]
