from django.urls import path
from api.views import ProductListCreateView, OrderCreateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='products'),
    path('orders/', OrderCreateView.as_view(), name='orders'),
]
