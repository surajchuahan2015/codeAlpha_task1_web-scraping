import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = []

for book in soup.select(".product_pod"):

    title = book.h3.a["title"]
    price = book.select_one(".price_color").text
    rating = book.select_one(".star-rating")["class"][1]

    data.append([title, price, rating])

with open("books.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Book Name", "Price", "Rating"])
    writer.writerows(data)

print("Scraping completed!")
print("Data saved in books.csv")