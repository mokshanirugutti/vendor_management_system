from django.urls import path
from . import purchase_views,user_views,vendor_views

urlpatterns = [
    path('signup/', user_views.signup, name='signup'),
    path('login/', user_views.login, name='login'),
    path('vendors/', vendor_views.get_vendors, name='get-vendors'),
    path('vendors/<str:pk>/', vendor_views.vendor_crud, name='get-update-vendor'),
    path('vendors/<str:pk>/performance/', vendor_views.get_vendor_performance, name='get-vendor-performance'),
    path('purchase_orders/', purchase_views.get_purchase_orders, name='purchase_orders'),
    path('purchase_orders/<str:po_id>/', purchase_views.purchase_order_detail, name='purchase-order-detail'),
]
