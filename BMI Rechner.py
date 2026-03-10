##------------------------------------------------------------------
## Ein einfacher BMI Rechner der über das Terminal funktioniert    |
##------------------------------------------------------------------


## Introduction - Begrüßung und erklärung des Programms
print("Willkommen beim BMI Rechner!")
print("Dieses Programm berechnet ihren Body-Mass-Index (BMI)")

## Input - Fragt erst nach dem Gewicht in Kilogramm und in Metern über zwei float values
w = float(input("Bitte dein Gewicht in Kilogramm: "))  ## Gewichtseingabe
h = float(input("Dann bitte deine Größe in Metern: ")) ## Körpergrößeneingabe


## Berechnung vom BMI - Die Formel für den BMI mit rundung auf die erste Nachkommastelle
bmi = round(w / pow(h, 2), 1)


## Ergebnis - Die Ausgabe vom Ergebnis
print("Ihr BMI Beträgt: " + str(bmi))
    
## BMI Kategorisierungen - Die verschiedenen BMI Kategorien und deren Grenzwerte

bmi_categories = [
    (18.5, "Untergewicht"),
    (24.5, "Normalgewicht"),
    (29.9, "Übergewichtig"),
    (34.9, "Adipositas Grad 1"),
    (39.9, "Adipositas Grad 2"),
    (float('inf'), "Adipositas Grad 3"),
]

## for loop, der checkt in welche Kategorie oben der BMI fällt plus Ausgabe und dann beendigung des Loops
for threshold, label in bmi_categories: 
    if bmi < threshold:
        print("Sie haben " + label)
        break

