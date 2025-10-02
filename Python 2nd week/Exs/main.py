#Andmed tekstifailis
#Tekstifailist lugemine
#Loo fail nimega "request-log.txt"
#Lisa sinna käsitsi kolm rida teksti, kus iga uus rida algab reanumbriga.
#Loo tekstiline muutuja "file-content".
#Loe andmed tekstifailist loodud muutujasse.
#Väljasta "file-content" sisu terminali.
#Lisa uus tühi järjend "request-log-entries".
#Täienda programmikoodi, kus tekstifaili iga rida. pannakse eraldi tekstina loodud järjendisse .
#Väljasta terminali tekst "Logifailis on {x} rida."
#Väljasta järjendi sisu terminali nii et iga rea vahel oleks täiendav reavahetus.
#Tekstifaili kirjutamine
#Lisa faili nimega request-log.txt täiendavad 3 uut rida.
#Väljasta uuesti faili sisu terminali.
#Funktsioonide loomine
#Loo uus funkstioon "add_text", mis saab sisendidna faili nime ja lisatava teksti ning see tekst listatakse faili lõppu juurde.
#Loo uus funktsioon "return_last_3_rows", mis tagastab viimased 3 faili lisatud rida.
#Mida eelnevast ülesandest võiks eraldi funktsioonidesse paigutada, et koodi saaks korduvalt kasutada?


#Funktsioonide loomine
#Loo uus funkstioon "add_text", mis saab sisendidna faili nime ja lisatava teksti ning see tekst listatakse faili lõppu juurde.
#Loo uus funktsioon "return_last_3_rows", mis tagastab viimased 3 faili lisatud rida.
#Mida eelnevast ülesandest võiks eraldi funktsioonidesse paigutada, et koodi saaks korduvalt kasutada?

from file_functions import File_functions


def main():

    file_path =  "C:/Users/User/Desktop/AndmeTarkusGit/andmeTarkus-1/python_harjutused/Python_excs/ANALYSIS/input/request_log.txt"

    filecontent = ""

    with open(file_path, encoding='utf-8') as f:
        filecontent = f.read()

    request_log_entries = filecontent.splitlines()

    for line in request_log_entries:
        print(line)
    
    row_count = len(request_log_entries)
    print(f"Logifailis on {row_count} rida.")


    File_functions().add_line_to_file(file_path, "4. See on neljas rida.")

if __name__ == "__main__":
    main()