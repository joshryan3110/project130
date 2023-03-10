from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
star_data = []

def scrape_more_data(hyperlink):
    try:
        page.requests.get(hyperlink)
        soup = BeautifulSoup(START_URL.page_source, "html.parser")
        temp_list = []
        for tr_tag in soup.find_all("tr",attrs ={"class"} ):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                td_tag.strip()
        star_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

headers = ["star_name", "radius", "mass", "distance"]
dwarf_stars = pd.DataFrame(star_data, columns=headers)
dwarf_stars.to_csv("dward_star_data.csv",index=True,index_label="id")


