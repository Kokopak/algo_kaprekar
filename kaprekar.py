#!/usr/bin/python
#-*-coding: utf-8-*-

from itertools import permutations

def minmaxNombre(nombre):

    l = list(str(nombre))
    minn = int("".join(sorted(l)))
    maxn = int("".join(sorted(l, reverse=True)))
    return maxn - minn

def kaprekar(n) :
    l_nb = []
    while True :
        new = minmaxNombre(n)
        if new == n :
            # cas de la suite constante
            return n
        elif new in l_nb :
            # cas d'un cycle de nombres
            pos = l_nb.index(new)
            return tuple(sorted(l_nb[pos:]))
        l_nb.append(new)
        n = new

s = {}
for n in range(100000) :
    k = kaprekar(n)
    if k in s :
        s[k] += 1
    else :
        s[k] = 1

for k in sorted(s.keys()) :
    print k, s[k]
