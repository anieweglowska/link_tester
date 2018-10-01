#-*- coding: utf-8 -*-
from sys import argv
import requests
from bs4 import BeautifulSoup

script, website = argv
file = "link_report.txt"

url_without_prefix = not website.startswith("http://") and not website.startswith("https://")
if url_without_prefix:
    website = "http://" + website
try:
    response = requests.get(website)
    html = BeautifulSoup(response.content, 'html.parser')
    links = html.findAll('a')
    openfile = open(file, 'w')
    openfile.truncate()
    for link in links:
        link_url = link['href']
        if link_url.startswith("http://") or link_url.startswith("https://"):
            response = requests.get(link_url)
            link_and_status_code = f"{link_url} - staus code: {response.status_code}"
            print (link_and_status_code)
            openfile.write(link_and_status_code + "\n")

    openfile.close()
    print(f"Report was saved in file {file}")
except Exception:
     print("Wrong url.")
