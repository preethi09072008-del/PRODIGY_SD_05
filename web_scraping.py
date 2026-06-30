import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Check request status
if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    # Find all book containers
    for item in soup.find_all("article", class_="product_pod"):

        title = item.h3.a["title"]
        price = item.find("p", class_="price_color").text
        availability = item.find("p", class_="instock availability").text.strip()

        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    # Save data into CSV
    df = pd.DataFrame(books)
    df.to_csv("books.csv", index=False)

    print("Data scraped successfully!")
    print("Saved as books.csv")

else:
    print("Failed to retrieve website.")
