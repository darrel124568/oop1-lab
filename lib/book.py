#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def set_pages(self, page_count):
        if type(page_count) is int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    def get_pages(self):
        return self._page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")  

    page_count = property(get_pages, set_pages)
        