# Target
# Library Dependency:

**Re** : A regular expression is a sequence of characters that define a search pattern. Usually such patterns are used by string-searching algorithms for "find" or "find and replace" operations on strings, or for input validation.

**scrapy** : Scrapy uses Spiders to define how a site (or a bunch of sites) should be scraped for information. Scrapy lets us determine how we want the spider to crawl, what information we want to extract, and how we can extract it. Specifically, Spiders are Python classes where we’ll put all of our custom logic and behavior.

**json**:  Is a way to store information in an organized, easy-to-access manner. In a nutshell, it gives us a human-readable collection of data that we can access in a really logical manner.

# How it's work:

Open a CMD and type command which given below. 

scrapy crawl target -a url=<URL>
  
# Output
{
'url': 'https://www.target.com/p/levi-s-men-s-512-slim-taper-fit-jeans/-/A-79691588', 
'tcin': '79645710', 
'upc': '194576178246', 
'price': 59.99, 
'currency': 'USD',
 'title': "Levi's® Men's 512™ Slim Taper Fit Jeans", 
'description': "These Jeans that are slim from the hip, and narrow from the knee down to ankle. Slimmer leg than the Levi's® 511™. Right amount of stretch for all-day comfort. The narrow leg gives a more tailored look. In 1873, Levi's ® invented the blue jean. What started as a piece of clothing for the American worker quickly became an icon of American style around the globe. And every Levi's ® style is crafted with the same high standard of craftsmanship and quality they've always been known for. Worn by everyone from miners and rebels to rockstars, Levi's ® aren't just made to be worn, but to be lived in, too.",
 'specs': {
'Size': '28x30', 
'Sizing': 'Mens',
 'Material': '87% Cotton, 11% Polyester, 2% Elastane', 
'Garment Length': 'Full', 
'Closure Style': 'Fly Button and Zipper', 
'Inseam Length': '30 Inches', 
'Rise': 'Low Rise', 
'Fit': 'Taper', 
'Features': 'Dark Wash', 
'Pockets': 'Front Coin Pocket, Back Patch Pocket, Front Scoop Pocket', 
'Care and Cleaning': 'Machine Wash & Tumble Dry'
}
} 

