import urllib.request as urllibR
import bs4

url ='https://tv2.dk/'

tv2 = urllibR.urlopen(url)
print(tv2.read())
