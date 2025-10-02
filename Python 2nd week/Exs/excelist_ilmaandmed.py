import pandas as pd

excel_path = r"C:\Users\User\Desktop\AndmeTarkusGit\andmeTarkus-1\python_harjutused\Python_excs\ANALYSIS\input\Tallinn-Harku-2004-2024.xlsx"

# loe sisse ja vaheta kuupäeva veeru nimi vastavalt oma failile
data = pd.read_excel(excel_path, skiprows=2)

df_2024 = data[data['Aasta'] == 2024]

#salvesta dataframe uude faili
df_2024.to_csv(r"C:\Users\User\Desktop\AndmeTarkusGit\andmeTarkus-1\python_harjutused\Python_excs\ANALYSIS\output\Tallinn-Harku-CSV-2024.csv", index=False)

