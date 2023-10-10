import random
from  statistics import median
import math
from collections import Counter

lista = []

for x in range(100):

   lista.append(random.randint(1, 1000))

#zadanie 1
print("1. Suma wszystkich cyfr z listy wynosi:\n", sum(lista),)

#zadanie 2 z funkcja pythona
print("2a. Najmniejszy element listy to:\n ", min(lista))
#zadanie 2 bez pythona

l = list(lista)
min1 = l[0]
for i in range(1, len(l)):
    if (l[i] < min1):
        min1 = l[i]
print("2b. Najmniejszy element listy to:\n ",min1)

#zadanie 3 z funkcja pythona
print("3a. Najwiekszy element listy to:\n ", max(lista))
#zadanie 3 bez pythona
l = list(lista)
min1 = l[0]
for i in range(1, len(l)):
    if (l[i] > min1):
        min1 = l[i]
print("3b. Najwiekszy element listy to:\n ",min1)
#zadanie 4

print("4. Mediana wynosi: \n", (median(lista)))

#zadanie 5
sorted_liczby = sorted(lista)
print("5a. Pierwsze 20 najmniejeszych liczb to :\n",sorted_liczby[0:20])

#zadanie 5 bez wbudowanej funkcji

number = lista

for i in range(len(number)):
    for j in range(i + 1, len(number)):

        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]

print("5b. Pierwsze 20 najmniejeszych liczb to :\n", number[0:20])


#zadanie 6

wynik = math.prod(lista)
print("6. Iloczyn  listy wynosi: \n", wynik)

#zadanie 7

counters = Counter(map(lambda x: len(str(x)), lista))
print("7. Ilość liczb trzy cyfrowych: \n",counters.get(3, 0))

#zadanie 8

def policz(list):
    tab = [[list[0], 0]]
    for i in list:
        for j in range(0, len(tab)):
            if (i == tab[j][0]):
                tab[j][1] += 1
                break
        else:
            tab.append([i, 1])
    return tab


def ile(list):
    tab = [] + policz(list)
    max = tab[0][1]
    odp = []

    for i in tab:
        if (i[1] > max):
            odp = [i[0]]
            max = i[1]
        elif (i[1] == max):
            odp.append(i[0])
    return [odp, max]


print("8. Powtarzają sie liczby: ", ile(lista)[0], "ilość powtórzeń:", ile(lista)[1],"\n")

#zadanie 9

def ilemin(powt):
    tab = [] + policz(powt)
    min = 1
    odp = []

    for i in tab:
        if (i[1] < min):
            odp = [i[0]]
            min = i[1]
        elif (i[1] == min):
            odp.append(i[0])
    return [odp, min]

print("9. Nie powtarzają sie liczby: \n", ilemin(lista)[0])

#zadanie 10

def ile3(xxx, licz3):
    tab = [] + policz(licz3)
    odp = []

    for i in tab:
        if (i[1] == xxx):
            odp.append(i[0])
    return odp


print("10. Liczby powtarzające sie na liście dokładnie 3 razy to:\n ", ile3(3, lista))


# zadanie 11

liczby = []

for y in lista:

   if str(21) in str(y):

       liczby.append(y)

print("11. Liczby zawierające w sobie 21 (oddzielone przcinkiem):\n", ", ".join(map(str, liczby)))

# zadanie 12

licznik = 0

for y in lista:

   if y > 800:

       licznik += 1

print("12.W zbiorze jest", licznik, "liczb większych niż 800\n")

# zadanie 13

mini = sorted(lista)[:3]

maxi = sorted(lista)[len(lista)-3:len(lista)]

print("13.Trzy najmniejsze liczby z tego zbioru to:\n", ", ".join(map(str, mini)))

print("Trzy największe liczby z tego zbioru to:\n", ", ".join(map(str, maxi)))

# zadanie 14

lista2 = list(dict.fromkeys(lista))

print("14. Po usunięciu duplikatów pozostało", len(lista2), "elementów\n")

#zadanie 15
print("15.", lista,"\n   ",random.sample(lista, len(lista)))

#zadanie 16
licz = list(map(str, lista))
print("16. Lista przekonwertowana na string:\n",licz)

#zadanie 17
print("17.Liczby z listy razem z informacja ile razy sie powtarzają \n", policz(lista))

#zadanie 18

def pom(a,b,tablica):
  tab = policz(tablica)
  odp = 0
  for i in tab:
    if(i[0]>=a and i[0]<=b):
      odp+=i[1]
  return odp


a = int(input(" Podaj liczbe a: "))
c = int(input(" Podaj liczbe b: "))
print("18.", pom(a,c,lista))
del a, c

#zadanie 19 ,20

def ele(a, tablica):
  tab = policz(tablica)
  odp = 0
  for i in tab:
    if(a and i[0]%2==0):
      odp+=i[1]
    elif(not a and i[0]%2==1):
      odp+=i[1]
  return odp

print("19.Elementy parzyste w liście.\n", ele(1,lista))
print("20.Elementy nieparzyste w liście. \n", ele(0,lista))


