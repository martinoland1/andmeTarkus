import requests
import pandas as pd

url = "https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php"
response = requests.get(url)
xml_content = response.content
df = pd.read_xml(xml_content, xpath=".//place")
print(df.head())

#kõige madalam temperatuur ja kõige kõrgem temperatuur

min_temp_row = df[df['tempmin'] == df['tempmin'].min()]
max_temp_row = df[df['tempmax'] == df['tempmax'].max()]
print("Kõige madalam temperatuur:")
print(min_temp_row)
print("Kõige kõrgem temperatuur:")
print(max_temp_row)
