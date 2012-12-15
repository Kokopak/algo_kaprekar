#!/usr/bin/python
#-*-coding: utf-8-*-

from itertools import permutations

def minmaxNombre(nombre):

    stnbr = str(nombre)
    if len(str(nbr)) == 1:
        stnbr = "0"+stnbr

    maxn = max([int("".join(permu)) for permu in permutations(stnbr, len(stnbr))])
    minn = min([int("".join(permu)) for permu in permutations(stnbr, len(stnbr))])
    return maxn - minn

goodEn = False

while not goodEn:
    try:
        nbr = input("Nombre : ")
    except NameError:
        print "Nombre incorrect !"
    else:
        goodEn = True

etapes = raw_input("Voir les étapes ? (O/N) ")

bon = True
lis_nbr = []

et = 1
while bon:
    resul = minmaxNombre(nbr)
    if resul == nbr or resul == 0 or resul in lis_nbr:
        bon = False
    nbr = resul
    if etapes == "O":
        print "Etape(s) %d : %d " % (et, nbr)
    lis_nbr.append(nbr)
    et += 1

print "==================="

if resul in lis_nbr:
    print " ".join(str(el) for el in lis_nbr) + "..."
    print "La séquence se répète ou le nombre ne varie plus !"
elif resul == 0:
    print " ".join(str(el) for el in lis_nbr)
    print "La séquence s'arrête à 0"
else:
    print " ".join(str(el) for el in lis_nbr)
    print "Nombre bizarre O_O"

