# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 20:15:57 2021

@author: tmisk
"""

import tkinter as tk
from tkinter import ttk
import scraping_functions as function

class Interface(ttk.Frame):
    
    def __init__(self, container):
        super().__init__(container)

        #######################################################################
        
        self.user_price_minimum = tk.StringVar()
        
        minimum_price = ttk.Label(self, text="Minimum price is: ")
        minimum_price.grid(row=0, column=0, padx=5, pady=5)
        minimum_price_entry = ttk.Entry(self, width=15, textvariable=self.user_price_minimum)
        minimum_price_entry.grid(row=0, column=1)
        minimum_price_entry.focus()

        #######################################################################
        
        self.user_price_maximum = tk.StringVar()
        
        maximum_price = ttk.Label(self, text="Maximum price is: ")
        maximum_price.grid(row=1, column=0,padx=5, pady=5)
        maximum_price_entry = ttk.Entry(self, width=15, textvariable=self.user_price_maximum)
        maximum_price_entry.grid(row=1, column=1)
        maximum_price_entry.focus()
        
        #######################################################################
        
        self.min_flat_area = tk.StringVar()
        
        min_flat_area = ttk.Label(self, text="Minimum flat area is: ")
        min_flat_area.grid(row=2, column=0,padx=5, pady=5)
        min_flat_area_entry = ttk.Entry(self, width=15, textvariable=self.min_flat_area)
        min_flat_area_entry.grid(row=2, column=1)
        min_flat_area_entry.focus()
        
        #######################################################################
        
        self.max_flat_area = tk.StringVar()
        
        max_flat_area = ttk.Label(self, text="Maximum flat area is: ")
        max_flat_area.grid(row=3, column=0,padx=5, pady=5)
        max_flat_area_entry = ttk.Entry(self, width=15, textvariable=self.max_flat_area)
        max_flat_area_entry.grid(row=3, column=1)
        max_flat_area_entry.focus()
        
        #######################################################################
        
        self.private_offer = tk.StringVar()
        
        private_offer = ttk.Label(self, text="Is it praivate offer (true or false): ")
        private_offer.grid(row=4, column=0,padx=5, pady=5)
        private_offer_entry = ttk.Entry(self, width=15, textvariable=self.private_offer)
        private_offer_entry.grid(row=4, column=1)
        private_offer_entry.focus()
        
        #######################################################################
        
        self.rooms = tk.StringVar()
        
        rooms = ttk.Label(self, text="How many rooms do you want to: ")
        rooms.grid(row=5, column=0,padx=5, pady=5)
        rooms_entry = ttk.Entry(self, width=15, textvariable=self.rooms)
        rooms_entry.grid(row=5, column=1)
        rooms_entry.focus()
        
        #######################################################################
        
        scraper_button = ttk.Button(self, text="Show offers", command=lambda: [function.scraper(self), function.otodom(self), function.olx(self), function.gumtree(self), function.finall_file(self)])
        
        scraper_button.grid(column=0, rows=2, columnspan=2, padx=5, pady=5)

root = tk.Tk()
root.geometry("450x250")
root.title("Looking for a flat")
root.columnconfigure(0, weight=1)

frame = Interface(root)
frame.pack()

root.mainloop()

