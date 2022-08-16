from django.urls import path
from .views import OpenedCartDetails, ConfirmCartView

urlpatterns = [
    path("oppened-cart-details/<int:id>", OpenedCartDetails.as_view()),
    path("confirm-cart", ConfirmCartView.as_view())
]