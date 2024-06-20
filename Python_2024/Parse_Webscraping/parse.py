import urllib.request as urllibR  # Import the urllib.request module and alias it as urllibR for handling URL requests
from bs4 import BeautifulSoup  # Import BeautifulSoup from the bs4 library for parsing HTML

# Define the URL to be accessed
url = 'https://tv2.dk/'

# Open the URL and read the response
tv2 = urllibR.urlopen(url)  # Open the URL and get the response object

# Read the HTML content from the response
html_content = tv2.read()  # Read the HTML content from the response object

# Parse the HTML content using BeautifulSoup
tv2BS = BeautifulSoup(html_content, 'html.parser')  # Parse the HTML content with BeautifulSoup

# Print the parsed HTML content
print(tv2BS.prettify())  # Print the parsed HTML content in a prettified format

