# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:15:04 2021

@author: tmisk
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import messagebox

def scraper(self):

    price_min = self.user_price_minimum.get()
    price_min = int(price_min)
    
    price_max = self.user_price_maximum.get()
    price_max = int(price_max)
    
    min_flat_area = self.min_flat_area.get()
    min_flat_area = int(min_flat_area)
    
    max_flat_area = self.max_flat_area.get()
    max_flat_area = int(max_flat_area)
    
    private_offer = self.private_offer.get()

    rooms = self.rooms.get()
    rooms = int(rooms)

    return price_min, price_max, min_flat_area, max_flat_area, private_offer, rooms
    
def otodom(self):
    
    price_min, price_max, min_flat_area, max_flat_area, private_offer, rooms =scraper(self)
    links = []
        
    for page_num in range(1, 10):
    
        url = (f'https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/wiele-lokalizacji?roomsNumber=%5BTWO%2CTHREE%5D'\
               f'&priceMin={price_min}&priceMax={price_max}&areaMin={min_flat_area}&areaMax={max_flat_area}&isPrivateOwner={private_offer}&market=SECONDARY&page=1&limit=24'\
               f'&locations=%5B%5Bobject+Object%5D%2C%5Bobject+Object%5D%2C%5Bobject+Object%5D%2C%5Bobject+Object%5D%2C%5Bobject'\
               f'+Object%5D%2C%5Bobject+Object%5D%2C%5Bobject+Object%5D%2C%5Bobject+Object%5D%2C%5Bobject+Object%5D%2C%5Bobject'\
               f'+Object%5D%5D&by=DEFAULT&direction=DESC&locations%5B0%5D%5BregionId%5D=7&locations%5B0%5D%5BcityId%5D=26'\
               f'&locations%5B0%5D%5BdistrictId%5D=44&locations%5B0%5D%5BsubregionId%5D=197&locations%5B1%5D%5BregionId%5D=7'\
               f'&locations%5B1%5D%5BcityId%5D=26&locations%5B1%5D%5BdistrictId%5D=117&locations%5B1%5D%5BsubregionId%5D=197'\
               f'&locations%5B2%5D%5BregionId%5D=7&locations%5B2%5D%5BcityId%5D=26&locations%5B2%5D%5BdistrictId%5D=50'\
               f'&locations%5B2%5D%5BsubregionId%5D=197&locations%5B3%5D%5BregionId%5D=7&locations%5B3%5D%5BcityId%5D=26'\
               f'&locations%5B3%5D%5BdistrictId%5D=174&locations%5B3%5D%5BsubregionId%5D=197&locations%5B4%5D%5BregionId%5D=7'\
               f'&locations%5B4%5D%5BcityId%5D=26&locations%5B4%5D%5BdistrictId%5D=11619&locations%5B4%5D%5BsubregionId%5D=197'\
               f'&locations%5B5%5D%5BregionId%5D=7&locations%5B5%5D%5BcityId%5D=26&locations%5B5%5D%5BdistrictId%5D=36'\
               f'&locations%5B5%5D%5BsubregionId%5D=197&locations%5B6%5D%5BregionId%5D=7&locations%5B6%5D%5BcityId%5D=26'\
               f'&locations%5B6%5D%5BdistrictId%5D=40&locations%5B6%5D%5BsubregionId%5D=197&locations%5B7%5D%5BregionId%5D=7'\
               f'&locations%5B7%5D%5BcityId%5D=26&locations%5B7%5D%5BdistrictId%5D=47&locations%5B7%5D%5BsubregionId%5D=197'\
               f'&locations%5B8%5D%5BregionId%5D=7&locations%5B8%5D%5BcityId%5D=26&locations%5B8%5D%5BdistrictId%5D=39'\
               f'&locations%5B8%5D%5BsubregionId%5D=197&locations%5B9%5D%5BregionId%5D=7&locations%5B9%5D%5BcityId%5D=26'\
               f'&locations%5B9%5D%5BdistrictId%5D=45&locations%5B9%5D%5BsubregionId%5D=197')
        
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        
        
        for a_href in soup.find_all("a", href=True):
            links.append(a_href["href"])
        
        valid_links = [i for i in links if i.startswith('/pl/oferta/')]
        string = 'https://www.otodom.pl'
        
        valid_links_ = [string + s for s in valid_links]
        
        df_valid_links = pd.DataFrame(valid_links_)
        df_valid_links["Strona zawierająca ofertę"] = "Otodom"
        df_valid_links = df_valid_links.rename(columns={0:"Link"})
        df_otodom = df_valid_links
    
    return df_otodom

def olx(self):
    
    price_min, price_max, min_flat_area, max_flat_area, private_offer, rooms =scraper(self)

    links_olx = []
    
    for page_num in (367, 359, 351, 371, 353, 357, 369, 355, 373, 377):
    
        url = (f'https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/?search%5Bfilter_float_price%3Afrom%5D={price_min}' \
               f'&search%5Bfilter_float_price%3Ato%5D={price_max}&search%5Bfilter_float_m%3Afrom%5D={min_flat_area}' \
               f'&search%5Bfilter_float_m%3Ato%5D={max_flat_area}&search%5Bfilter_enum_rooms%5D%5B0%5D=three&search%5Bdistrict_id%5D=')+ str(page_num)

        
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        
        
        
        for a_href in soup.find_all("a", href=True):
            links_olx.append(a_href["href"])
        
        valid_links = [i for i in links_olx if i.startswith('https://www.olx.pl/d/oferta')]
        
        not_promoted = [i for i in valid_links if not i.endswith(';promoted')]
        not_promoted = list(set(not_promoted))
        
        df_valid_links = pd.DataFrame(not_promoted)
        df_valid_links["Strona zawierająca ofertę"] = "Olx"
        df_valid_links = df_valid_links.rename(columns={0:"Link"})
        df_olx = df_valid_links
    
    return df_olx

def gumtree(self):
    
    price_min, price_max, min_flat_area, max_flat_area, private_offer, rooms =scraper(self)
    
    links_gumtree = []
    
    for name in ('bemowo','bielany','mokotow','ochota','ursynow','wola','targowek'):
        url = (f'https://www.gumtree.pl/s-mieszkania-i-domy-sprzedam-i-kupie/warszawa/v1c9073l3200008p1?' + \
               f'pr={price_min},{price_max}&df=ownr&nr={rooms}').format(name)
   

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")



        for a_href in soup.find_all("a", href=True):
            links_gumtree.append(a_href["href"])

        valid_links_gumtree = [i for i in links_gumtree if i.startswith('/a-')]

        string_ = 'https://www.gumtree.pl'

        valid_links_gumtree = [string_ + y for y in valid_links_gumtree]

        valid_links_gumtree = pd.DataFrame(valid_links_gumtree)
        valid_links_gumtree["Strona zawierająca ofertę"] = "Gumtree"
        valid_links_gumtree = valid_links_gumtree.rename(columns={0:"Link"})
        df_gumtree = valid_links_gumtree
        
    return df_gumtree

def finall_file(self):
    
    df_otodom = otodom(self)
    df_olx = olx(self)
    df_gumtree = gumtree(self)
    
    frames = [df_otodom, df_olx, df_gumtree]
    df_finall = pd.concat(frames)
    df_finall["Link"] = df_finall["Link"].astype(str)
    
    df_finall = df_finall.drop_duplicates()
    df_finall = df_finall.reset_index(drop=True)
    not_look_for = ["bialoleka","ursus","rembertow"]
    df_finall = df_finall[~df_finall["Link"].str.contains('|'.join(not_look_for))]
          
    df_finall.to_excel("Results of flats.xlsx")
    
    messagebox.showinfo(title="The end", message="Excel file with results is ready to check :)")