# lae andmed äriregsitrist
import pandas as pd

xml_path = r"C:\Users\User\Desktop\AndmeTarkusGit\andmeTarkus-1\python_harjutused\Python_excs\ANALYSIS\input\ettevotja_rekvisiidid_lihtandmed.xml"

# loe xml andmed DataFrame'i
df = pd.read_xml(xml_path, xpath=".//ettevotjad")
print(df.info())