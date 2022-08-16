from xmlrpc.client import DateTime
from django.shortcuts import render
from django.views.generic import View
from .models import ShoppingCart, ShoppingCartProductUnitItem, CartStatus
from django.http import JsonResponse
from products.models import ProductUnit
import datetime
import json
# Create your views here.

class OpenedCartDetails(View):
    def get(self, request, id):
        try:
            shopping_cart = ShoppingCart.objects.get(pk=int(id))
            if shopping_cart.status == CartStatus.CONFIRMED:
                return render(request=request, template_name="shopping_cart/already_confirmed_cart.html")
            shopping_cart_ctx = {"id": shopping_cart.id ,"total_price": shopping_cart.total_price, "items": []}
            for item in shopping_cart.shopping_cart_product_unit_items.select_related():
                item_ctx = {
                    "id" : item.id,
                    "img" : item.product_unit.product.image.url,
                    'name' : item.product_unit.product.name,
                    'description' : item.product_unit.product.description,
                    'product_unit' : item.product_unit,
                    'price' : item.price,
                    'quantity': item.quantity,
                    'total_price': item.price * item.quantity
                }
                shopping_cart_ctx['items'].append(item_ctx)
            ctx = {"shopping_cart" :  shopping_cart_ctx}
            return render(request=request, template_name="shopping_cart/oppened_cart_details.html", context=ctx)
        except ShoppingCart.DoesNotExist:
            return render(request=request, template_name="shopping_cart/cart_not_found.html")


class ConfirmCartView(View):
    def post(self, request):
        #parse data
        data = json.loads(request.body.decode('utf-8'))['items']
        #Check Inventeroy 
        errors = []
        for item in data:
            inventroyStorage = ProductUnit.objects.get(pk = item['product_unit_id']).inventroy_product_unit_storage
            if inventroyStorage.quantity < item['quantity']:
                error_message = "We only have {0} {1} of {2} left".format(inventroyStorage.quantity, inventroyStorage.product_unit.name, inventroyStorage.product_unit.product.name)
                errors.append(error_message)
        if len(errors) > 0:
            return JsonResponse({'errors': errors})

        #Update Cart Items Data After Validating the Quantities     
        total_price = 0    
        for idx, item in  enumerate(data):
            shoping_cart_item = ShoppingCartProductUnitItem.objects.get(pk=item['id'])
            shoping_cart_item.price = item['price']
            shoping_cart_item.quantity = item['quantity']
            total_price += shoping_cart_item.price * shoping_cart_item.quantity
            shoping_cart_item.product_unit = ProductUnit.objects.get(pk = item['product_unit_id'])
            shoping_cart_item.save()
            #Update Inventory Storage
            inventroyStorage = ProductUnit.objects.get(pk = item['product_unit_id']).inventroy_product_unit_storage
            inventroyStorage.quantity -= shoping_cart_item.quantity
            inventroyStorage.save()
            #Update Cart Info
            if idx == (len(data)-1):
                cart = shoping_cart_item.shopping_cart
                cart.status = CartStatus.CONFIRMED
                cart.close_date = datetime.datetime.now()
                cart.total_price = total_price
                cart.save()

        return JsonResponse({"errors" : [], "message": "Cart Confirmed Thanks for choosing us!"})

    



        


