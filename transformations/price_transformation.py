class itemPrice:
    
    def calculate_discount(self):
        print(f'Price after discount : {self.price *self.discount/100}')

        return
item_price1 = itemPrice()
item_price1.price =500
item_price1.discount =10
item_price1.calculate_discount();
