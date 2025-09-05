#----------------Peamised Python andmestruktuurid------------------------
#Loo uus fail ex2.py
#--------------------------List (Sõnede järjend)----------------------------
#Loo uus järjend boys_names mis sisaldab nimesid: Ain, Peeter, Kusti, Karl
#Lisa loodud järjendisse boys_names täiendav nimi "Margus"
#Loo uus järjend girl_names mis sisaldab nimesid: Jaanika, Malle, Kersti, Ann
#Loo uus tühi järjend names
#Lisa sinna elemendid nii boys_names ja ka girl_names kõik elemendid
#Moodusta uus järjend names_sorted, mis sisaldab nimesid sorteeritud tähestiku järjekorras.
##Väljasta Terminali järjend names_sorted
#Väljasta Terminali mis väärtused tagastavad meetodid max(), min() järjendi girl_names puhul
#Väljasta Terminali mitu elementi on järjendis names_sorted esimene
#Väljasta Terminali järjendi names_sorted esimene element
#Väljasta Terminali järjendi names_sorted viimane element
#Lisa järjendisse boys_names_reverse järjend boys_names pööratud järjekorras
#Väljasta Terminali järjend boys_names_reverse
#--------------------Set (Hulk)-----------------------------
#Loo järjend transaction_customer_id
#Lisa sinna väärtused 1, 2, 5, 2, 4, 8
#Trüki loodud järjend välja terminali
##Loo hulk active_customers kuhu lisad transaction_customer_id väärtused
#Trüki loodud hulk välja terminali
#Loo hulk all_customers väärtustega 1,2,3,4,5,6,7,8,9,10. Väärtuste loomiseks kasuta funksiooni range()
#Loo hulk passive_customers kuhu lisad kõik kliendikoodid, mis ei ole tehinguid teinud.
#--------------------------Dictionary (Sõnastik)-----------------------
#Loo uus sõnastik my_company_data, mis sisaldab järgmist infot
#id on 12345678
##name: "Best Analytics Ever"
#mille sees on omakoda sõnastik year_sales väärtustega
#2023: 12000.00
#2024: 15000.00
#Väljasta Terminali loodud sõnastik
#Väljasta Terminali my_company_data nimetus
#Väljasta Terminali my_company_data 2023 aasta müügi väärtus kujul "Ettevõtte {Ettevõtte nimi} müük aastal 2023 oli {väärtus} eurot."
#Muutke ettevõtte nimi ära
#Lisage my_company_data Järjend offices väärtustega Tallinn, Tartu, Helsinki
#Väljasta Terminali muudetud sõnastik
#----------------------------------Tuple (Ennik)----------------------------
#Loo uus ennik popular_boys_names, mis sisaldab nimesid Peeter, Karl
#Väljastage ennik popular_boys_names terminali
#Väljastage enniku esimene elemeny popular_boys_names terminali
#Loo uus ennik random_data, mis sisaldab väärtusi: Viis, 5, 5.0
#Väljastage ennik random_data terminali

#--------------------------List (Sõnede järjend)----------------------------

boys_names = ["Ain", "Peeter", "Kusti", "Karl"]
additional_name = "Margus"
boys_names.append(additional_name)
print(boys_names)
girl_names = ["Jaanika", "Malle", "Kersti", "Ann"]
names = []
names = boys_names + girl_names
print("names " + str(names))
names_sorted = sorted(names)
print("names_sorted " + str(names_sorted))
print("max " + max(girl_names))
print("min " + min(girl_names))
lenght_of_names_sorted = len(names_sorted)
print("names_sorted length " + str(lenght_of_names_sorted))
print("names_sorted first element " + names_sorted[0])
print("names_sorted last element " + names_sorted[-1])
boys_names_reverse = boys_names[::-1]
print(boys_names_reverse)

#--------------------Set (Hulk)-----------------------------

transaction_customer_id = [1, 2, 5, 2, 4, 8]
print("transaction_customer_id " + str(transaction_customer_id))
print("pikkus customeril " + str(len(transaction_customer_id)))
active_customers = set(transaction_customer_id)
print("active_customers " + str(active_customers)) #tagastab ainult unikaalsed väärtused
all_customers = set(range(1, 11)) #range jätab viimase numbri välja
print("all customers", all_customers)
passive_customers = all_customers - active_customers
intersection_customers = all_customers & active_customers
print("passive_customers " + str(passive_customers))
print("intersection_customers " + str(intersection_customers))

#--------------------------Dictionary (Sõnastik)-----------------------
my_company_data = {
    "id": 12345678
    ,"name": "Best Analytics Ever"
    ,"year_sales": {
        2023: 12000.00,
        2024: 15000.00,
        2025: 18000.00
    }
}
print("my_company_data " + str(my_company_data))
print("my_company_data name " + my_company_data["name"])
my_company_data["year_sales"][2023] = 888000.00
my_company_data["year_sales"][2025] = 20000.00
print("my_company_data 2023 sales " + str(my_company_data["year_sales"][2023]))
my_company_data["name"] = "Johannes Analytics"
my_company_data["offices"] = ["Tallinn", "Tartu", "Helsinki"]
print("my_company_data " + str(my_company_data))

#----------------------------------Tuple (Ennik)----------------------------
#andmestik, mida ei saa muuta
popular_boys_names = ("Peeter", "Karl")
print("popular bys names " + str(popular_boys_names))
print("popular bys names first element " + popular_boys_names[0])
random_data = ("Viis", 5, 5.0)
print("random_data " + str(random_data))