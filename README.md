# kalvad
Cart Assignment 
To Install and run the application, we have to do the following steps:
- we have to install python 3.10 from it is official website.
- Install Django  (make sure that python is installed) run "python -m pip install Django" on cmd.
- Install Pillow /We have used images for products/ run "pip install pillow" on cmd.
- It is more prefarable to create and activate a virtual enviroment to isolate project libs from global one.
- Navigate to the project root and run "python manage.py runserver" / you do not need to makeigrations or migrate or createsuperuser because the project is shipped with sqllite file that hold everything.
-You can access the admin by visiting http://127.0.0.1/admin and using username=kalvad/password=P@ssw0rd
- We can define new products, product units, shopping carts, cart items inside the admin(I did not adjusted the admin UI or functionality but it serve the need of creating the required entites).
-We can change the inventory storage quantity from the admin by navigating to http://127.0.0.1:8000/admin/products/inventroyproductunitstorage/
- To make things clear we have the following entites inside database:
--Product 
--Product Unit(price is defined here)(once we create a new Product Unit a new unique Inventroy Product Unit Storage record will be created with the quantity of 0)
--Inventroy Product Unit Storage(Storage quantity is stored here and each time we confirm a cart the confirmed quantites will subtracted from the storage)
--Shopping Cart
--Shopping Cart Product Unit Item(Represent the Cart Items)
-We can access the oppened shoping carts by visiting the following url http://127.0.0.1:8000/cart/oppened-cart-details/<int:id>
-the rquired instance could be accsessed by visiting  http://127.0.0.1:8000/cart/oppened-cart-details/3
-Another instance that shows that you can change the unit of product could be accessed by visiting http://127.0.0.1:8000/cart/oppened-cart-details/4 
