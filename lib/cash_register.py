#!/usr/bin/env python3


  class CashRegister:

    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []


    def add_item(self, title, price, quantity=1):

        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(title)

        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })


    def apply_discount(self):

        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)

        self.total -= discount_amount

        print(f"After the discount, the total comes to ${self.total}.")


    def void_last_transaction(self):

        if len(self.previous_transactions) == 0:
            return

        last = self.previous_transactions.pop()

        amount = last["price"] * last["quantity"]

        self.total -= amount

        for _ in range(last["quantity"]):
            self.items.remove(last["title"])

        if self.total <= 0:
            self.total = 0.0


    def get_items(self):
        return self.items
