from bs4 import BeautifulSoup
import time
import pandas as pd

scrapped_data = []
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

def scrape():
    soup = BeautifulSoup(START_URL.page_source, "html.parser")
    bright_star_table = soup.find("table",attrs={"class","wikitable"})
    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")
        print(table_cols)
        temp_list = []

        for col_data in table_cols:
            print(col_data.text)
            data = col_data.text.strip()
            print(data)
            temp_list.append(data)

        scrapped_data.append(temp_list)

scrape()

stars_data =[]

for i in range(0, len(scrapped_data)):
    star_names = scrapped_data[i][1]
    distance = scrapped_data[i][3]
    mass = scrapped_data[i][5]
    radius = scrapped_data[i][6]
    lum = scrapped_data[i][7]
    required_data = [star_names,distance,mass,radius,lum]
    stars_data.append(required_data)

headers = ["Star_name","Distance","Mass","Radius","Luminosity"]
star_df_1 = pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv("scrapped_data.csv", index=True, index_label="id")