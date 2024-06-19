import urllib.request as urllibR


url ='https://tv2.dk/'

tv2BS = bs4.BeautifulSoup(tv2.read())
tv2 = urllibR.urlopen(url)

print(tv2.read())
