#Moodusta eraldi loend names_starting_with_a kuhu lisad a tähega algavad nimed loendist names_sorted 
# (kasuta list comprehensionit)
#Moodusta eraldi loend names_containing_a kuhu lisad a tähte sisaldavad nimed loendist 
# names_sorted (kasuta list comprehensionit)
girl_names = ["Jaanika", "Malle", "Kersti", "Ann"]

names_starting_with_a = [name for name in girl_names if "a" in name]

print("names_starting_with_a " + str(names_starting_with_a))

names_starting_with_a = [name for name in girl_names if name.startswith("A")]
print("names_starting_with_a " + str(names_starting_with_a))


#nimed mis on lühemad kui 4 tähte
names_shorter_than_4 = [name for name in girl_names if len(name) < 4]
print("names_shorter_than_4 " + str(names_shorter_than_4))
