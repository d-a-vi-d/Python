while True:
    gleichung = input("Gleichung: ")
    gleichung.replace(" ", "").replace("y=","")
    k, d = gleichung.split("x")
    k = float(k) if k!=("") else 1
    d = float(d) if d!=("") else 0
    a = -d/k
    print("Steigung k=", k)
    print("Nullstelle=", a)
    print("d=", d)