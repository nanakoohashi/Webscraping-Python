#!/usr/bin/env python
# coding: utf-8

# # Python Assessment

# In[142]:


from bs4 import BeautifulSoup
import urllib
import re
import csv 


# In[143]:


r = urllib.request.urlopen('https://www.census.gov/programs-surveys/popest.html').read()
soup = BeautifulSoup(r, "lxml")
type(soup)


# ## Scraping a webpage and saving your results

# In[144]:


print(soup.prettify()[:100])


# In[145]:


# Gather all the hrefs for the a tags
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
print(links)


# In[146]:


# Remove "None" values, "/" values, and if starts with "#"
print(len(links))
for i in reversed(range(len(links))):
    l = links[i]
    if l == None:
        links.pop(i)
    elif l == "/":
        links.pop(i)
    elif l[:1] == "#":
        links.pop(i)
print(len(links))


# In[147]:


# Turn relative links into absolute links
for i in range(len(links)):
    l = links[i]
    if l[:1] == "/":
        links[i] = "https://www.census.gov"+l
        print(l, "-->", links[i])


# In[148]:


# Strip https://, http://, and trailing backslashes from list 
for i in range(len(http_links)):
    l = http_links[i]
    if l[:8] == "https://":
        http_links[i] = l[8:]
        
    l = http_links[i]
    if l[:7] == "http://":
        http_links[i] = l[7:]
        
    l = http_links[i]
    if l[-1:] == "/":
        http_links[i] = l[:len(l)-1]
print(http_links)


# In[149]:


# remove duplicates
unique_links = []
for l in http_links:
    if not l in unique_links:
        unique_links.append(l)
print(len(http_links))
print(len(unique_links))
unique_links.sort()


# In[150]:


# Check for links to same page
for l in unique_links:
    if 'www.census.gov/programs-surveys/popest.html' in l:
        print(l)


# In[151]:


for l in unique_links:
    print(l)


# In[152]:


with open('unique_links.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(unique_links)


# In[ ]:




