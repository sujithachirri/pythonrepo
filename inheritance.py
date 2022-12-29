#inheritance
class product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating

    def display_product_details(self):
       print("product:{}".format(self.name))
       print("price:{}".format(self.price))
       print("deal_price:{}".format(self.deal_price))
       print("rating:{}".format(self.rating))
    def get_deal_price(self):
        return self.deal_price
class electronicdevice(product):
   def set_warrenty(self,warrenty_in_months):
       self.warrenty_in_months=warrenty_in_months
   def get_warrenty(self):
       return self.warrenty_in_months

class groceryitem(product):
    pass
class order:
    def __init__(self,delivary_speed,delivary_address):
        self.items_in_cart=delivary_speed
        self.delivary_address=delivary_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))








