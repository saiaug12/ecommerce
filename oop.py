class Product:
    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_saved = price - deal_price 
    

    def display_productdetails(self):
        print("Product name : {}".format(self.name))
        print("Price : {}".format(self.price))
        print("Deal_price : {}".format(self.deal_price))
        print("rating : {}".format(self.rating))
        print("you_saved : {}".format(self.you_saved))

class Electronicitem(Product):
    def __init__(self, name, price, deal_price, rating, warranty_in_months):
        super().__init__(name, price, deal_price, rating)
        self.warranty_in_months = warranty_in_months
    
    def display_productdetails(self):
        super().display_productdetails()
        print("warranty : {} months ".format(self.warranty_in_months))

class Groceryitem(Product):
    def __init__(self, name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date = expiry_date
    
    def display_productdetails(self):
        super().display_productdetails()
        print("Expirydate : {} ".format(self.expiry_date))
class Order:
    delivery_charges = {
        "Normal" : 0,
        "Prime_delivery" : 99
    }
    def __init__(self, delivery_method, delivery_address):
        self.items_in_cart = []
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        item = (product, quantity)
        self.items_in_cart.append(item)
        print(self.items_in_cart)
    
    def display_order_details(self):
        print("Delivery method : {}".format(self.delivery_method))
        print("Delivery_address : {}".format(self.delivery_address))
        print("Products")
        print("==============================================================")
        for product, quantity in self.items_in_cart:
            product.display_productdetails()
            print("Quantity : {}".format(quantity))
            print(" ")

    def tot_bill(self):
        Total_B = 0
        for product, quantity in self.items_in_cart:
            Bill = product.deal_price*quantity
            Total_B+=Bill
            print(f"Totalbill for your {product}  : {Total_B}")



p = Electronicitem("Washing machine", 50000, 30000, 4.8, 50)
#p.display_productdetails()
g = Groceryitem("Maggie", 200, 150, 4.5, 2023)
#g.display_productdetails()
A = Order("Normal","Tadipatri")
A.add_item(p, 3)
A.add_item(g, 2)
A.display_order_details()
A.tot_bill()