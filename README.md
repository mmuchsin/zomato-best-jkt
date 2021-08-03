# Scrap Best Restaurant in Jakarta

A Scrapy project to scrape restaurant information from Zomato. Only best restaurant information from jakarta have been scraped.

## Data Description

**column_name** | **contain** 
-------------|------------------
url          | the url of the restaurant in the zomato website
address      | the address of the restaurant in Bengaluru
name         | the name of the restaurant
online_order | whether online ordering is available in the restaurant or not
book_table   | table book option available or not
rate         | the overall rating of the restaurant out of 5
votes        | total number of rating for the restaurant as of the above mentioned date
phone        | the phone number of the restaurant
location     | the neighborhood in which the restaurant is located
rest_type    | restaurant type
dish_liked   | dishes people liked in the restaurant
cuisines     | food styles, separated by comma
approx_cost (for two people) | contains the approximate cost of meal for two people
reviews_list | list of tuples containing reviews for the restaurant, each tuple
menu_item    | list of menus available in the restaurant
listed_in (type)    | type of meal
listed_in (city)   | the neighborhood in which the restaurant is listed