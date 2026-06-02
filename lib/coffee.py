#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    def set_size(self, size):
        if size in ["Small", "Medium", "Large"] :
            self._size = size
        else:
            print("size must be Small, Medium, or Large")
    def get_size(self):
        return self._size

    def tip(self):
        print("This coffee is great, here’s a tip!")  
        self.price += 1

    size = property(get_size, set_size)