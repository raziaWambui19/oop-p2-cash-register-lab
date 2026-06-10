class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []
        
    @property 
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
            self._discount = 0
        else:
            self._discount = value

    def add_item(self, item, price, quantity): 
        self.total += price * quantity
        self.items.extend([item] * quantity)
         
        self.previous_transactions.append(
            {
                "item": item,
                "price": price,
                "quantity": quantity
            }
         )
        
    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
            
    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        
        last_transaction = self.previous_transactions.pop()

        item = last_transaction["item"]
        price = last_transaction["price"]   
        quantity = last_transaction["quantity"]

        self.total -= price * quantity 

        for _ in range(quantity):
            if item in self.items:
                self.items.remove(item)