## BMI Rechner für die Schule

## Introduction
print("Willkommen beim BMI Rechner!")
print("Dieses Programm berechnet ihren Body-Mass-Index (BMI)")

## Input
w = float(input("Bitte dein Gewicht in Kilogramm: "))  ## Gewichtseingabe
h = float(input("Dann bitte deine Größe in Metern: ")) ## Körpergrößeneingabe

## Berechnung vom BMI
bmi = round(w / pow(h, 2), 1)


## Ergebnis
print("Ihr BMI Beträgt: " + str(bmi))
    
## BMI Kategorisierungen

bmi_categories = [
    (18.5, "Untergewichtig"),
    (24.5, "Normalgewicht"),
    (29.9, "Übergewichtig"),
    (34.9, "Adipositas Grad 1"),
    (39.9, "Adipositas Grad 2"),
    (float('inf'), "Adipositas Grad 3"),
]

for threshold, label in bmi_categories: 
    if bmi < threshold:
        print("Sie haben " + label)
        break
