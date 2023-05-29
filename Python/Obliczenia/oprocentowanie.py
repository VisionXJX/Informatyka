start = float(input("Stan początkowy konta wynosi: "))

#Stopa Oprocentowania
rate = float(input("Stopa oprocentowania w skali roku wynosi: "))

n = int(input("Liczba lat na lokacie: "))
end = start*(1 + rate * n)

print ("Po {} latach kapitał będzie wynosił {} zł" .format (n,end))
