#Loo uus järjend girl_names mis sisaldab nimesid: Jaanika, Malle, Kersti, Ann, Mari, Kati
#Kasutades FOR tsüklit väljasta kõik järjendi nimed üks haaval terminali
#Kasutades FOR tsüklit väljasta järjendi kaks esimest nime terminali
#Kasutades FOR tsüklit väljasta järjendi teine kuni neljas nimi terminali
#Kasutades FOR tsüklit väljasta kõik järjendi elemendid üks haaval terminali alustades järjendi lõpust (viimasest elemendist)
#Kasutades FOR tsüklit ja tingimuslauset väljasta terminali nimed, mis algavad K tähega.

girl_names = ["Jaanika", "Malle", "Kersti", "Ann", "Mari", "Kati"]
for x in girl_names:
    print (x)

print("--------------------lahendus 1 (kaks esimest nime)----------------------------------------")

for i in range(2):
    print(girl_names[i])

print("------------------------lahendus 2 (kaks esimest nime)------------------------------------")

for name in girl_names[:2]:
    print(name)

print("------------------------teine kuni neljas------------------------------------")

for name in girl_names[1:4]:
    if name[:-1]:
        print(" ")
    print(name, end=",")

print("\n------------------------kõik elemendid lõpust------------------------------------")
for name in reversed(girl_names):
    print(name, end=" ")

print("\n------------------------alusta esimest elemendist ja trüki iga 2 välja------------------------")

print("paaris elemendiga indeksid")
for i in range(0, len(girl_names), 2):
    print(girl_names[i])

print("\n------------------------nimed mis algavad k tähega------------------------")
for name in girl_names:
    if name.startswith("K"):
        print(name)
#luua dictionary kus on võti m, ja loend milles on kõik nimed mis algavad m tähega
names_starting_with_m = { "m": [name for name in girl_names if name.lower().startswith("m")] }
print(names_starting_with_m)

sorted_names = {}

for name in girl_names:
    first_letter = name[0].lower()
    print("first_letter " + first_letter)
    if first_letter not in sorted_names:
        sorted_names[first_letter] = []
    sorted_names[first_letter].append(name)
print(f"esimesed tähed{sorted_names}")

