#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.prices = []

  def add_item(self, item, price, quantity = 1):
    self.total += (price * quantity)

    self.prices.append(price * quantity)

    for num in range(quantity):
      self.items.append(item)

  def apply_discount(self):
    self.total = self.total - ((self.total * self.discount) / 100)

    if self.discount:
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else: 
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.prices.pop()