# Webscraping-Python
## Summary
This repository unique US Census Bureau website links scraped from their website using Python.
## Getting Started
- Python 3
### Packages
- BeautifulSoup
- urllib
- re
- csv
## Steps
1. Open a Python program.
2. Using bs4, import the BeautifulSoup package. Also import the urllib, re, and csv libraries.
3. Create a variable and call the urllib.request.urlopen function. Insert the United States Census Bureau link provided (United States Census Bureau, n.d.) in the function and then use the .read() function.
4. Create a Beautiful Soup object and call the BeautifulSoup constructor, and pass in r using the ‘xlml’ parser.
5. Use the prettify function to add some structure and make it easy to read.
6. Create an empty list.
7. Create a for loop for links in soup, call the find all method and then pass in a string that reads “a”. For each of the “a” tags we want to append the links that have an attribute of ‘href’ to the empty list.
## References
