from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import View
from .models import ProductUnit

# Create your views here.
class ProductUnitDetailsView(View):
    def get(self, request, id):
        qs = get_object_or_404(ProductUnit, pk=id)
        product_unit_details = {
            "id": qs.id,
            "name": qs.name,
            "product_id": qs.product_id,
            "price": qs.price,
        }
        return JsonResponse(product_unit_details)
