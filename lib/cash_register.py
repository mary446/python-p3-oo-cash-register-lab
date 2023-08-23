#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount=0.0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0
        self.last_transaction_quantity = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title]*quantity)
        self.last_transaction_amount = price
        self.last_transaction_quantity = quantity

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            if self.total % 1 == 0:  # check if the decimal part is .00
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount * self.last_transaction_quantity
        for _ in range(self.last_transaction_quantity):
            self.items.pop()


  
