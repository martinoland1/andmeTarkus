# Elektrihind rest teenusest

from zoneinfo import ZoneInfo
from datetime import datetime
import requests
import json
now = datetime.now()


# elering_url = "https://dashboard.elering.ee/api/nps/price?start=2025-01-01T00%3A00%3A01.999Z&end=2025-06-30T23%3A59%3A59.999Z"

# url ilma parameetriteta
elering_url = "https://dashboard.elering.ee/api/nps/price"

path = r"elektrihind\output_"
# Elektrihind rest teenusest

def get_price(start: str, end: str) -> dict:
    """Hangi elektrihind antud ajavahemikus. Tagasta JSON andmed."""
    url = f"https://dashboard.elering.ee/api/nps/price?start={start}&end={end}"
    response = requests.get(url)
    # võtan päringust vaid "Eesti" andmed
    data = response.json()['data']['ee']
    data_with_dates = []
    for item in data:
        item['datetime'] = convert_timestamp(
            item['timestamp']).strftime("%Y-%m-%d %H:%M")
        data_with_dates.append(item)
    return {"data": data_with_dates}


def save_json(data: dict, filename: str):
    """Salvesta andmed faili JSON formaadis."""
    with open(path + filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def convert_timestamp(ts: int) -> datetime:
    """Teisenda unix timestamp (sekundites) datetime objektiks Europe/Tallinn ajavööndis."""
    tz = ZoneInfo("Europe/Tallinn")
    return datetime.fromtimestamp(ts, tz)

# Kontrollime kas fail olemas, siis lae failist, muuljuhul tee päring ja salvesta faili

def load_or_fetch_data(start: str, end: str, filename: str) -> dict:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        data = get_price(start, end)
        save_json(data, filename)
        return data

# Näide kasutusest:
# data = get_price("2025-01-01T00:00:01.999Z", "2025-06-30T23:59:59.999Z")
# save_json(data, "elering_price.json")

#võtame kolme aasta,kuu,päeva andmed
def month_end_date(year: int, month: int) -> int:
    """Tagasta kuu viimane päev antud aastal ja kuul."""
    if month == 2:
        # Liigaasta kontroll
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

for year in range(2024, 2026):
    for month in range(1, 13):
        # ära mine tulevikku (lubatud kuni eelmise kuuni)
        if (year > now.year) or (year == now.year and month >= now.month):
            break

        last_day = month_end_date(year, month)
        start = f"{year}-{month:02d}-01T00:00:01.999Z"
        end   = f"{year}-{month:02d}-{last_day:02d}T23:59:59.999Z"

        data = get_price(start, end)
        save_json(data, f"elering_price_{year}_{month:02d}.json")
