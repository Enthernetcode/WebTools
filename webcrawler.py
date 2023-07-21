#!/data/data/com.termux/files/usr/bin/python3.11
import requests
import time
from bs4 import BeautifulSoup
import socket
import scapy
import base64
import os
import subprocess

####################################
#########  c o l o r s #############
red = "\033[1;31m"		   #
green = "\033[1;32m"		   #
cyan = "\033[1;36m"		   #
yea = "\033[1;35m"		   #
####################################
Css = []
list = []
script = []
Title = []
links = []
images = []
crawled = []
def getWebContent(link):
    updater = requests.get(link)
    # Parsing imto a list if source code is to be scraped
    filtering(updater)
def filtering(updater):
    filter = BeautifulSoup(updater.content, "html.parser")
    filtered = filter.select("a") #filter.find_all("a")
    title = filter.title.string
    jsScript = filter.find_all("script")
    css = filter.find_all("link")
    img = filter.find_all("img")
    update(updater, css, jsScript, title, filtered, img)
def update(updater, css, jsScript, title, filtered, img):
    try:
     list.append(updater.text)
     for c in css:
      css = c.get("href")
      try:
        if css[0] != "h":
         Css.append(f"{link}"+css)
        else:
         Css.append(css)
      except TypeError:
         continue
     for s in jsScript:
      jsScript = s.get("src")
      try:
        if jsScript[0] != "h":
         script.append(f"{link}"+jsScript)
        else:
         script.append(jsScript)
      except TypeError:
         continue
     Title.append(title)
     for l in filtered:
      filtered = l.get("href")
      try:
        if filtered[0] != "h":
         links.append(f"{link}"+filtered)
        else:
         links.append(filtered)
      except TypeError:
         continue
     for i in img:
      img = i.get("src")
      try:
        if img[0] != "h":
         images.append(f"{link}"+img)
        else:
         images.append(img)
      except TypeError:
         continue
    except:
#     continue
      return 0
def inputer():
    global link
    link = input(f"{red}Enter domain name to crawl: \t")
    print (f"{yea}Please wait patiently................")
    getWebContent(link)

def loop(images):
    for lo in images:
#     for l in lo:
      lo = lo.prettify(lo)
      print (lo, end="\n")
def crawler():
       for links in crawled:
         if links[0] == "h":
            getWebContent(links)
#         else:
#            getWebContent(f"{link}"+links)

def crawl():
      for css in  Css:
         crawled.append(css)
      for scripts in  script:
         crawled.append(scripts)
      for image in  images:
         crawled.append(image)
      for lin in  links:
         crawled.append(lin)
def choose(link):
    opt = int(input(f"{yea}Enter list to filter:\t options \n1. source code\n2. css links\n3. js scripts\n4. image link\n5. links\nChoose Options:\t"))
    if opt == 1:
      for lists in  list:
       print (f"\n{lists}\n")
    elif opt == 2:
      for css in  Css:
       print (f"\n{css}\n")
    elif opt == 3:
      for scripts in  script:
         print (f"\n{scripts}\n")
    elif opt == 4:
      for image in  images:
         print (f"\n{image}\n")
    elif opt == 5:
      crawl()
      for link in  crawled: #, script, Css:
#       for lin in link:
        print (f"\n{link}\n",end="\n")
#    loop(loop)
inputer()
crawler()# loop(list) 
choose(link)
print (link)
#print (f"""
#{green}Css scripts found {yea}{Css}\n
#{green}Site source code {yea}{red}\n
#{green}JS scripts found {yea}{script}\n
#{green}Site title {yea}{Title}\n
#{green}Links found on site {cyan}{links}\n
#{cyan}Images found {green}{images}
#""")

