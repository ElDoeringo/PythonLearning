import urllib.request as urllibR
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url = 'https://tv2.dk/'

try:
    tv2 = urllibR.urlopen(url)  # Try to open the URL
    html_content = tv2.read()  # Read the HTML content
    tv2BS = BeautifulSoup(html_content, 'html.parser')  # Parse the HTML content
    print(tv2BS.prettify())  # Print the parsed HTML content
except HTTPError as e:
    print(f'HTTP error occurred: {e.code} {e.reason}')  # Handle HTTP errors
except URLError as e:
    print(f'Failed to reach the server: {e.reason}')  # Handle URL errors
except Exception as e:
    print(f'An error occurred: {e}')  # Handle other exceptions
