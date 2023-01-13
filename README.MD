### Project Python Pacmann


#### Latar belakang masalah




#### Requirements / objectives



#### Flowchart


!['Flowchart app'](./images/python_cashier_project.drawio.png)

The cashier app program operates as a self-service system, beginning with displaying the menu options to the customer. There are a total of 7 menu items, as shown in the accompanying image :

!['Menu Awal'](./images/1.PNG)

Customers can add items to their order by selecting menu option 1. However, before making a selection, it is important to note that inputting an incorrect menu choice, such as number 8 or non-digit characters, will result in an error message "Invalid selection. Try again." as shown in the accompanying images.

!['Salah Pilih Menu'](./images/2.PNG)  
!['Salah Pilih Menu'](./images/3.PNG)

After selecting the correct menu as displayed, customers can add items to their transaction by choosing menu option 1. They will then be prompted to input the product name, quantity, and price per item. Once these details have been successfully input, the customer will be asked if they wish to add more items to the transaction. If they choose to do so, they should input "y", otherwise, they should input "n" if they do not wish to add any more items.

!['Menu 1'](./images/4.PNG)

If the customer chooses to add more items, they will be prompted to input the product details (product name, quantity, and price per item) as before, and the process will repeat until the customer chooses to end the transaction by inputting "n".

!['Menu 1-Tambah Items Lain'](./images/5.PNG)

By selecting menu option 2 (View items), customers can view all of the items they have added to their transaction, including the product name, quantity, and the total price per product.

!['Menu 2'](./images/6.PNG)

Menu option 4 (Update item) allows customers to make changes to items they have already added to their transaction. After selecting this menu, a list of products that have been input will be displayed. Customers can then select the number of the product they wish to update and make necessary changes.

!['Menu 4 - List Produk'](./images/7.PNG)

For example, if a customer wants to update item number 3 (Semangka) they would select number 3 from the list of products. The customer would then be presented with the option to update the product name (1), quantity (2), price per item (3) or to cancel the update (4). The latter option would return the customer to the main menu in case they have chosen the wrong product to update.

!['Menu 4 - Produk terpilih - Action Update'](./images/8.PNG)

If the customer chooses menu option 1, they will be prompted to input the new name of the product. For example, if they initially input the name of the product as `semangka` and later realize it should be `Semangka Merah`, they can update the name in this menu.

!['Menu 4 - Produk terpilih - Update Nama'](./images/9.PNG)

If the customer chooses menu option 2, they will be prompted to input the new quantity of the product. For example, if they initially input the quantity as `2` and later realize they want to change it to `12`, they can update the quantity in this menu.

!['Menu 4 - Produk terpilih - Update Quantity'](./images/10.PNG)

If the customer chooses menu option 3, they will be prompted to input the new price per item of the product. For example, if they initially input the price per item as `50000` and later realize they want to change it to `55000`, they can update the price in this menu.

!['Menu 4 - Produk terpilih - Update Quantity'](./images/11.PNG)

