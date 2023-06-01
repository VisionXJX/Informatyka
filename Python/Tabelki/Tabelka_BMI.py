print ("To jest program liczacy BMI dla calej rodziny")

I1 = input("Podaj swoje Imie: ")
G1 = int(input("Podaj swoja Wage: "))
H1 = float(input("Podaj swoj Wzrost: "))
BMI1 = (G1 / (H1**2))

I2 = input("Wpisz czlonka rodziny: ")
G2 = int(input("Podaj Wage Osoby: "))
H2 = float(input("Podaj Wzrost Osoby: "))
BMI2 = (G2 / (H2**2))

I3 = input("Wpisz czlonka rodziny: ")
G3 = int(input("Podaj Wage Osoby: "))
H3 = float(input("Podaj Wzrost Osoby: "))
BMI3 = (G3 / (H3**2))


szer = 38
print ("_" * szer)
print ("│ {:9s} │ {:3s} │ {:4s} │ {:5s} │".format("Kto", "Waga", "Wzrost", "BMI"))
print ("*" * szer)
print ("│ {:9s} │ {:3d} │ {:4.2f} │ {:5.2f} │".format(I1, G1, H1, BMI1))
print ("│ {:9s} │ {:3d} │ {:4.2f} │ {:5.2f} │".format(I2, G2, H2, BMI2))
print ("│ {:9s} │ {:3d} │ {:4.2f} │ {:5.2f} │".format(I3, G3, H3, BMI3))
print ("_" * szer)
