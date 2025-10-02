import pandas as pd

file = (r"python_harjutused\Python_excs\ANALYSIS\input\BudgetPivot.xlsx")

data = pd.read_excel(file)
data_dict = data.to_dict(orient="records")
print(data)
print(data_dict)

file_csv = (r"python_harjutused\Python_excs\ANALYSIS\input\BudgetPivot.csv")
data2 = pd.read_csv(file_csv)