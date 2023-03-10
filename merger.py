import pandas as pd

bright_stars = pd.read_csv("PRO-Stars-Dataset-CSVs-main/bright_stars.csv")
dwarf_stars = pd.read_csv("/PRO-Stars-Dataset-CSVs-main/dwarf_stars.csv")

dwarf_stars.drop(
    columns=["Luminosity"],
    inplace=True
)
dwarf_stars.head()

headers = [
    "id",
    "Star_name",
    "Distance",
    "Mass",
    "Radius"
]

all_stars_df = pd.DataFrame(columns=headers)
all_stars_df = pd.merge(bright_stars, dwarf_stars)
all_stars_df.to_csv("final_database.csv")

new_web_df = pd.read_csv('/content/PRO-NASA-Exoplanet-Scraped-Data/PSCompPars.csv')
new_web_df["pl_name"] = new_web_df["pl_name"].str.lower()
new_web_df = new_web_df.sort_values("pl_name")

merge_planets_df = pd.merge(all_stars_df, new_web_df, on = "id")
merge_planets_df.columns
merge_planets_df.to_csv("final_merged_planet_database.csv")
