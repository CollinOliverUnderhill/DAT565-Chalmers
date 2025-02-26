from bs4 import BeautifulSoup
import pandas as pd
import re
import os

html_folder_path = "C:/Users/xiach/OneDrive/桌面/kungalv_slutpriser"
def parse_ad(ad_html):
    date_text = ad_html.find("span", class_="hcl-label--sold-at")
    date_of_sale = date_text.get_text(strip=True) if date_text else None
    address_tag = ad_html.find("h2", class_="sold-property-listing__heading")
    address = address_tag.get_text(strip=True) if address_tag else None
    location_tag = ad_html.find(string=re.compile(r"Kungälvs kommun"))
    location = location_tag.replace("\n", "").replace("\r", "").strip() if location_tag else None
    area_rooms_text = ad_html.find("div", class_="sold-property-listing__subheading")
    if area_rooms_text:
        area_rooms_str = area_rooms_text.get_text(strip=True)
        areas = re.findall(r"\d+", area_rooms_str)
        boarea = areas[0] if len(areas) > 0 else None
        biarea = areas[1] if len(areas) > 1 else None
        total_area = f"{boarea}+{biarea} m²" if boarea and biarea else (f"{boarea} m²" if boarea else None)
        rooms = re.search(r"(\d+)\s+rum", area_rooms_str)
        rooms = rooms.group(1) if rooms else None
    else:
        boarea, biarea, total_area, rooms = None, None, None, None
    plot_area_tag = ad_html.find("div", class_="sold-property-listing__land-area")
    plot_area = re.search(r"(\d+)\s*m²", plot_area_tag.get_text(strip=True)) if plot_area_tag else None
    plot_area = plot_area.group(1) if plot_area else None
    closing_price_tag = ad_html.find("span", class_="hcl-text--medium")
    if closing_price_tag:
        closing_price_matches = re.findall(r"\d+", closing_price_tag.get_text().replace(" ", ""))
        closing_price = "".join(closing_price_matches) if closing_price_matches else None
    else:
        closing_price = None
    return {
        "date_of_sale": date_of_sale,
        "address": address,
        "location": location,
        "total_area": total_area,
        "rooms": rooms,
        "plot_area": plot_area,
        "closing_price": closing_price
    }
data = []
for filename in os.listdir(html_folder_path):
    file_path = os.path.join(html_folder_path, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        ads = soup.find_all("li", class_="sold-results__normal-hit")
        for ad in ads:
            ad_data = parse_ad(ad)
            if any(ad_data.values()):
                data.append(ad_data)
df = pd.DataFrame(data)
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df.dropna(how='all', inplace=True)
df.replace("", pd.NA, inplace=True)
df.dropna(how='all', inplace=True)
output_excel_path = "C:/Users/xiach/OneDrive/桌面/house_prices.xlsx"
with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
    df.to_excel(writer, index=False)

print(f"Data saved to {output_excel_path}")
