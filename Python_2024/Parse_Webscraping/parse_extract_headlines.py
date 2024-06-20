import urllib.request as urllibR
from bs4 import BeautifulSoup

url = 'https://tv2.dk/'

try:
    tv2 = urllibR.urlopen(url)  # Open the URL
    html_content = tv2.read()  # Read the HTML content
    tv2BS = BeautifulSoup(html_content, 'html.parser')  # Parse the HTML content

    # Extract headlines (assuming they are in <h2> tags with a class 'headline')
    headlines = tv2BS.find_all('h2', class_='headline')
    for headline in headlines:
        print(headline.text)  # Print the text content of each headline
except Exception as e:
    print(f'An error occurred: {e}')  # Handle exceptions
