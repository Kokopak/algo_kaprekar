#!/usr/bin/python
#-*-coding: utf-8-*-

from itertools import permutations

def minmaxNombre(nombre):

    l = list(str(nombre))
    minn = int("".join(sorted(l)))
    maxn = int("".join(sorted(l, reverse=True)))
    return maxn - minn

nbr = input("Nombre : ")
lis_nbr = []
et = 1
while True :
    resul = minmaxNombre(nbr)
    if resul == 0 :
        print "La séquence s'arrête à 0"
        break
    elif resul == nbr :
        print "La séquence est constante"
        break
    elif resul in lis_nbr :
        print "La séquence se répète"
        break
    nbr = resul
    print "Etape %d : %d " % (et, nbr)
    lis_nbr.append(nbr)
    et += 1
