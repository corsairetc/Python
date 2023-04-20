# Definujeme si proměnné
a = float(input("Zadejte stranu A místnosti v metrech :" ))
b = float(input("Zadejte stranu B místnosti v metrech :" ))

# Definice programu.
if a <= 0 or b <= 0:
    print("Délka stran nemůže být záporná!")
else:
    print("Obvod místnosti je :", a * b, "m2")
