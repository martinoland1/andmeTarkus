#Andmed CSV failis
#Lae andmed failist CustomerTable.csv
#Väljasta laetud andmed terminali
#Täienda programmi koodi ja salvesta laetud andmeted järjendisse "customers", 
# mis sisaldab iga kliendi andmeid eraldi ennikus (tuple).
#Esimene tulpe sisaldab päise andmeid ja järgmised elemendid kliendi andmeid
#Väljasta järjend "customers" sisu terminali.
#Andmete salvestamine SQL insert käsuna
#Salvesta järjend "customers" andmed faili insert_customers.sql järgnevalt
#Faili esimene rida on "INSERT INTO customers"
#Faili teine rida on "VALUES {"customers" loendi esimene element}"
#Järmine rida VALUES
#Edasi eraldi ridadele "customers" elemendid.
#Iga andmerea lõppu tuleb lisada koma ja viimase andmerea lõppu semikoolon.
#Veendu, et SQL käsk oleks korrektne (sulud jms).
#Funktioonide täiendamine
#Mida eelnevast võiks lahendada funktsioonidena?

# andmed CSV failis

import csv

data_from_csv = []

with open ("C:/Users/User/Desktop/AndmeTarkusGit/andmeTarkus-1/python_harjutused/Python_excs/ANALYSIS/input/CustomerTable.csv", encoding='utf-8') as file:
    #tekita reader objekt
    reader = csv.reader(file)
    # teisenda reader objekt listiks
    data_from_csv = list(reader)
    print(data_from_csv)
print(data_from_csv)

#esimene rida on päis
insert_statement = "INSERT INTO customers"

#instert_statement + veergude nimed
# insert_statement += pikalt kijrutades insert statement = insert_statement + ....
insert_statement += f"\n ({','.join(data_from_csv[0])}) \nVALUES  "

for row in data_from_csv[1:-1]:
    insert_statement += f"\n ({', '.join(row)}),"
#viimase rea lõppu semikoolon
insert_statement += f"\n ({', '.join(data_from_csv[-1])});"
print(insert_statement)