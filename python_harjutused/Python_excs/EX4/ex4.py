#-----------Funkstioon väite tõesuse kontrollimiseks-----------------
#Loo fukstioon nimega is_adult, mis võtab parameetriks age täisarvu
#Lisa fingimuslasuse, mis kontrollib kui sisendparameeter on 18 või suurem, 
# siis väljastab tõenäärtuse True, vastasel juhul False
#Testi terminalis funktsiooni väärtust funktsiooni andes sisendiks erinevaid väärtusi
#Lisa funkstiooni kontroll, mis kontrollib kas muutuja on arv ja ei ole negatiivne arv. 
# Kui tuvastatakse viga siis tagastatab funktsioon False
#Testi terminalis funktsiooni väärtust andes funktsiooni sisendiks erinevaid väärtusi
#-----------------Loo tingimuslause, mis kasutab vanuse kontrollimiseks funkstiooni is_adult. ----------------
# Kui tõene siis tagastab terminali "Võib Valida" vastasel juhul "Ei või valida".
#-----------Funkstioon väärtuse olemasolu kontrollimiseks loendis-----------------
#Lisa loend eu_northen_country_codes sõnedega DK, EE, FI, IS, LT, LV, NO, SE
#Lisa funktsioon is_northen_country (mis võtab vastu 2 kohalise riigi koodi country_code) ja tagastab kas tõenäärtuse True kui riigi kood on loetelus. vastasel juhul tagastab False.
#Funktsioon peab tagastama alati väärtuse False, kui sisend ei ole kahetäheline string
#Testi terminalis funktsiooni väljundit andes funktsiooni sisendiks erinevaid väärtusi

def is_adult(age: int) -> bool:
    """Kontrollib kas vanus on 18 või suurem ja tagastab True või False"""
    if age is None or not isinstance(age, int) or age < 0:
        return False
    if age >= 18:
        return True
    else:
        return False
    #või lühemalt
    #return age >= 18

#testime funktsiooni
print(is_adult(20)) #True
print(is_adult(17)) #False
print(is_adult(18))# True
print(is_adult("mari")) #Vigased andmed
print(is_adult(-1))

eu_northen_country_codes = ["DK", "EE", "FI", "IS", "LT", "LV", "NO", "SE"]

def is_northen_country(country: str) -> bool:
    """Kontrollib, et sisend on 2-täheline string ja kas see on loendis (case-insensitive)."""
    if not isinstance(country, str) or len(country) != 2:
        return False
    return country in eu_northen_country_codes

#testime funktsiooni
print(is_northen_country("EE")) #True
print(is_northen_country("ee")) #True
print(is_northen_country("US")) #False
print(is_northen_country("E")) #False
print(is_northen_country(5)) #False
