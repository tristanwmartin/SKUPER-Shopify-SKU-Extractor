#Extract SKU's Shopify store
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize 
from bs4 import BeautifulSoup # as bs
import requests
import re
import json
import tkinter as tk
from tkinter.ttk import *

sku_lookup = 'sku'

counter = 4


def Lookup(h_list, lookup):
    sku_idx = h_list.index(lookup)

    return h_list[sku_idx+counter]

def make_list(string):
    str_list = []
    str_list = word_tokenize(string)

    return str_list

def requestHTML(url):
    r = requests.get(url)
    return r.text

def getProductData(product_url):
    product_html = requestHTML(product_url)
    html_list = make_list(product_html)
    
    return Lookup(html_list, sku_lookup)
    
def Operate():
    e2.delete(0, 'end')
    url = url_var.get()
    e2.insert(0, getProductData(url))

def UpClick():
    global counter
    counter += 1
    Operate()

def DownClick():
    global counter
    counter += -1
    Operate()


master = tk.Tk()
master.title("SKUPER | Shopify SKU Extractor")
master.geometry("600x120")
master.configure(bg='black')

url_var = tk.StringVar()
    
tk.Label(master, text="URL", bg='black', fg='green').grid(row=0)
tk.Label(master, text="SKU", bg='black', fg='green').grid(row=1)
tk.Label(master, text="DEBUG", bg='black', fg='green').grid(row=3, column=2, sticky='nsew')
tk.Label(master, text="", bg='black', fg='black').grid(row=0, column=5, rowspan=4)

e1 = tk.Entry(master, textvariable = url_var, width=90, bg='grey', fg='white')
e2 = tk.Entry(master, width=90, bg='grey', fg='white')

e1.grid(row=0, column=1, columnspan=4, pady=10, sticky="nsew")
e2.grid(row=1, column=1, columnspan=4, pady=10, sticky="nsew")

tk.Button(master,
          text='Scoop SKU',
          command=Operate, bg='black', fg='green', padx=100).grid(row=3,
                                column=1)
tk.Button(master,
          text='↓',
          command=DownClick, bg='black', fg='green', padx=20).grid(row=3,
                                column=3, sticky='nsew')
tk.Button(master,
          text='↑',
          command=UpClick, bg='black', fg='green', padx=20).grid(row=3,
                                column=4, sticky='nsew')

master.grid_columnconfigure(1, weight=2)
master.grid_columnconfigure(2, weight=2)
master.grid_columnconfigure(3, weight=2)
master.grid_columnconfigure(4, weight=2)

master.mainloop()



