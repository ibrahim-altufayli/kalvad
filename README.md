# kalvad Cart Assignment 
To Install and run the application, we have to do the following steps:
- We have to install python 3.10 from it is official website https://www.python.org/.
- Install the required libs by using the updated requirements.txt, please run the following command on the project root folder "pip install to-requirements.txt". 
- It is preferable to create and activate a virtual environment to isolate project libs from the global one.
- Navigate to the project root and run "python manage.py runserver", you do not need to makeigrations, migrate or createsuperuser because the project is shipped with sqllite file that holds everything.
- No need to collect the static files, files already collected.
-You can access the admin panel by visiting http://127.0.0.1:8000/admin and using username=kalvad/password=P@ssw0rd
- We can define new products, product units, shopping carts, cart items inside the admin panel(I did not adjust the admin's UI or functionality because it serves the need of creating the required entities).
-We can change the inventory storage quantity from the admin by navigating to http://127.0.0.1:8000/admin/products/inventoryproductunitstorage/
* To make things clear we have the following entities inside the database:
  * *Product* 
  * *Product Unit*(price is defined here)(once we create a new Product Unit a new unique *Inventory Product Unit Storage* record will be created with the quantity of 0)
  * *Inventory Product Unit Storage*(Storage quantity is stored here and each time we confirm a cart the confirmed quantities will be subtracted from the storage)
  * *Shopping Cart*
  * *Shopping Cart Product Unit Item*(Represents the Cart Items)
* We can access the opened shopping carts by visiting the following URL http://127.0.0.1:8000/cart/oppened-cart-details/int:id
* Closed shopping carts and not-found carts cases are handeled Ex: http://127.0.0.1:8000/cart/oppened-cart-details/5 (Confirmed) http://127.0.0.1:8000/cart/oppened-cart-details/63 (Not-Found).
* the required instance could be accessed by visiting  http://127.0.0.1:8000/cart/oppened-cart-details/3
* Another instance that shows that you can change the unit of product could be accessed by visiting http://127.0.0.1:8000/cart/oppened-cart-details/4 
* To create a new Cart, we have to define the cart and define the related *Shopping Cart Product Unit Item* /the cart's total price will be recalculated on each shopping cart unit item save(in the model save() method)/.
* The black package was used to format the project by running the following command in the root of the project "python -m black ." and it was added to the requirements.txt file.
