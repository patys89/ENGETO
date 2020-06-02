'''
author =
'''

from pprint import pp

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "lizz": "pass123"}

oddelovac = "="*30

print(oddelovac)
print("Vitej v aplikaci! Prihlas se: ")
username = input("USERNAME: ")
heslo = input("HESLO: ")

if (username, heslo) not in uzivatele.items():
    print("Jmeno nebo heslo nejsou v seznamu registrovanych uzivatelu")
else:
    print(f"Uzivateli: {username}, vitej zpet!")

print(oddelovac)

print(f"Mame {len(TEXTS)} texty k analyze.")
cislo_textu = int(input("Zadej cislo textu od 1 do 3: "))
vybrany_text = TEXTS[cislo_textu -1]
print(oddelovac)

ocisteny_text = vybrany_text.strip(".,/")
rozdeleny_text = ocisteny_text.split()

pocet_slov = len(rozdeleny_text)

print(f"Pocet slov je: {pocet_slov}")

zacinajici_vel = []
for slovo in rozdeleny_text:
    if slovo.istitle():
        zacinajici_vel.append(slovo)
        
print(f"Pocet slov zacinajici velkym pismenem je: {len(zacinajici_vel)}")

obsahujici_velka = []
for slovo in rozdeleny_text:
    if slovo.isupper():
        obsahujici_velka.append(slovo)

print(f"Pocet slov obsahujici jen velka pismena je: {len(obsahujici_velka)}")

obsahujici_mal = []
for slovo in rozdeleny_text:
    if slovo.islower():
        obsahujici_mal.append(slovo)

print(f"Pocet slov obsahujici jen mala pismena je: {len(obsahujici_mal)}")

pocet_cisel = []
for slovo in rozdeleny_text:
    if slovo.isnumeric():
        pocet_cisel.append(slovo)

print(f"Pocet cisel je: {len(pocet_cisel)}")

print(oddelovac)

delky = []
for slovo in rozdeleny_text:
    delky.append(len(slovo))

pocet_delek = {}
for cislo in delky:
    pocet_delek[cislo] = delky.count(cislo)

hodnoty = pocet_delek.keys()
for klic in hodnoty:
    print(f"{klic * '*'} {pocet_delek.get(klic)}")

print(oddelovac)

suma = []
for slovo in pocet_cisel:
    suma.append(int(slovo))

print(f"Pokud secteme vsechna cisla v textu, dostaneme hodnotu: {sum(suma)}")
