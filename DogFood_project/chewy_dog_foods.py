## Script to Pull Dog Foods from Chewy.com
import os
import requests
from bs4 import BeautifulSoup
import re

#from web_scraper import simple_get


user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'

# Get html data from Chewy.com
raw_html = requests.get('https://www.chewy.com/b/food-332',
                         auth = ('user', 'pass'),
                         headers = {'User-Agent':user_agent})

# Extract str html from bytearray
html_content = raw_html.text

# Write html data to file to look at it
html_out = open("chewy_foods.html", "w") # works for str objects
#html_out = open("chewy_foods.html", "wb") # works for 'bytes-like' objects
html_out.write(html_content)
html_out.close()
os.getcwd() # directory it went to

# Get Dog Food Brands using Beautiful Soup
html = BeautifulSoup(html_content, features = 'html.parser')
test_html = html.contents[2]

# Returns catagories, including brand
categories = html.find_all('h5', text=False)
test_html.find_all('h5') # returns the same as above
html.find_all('h5', text=False)[1].text
brand_head = test_html.find_all('h5')[1]
brand_head.text # returns 'Brand'

# Remove html tags and write content to file
text = html.get_text()
text_out = open("tagless_text.txt", "w")
text_out.write(text)
text_out.close()

# Extract brand names from text file
# First get rid of whitespace
with open("tagless_text.txt", 'r') as fh:
    lines = fh.readlines()
    #clean_lines = [line.strip() for line in lines if line.strip()]
    clean_lines = []
    for line in lines:
        if line.strip():
            clean = line.strip()
            clean_lines.append(clean)
print(clean_lines)

# Re-write text file without whitespace
with open("Outfile.txt", 'a') as fh:
    for c in clean_lines:
        fh.write("{}\n".format(c))

# Find line with 'Brand' at the beginning as the start
# Find line with 'Food Form' at the beginng as the end
start = html.find_all('h5', text=False)[1].text
end = html.find_all('h5', text=False)[2].text
with open("Outfile.txt", 'r') as fh:
    lines = fh.readlines()
    for i in range(len(lines)):
        if lines[i].startswith(start):
            print(i) #1222
        if lines[i].startswith(end):
            print(i) #1404

# Write Dog Food Brands to File
# with open("Dog_food_brands.txt", "w") as fh:
#     for i in lines[1222:1404]:
#         fh.write("{}\n".format(i))
#
# # List Stripping examples
# testl = ["t     t", "Hi\n", "Shutup\r", "\t\t\t\tdicks"]
# newl = []
# for t in testl:
#     x = t.strip().replace(" ", "").replace("t", "a")
#     newl.append(x)
#
# newm = [t.strip().replace(" ","").replace("t","a") for t in testl]
# print(newl)
# print(newm)


# Working on extracting brands from html tags -- revisit later
#allFilters = html.find_all(class_ = "filter-section")
#allFilters = test_html.find_all(class_ = "filter-section").
#print(html.find_all("li"))

# List food names
# https://www.chewy.com/s?rh=c%3A288%2Cc%3A332%2Cbrand_facet%3ATiki+Dog
# https://www.chewy.com/s?rh=c%3A288%2Cc%3A332%2Cbrand_facet%3AAdirondack
# https://www.chewy.com/s?rh=c%3A288%2Cc%3A332%2Cbrand_facet%3ABlue+Wilderness
# Individual Food page
# https://www.chewy.com/blue-buffalo-wilderness-chicken/dp/32052
# Ingredients under
# Ingredients-title between <p><\p>

# for i, li in enumerate(html.select('li')):
#     print(i, li.text) # interesting but returns too much, includes some ingredients
#
# for i, li in enumerate(html.select('brand_facet%3')):
#     print(i, li.text) # interesting but returns too much, includes some ingredients
#
# # Try writing lines that have brand and number
# food_brands = re.search('brand_facet%3(.+?)</li>', html_content)
# if food_brands:
#     found = food_brands.group(1) # didn't return anything
#
# # Try matching line before brand name and number and printing the one after
# food_brands = re.search('brand_facet%3', html_content)
# if food_brands:
#     found = food_brands.group(1) # didn't return anything
#
# for i in html_content.split(\n):
#     if "brand_facet%3" in i:
#         print(next(html_content, '').strip())