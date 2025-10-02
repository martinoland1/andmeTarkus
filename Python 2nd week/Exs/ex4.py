# paigalda pip install tools.api_request

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

# url = "https://demo-datahub.rik.ee/api/v1/meta/classifications"

url_riik = 'https://api.worldbank.org/v2/countries/EST/?format=json'
url_rahvastik_ = 'https://api.worldbank.org/v2/country/EST/indicator/SP.POP.TOTL?format=json'
url_daamid = 'https://api.worldbank.org/v2/country/EST/indicator/SP.POP.TOTL.FE.IN?format=json'

response = requests.get(url_rahvastik_)
data = response.json()

women_response = requests.get(url_daamid)
data_women = women_response.json()

# json dumps muudab väljundi terminalis loetavaks
print(json.dumps(data, indent=2, ensure_ascii=False))
print(json.dumps(data_women, indent=2, ensure_ascii=False))

values = {'year': [], 'population': [], 'women': []}

# {"year": ["2021", "2020", "2019", ...], "population": [1331057, 1326535, 1324820, ...]}

for item in data[1]:
    values['year'].append(item['date'])
    values['population'].append(item['value'])

for item in data_women[1]:
    values['women'].append(item['value'])

print(json.dumps(values, indent=2, ensure_ascii=False))

df = pd.DataFrame(values)
df = df.sort_values(by='year')
df_women = pd.DataFrame(values)
df['men'] = df['population'] - df['women']


# väljastan esimesed read
print(df.head())

df.plot(
    x='year',
    y=['population', 'women' , 'men'],
    kind='line',
    marker='o',
    title='Eesti rahvaarv aastatel 1960–2021',
    xlabel='Aasta',
    ylabel='Inimeste arv'
)
plt.ylim(bottom = 0)  # Alusta y-telge nullist

plt.savefig('python_harjutused/Python_excs/ANALYSIS/output/rahvastik.png')

plt.show()

print(df)

response_df = pd.json_normalize(data)
print(response_df)