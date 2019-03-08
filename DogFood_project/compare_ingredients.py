## Script to Pull Ingredient Lists from Pages
import os
import requests
from bs4 import BeautifulSoup
import re

# Set up scraper
# Get html using requests.get and parse html with BeautifulSoup
def scrape(url):
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    # Get html data from Chewy.com
    raw_html = requests.get(url,
                            auth=('user', 'pass'),
                            headers={'User-Agent': user_agent})
    html = BeautifulSoup(raw_html.text, features = 'html.parser')
    return html

# def clean_ws(list):
#     '''This separated every letter for some reason'''
#     clean_lines = []
#     for i in list:
#         if i.strip():
#             clean = i.strip()
#             clean_lines.append(clean)
#     return clean_lines

def ingredients(html):
    soup = html.find('div', {'class': 'product-info-description'}).get_text()
    start = soup.find("Ingredients:")
    ingred = soup[start + len("Ingredients:"):]
    ingred_clean = ingred[:ingred.find('.')]
    return ingred_clean.strip() # no whitespace

# Pull from Costco
newfood = scrape('https://www.costco.com/Kirkland-Signature-Puppy-Formula-Chicken%2C-Rice-and-Vegetable-Dog-Food-20-lb..product.100343452.html')
oldfood = scrape('https://www.costco.com/Kirkland-Signature-Natures-Domain-Puppy-Formula-Chicken-&-Pea-Dog-Food-20-lb..product.100354281.html')

# Extract Ingredients
new_ingred = ingredients(newfood)
old_ingred = ingredients(oldfood)

# Put Ingredients in Sets
Kirkland_Signature = set([x.strip() for x in new_ingred.split(',')])
Natures_domain = set([x.strip() for x in old_ingred.split(',')])

# Compare Kirkland Signature Puppy (new) and Nature's Domain Puppy (old)
n_kirk = len(Kirkland_Signature)
n_nat = len(Natures_domain)
shared = Kirkland_Signature & Natures_domain
nat_unqiue = Natures_domain - Kirkland_Signature
kirk_unique = Kirkland_Signature - Natures_domain

print('\nOur poor puppy Apollo developed persistent diarrhea shortly after coming home with us.\n'
      'We had switched him to Costco\'s Kirkland Signature from Nature\'s Domain puppy food \n'
      'because our Costco didn\'t carry Nature\'s Domain. After a month-long round of antibiotics\n'
      'with no visible improvement, I decided to look into Apollo\'s diet. \n\n'
      'Kirkland Signature Puppy Formula and Nature\'s Domain Puppy formula are both Costco brand \n'
      'dog foods made with chicken. Both dog foods are similar in quality and share the same major \n'
      'protein source, which is usually the cause of gastric upset and sensitivity. Once we switched \n'
      'Apollo back to his original formula, Nature\'s Domain, his diarrhea cleared up and his elimination\n'
      'has been normal ever since.\n\n'
      'While unfortunate for Apollo, this gives us an opportunity to identify the ingredients in Kirkland\n'
      'Signature Puppy Formula that might trigger his gastric upset. Here I compare the two foods:\n\n\n'
      'Kirkland Signature contains {} ingredients, while Nature\'s Domain contains {} ingredients.\n\n'
      'Both foods share the following ingredients: {}\n\n'
      'Nature\'s Domain contains {}, \nwhile Kirkland Signature does not.\n\n'
      'Kirkland Signature contains {}, \nwhile Nature\'s Domain does not.\n\n\n'
      'With some additional information, namely that Apollo\'s diarrhea worsened on a bland diet of chicken\n'
      'and rice, we can conclude that grains, including barley and brown rice, might have triggered Apollo\'s'
      'bouts of diarrhea.'.format(n_kirk, n_nat, shared, nat_unqiue, kirk_unique))



# # Check html
# # Write html data to file to look at it
# html_out = open("natures_domain.html", "w") # works for str objects
# #html_out = open("chewy_foods.html", "wb") # works for 'bytes-like' objects
# html_out.write(oldfood)
# html_out.close()