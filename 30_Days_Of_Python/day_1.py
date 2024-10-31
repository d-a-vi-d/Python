david = {
'name':'David',
'country':'Australia', 
'age':20,
'is_married':False} 
while (0<1):
    x = input('was möchtest du haben? ')
    if x == "exit":  # Abbruchbedingung
        break  # Schleife beenden
    try:
        print(david[x])
    except KeyError:
        print("Das weiß ich leider nicht!")