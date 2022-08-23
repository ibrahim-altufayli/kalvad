from django.urls import path
from .views import ProductUnitDetailsView

urlpatterns = [path("product-unit/<int:id>", ProductUnitDetailsView.as_view())]
