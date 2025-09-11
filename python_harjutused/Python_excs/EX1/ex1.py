# -----------------------1 strings (sone) ---------------------------------
# # Lisage faili ex1.py kaks muutujat first_name ja surname ja omistage nendele enda ees- ja perenimi
# lisage muujuja full_name, mille väärtus võrdub first_name + surname sõnade (vahel tühik)
# väljastage terminali muujuja full_name väärtus kasutades Python print() funktsiooni
# lisage muutuja full_name_search, mille väärtuseks on full_name kus kõik tähed on suured tähed (vajadusel otsi abi "string methods")
# väljastage terminali muujuja full_name_search väärtus kasutades Python print() funktsiooni

first_name = "Johannes"
surname = "Kauksi"
full_name = first_name + " " + surname
print(full_name)
full_name_search = full_name.upper()
print(full_name_search)
# --- IGNORE --- vahe on kas suur või väike täht. selleks et otsingu töötaksid muudetakse kõik
# tähed suurteks tähtedeks. Saame alati vaste. 

#-----------------------2 numbers (int ja float) ---------------------------------
#Lisage muutuja age ja omistage sellele täisarvuline väärtus
#Lisage muutuja height ja omistage sellele väärtus täpsusega kaks kohta peale koma
#Kasutades print ja format string funktsiooni väljastage Terminali tekst
#  "Mu vanus on VANUS ja pikkus on PIKKUS." kus tekstis muutujad VANUS ja 
# PIKKUS asendatakse muutuja väärtusega.
#Lisage muutuja hashed_name, mis võtab aluseks surname ja kus on asendatud kõik tähed 
# alates teisest tähest väikse nime esitähega.
#Lisage muutuja initials, kus on kokku liidetud ees- ja perenimest mõlemast kas esimesest tähte

age = 28
height = 1.71
print("Mu vanus on {} ja pikkus on {}.".format(age, height))
print(f"Mu vanus on {age} ja pikkus on {height}." + "teine viis") #teine viis
minu_nimi_viimane_taht = first_name[-1] 
minu_nimi_esimene_taht = first_name[0] 

print("minu nimi viimane täht" + minu_nimi_viimane_taht)
print("minu nimi viimane täht" + minu_nimi_esimene_taht)

minu_nimi_yks_koolon = first_name[1:] 
print("minu nimi peale esimest tähte" + minu_nimi_yks_koolon)

minu_nimi_koolon_yks = first_name[:1] 
print("minu nimi enne esimest tähte" + minu_nimi_koolon_yks)


hashed_name = surname[0] + (len(surname)-1)*surname[0].lower()
print(hashed_name)

initials = first_name[0] + surname[0]
print(initials)

print("vanus ja eesnimi" + age*first_name)