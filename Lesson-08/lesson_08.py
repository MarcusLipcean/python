"""
# =====================================================================

# Partea I — Sets

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la lista de mai jos (cu repetări), află și
#  afișează câte numere UNICE conține.
# numere = [101, 203, 101, 305, 203, 407, 101, 305, 511, 407]
# numere = set(numere)
# print(len(numere))

"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la setul de mai jos: adaugă numărul 4, scoate
#  numărul 1, și încearcă să scoți numărul 99 — care nu există — fără
#  să se oprească programul. Afișează setul final.
# s = {1, 2, 3}
# s.add(4)
# s.remove(1)
# s.discard(99)
# print(s)
"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la setul și lista de mai jos, numără câte
#  elemente din listă se găsesc și în set. Afișează numărul.
# s = {1, 5, 7, 12}
# lista = [3, 5, 1, 8, 5, 12, 2, 7, 1]
# lista = set(lista)
# cate = len(lista.intersection(s))
# print(cate)
"""=================================================================================================="""

# TODO: Ex 4 — Pornind de la cele două seturi de mai jos, calculează
#  și afișează pe rând:
#    a) reuniunea — toate elementele din ambele
#    b) intersecția — doar elementele comune
#    c) diferențele a - b și b - a
#    d) diferența simetrică — elementele care apar într-un singur set
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))
# print(a.symmetric_difference(b))

"""
# =====================================================================

# Partea II — Tuples

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la tuplul de mai jos, afișează primul și
#  ultimul element. Apoi încearcă să modifici al doilea element în 99
#  și observă ce eroare apare. După ce ai văzut eroarea, comentează
#  linia care o produce ca să continue programul.
# punct = (10, 20, 30)
# print(punct[0])
# print(punct[len(punct)-1])
# punct[1] = 99

"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la tuplul de mai jos cu 3 elemente,
#  despachetează-l în trei variabile separate într-O SINGURĂ linie.
#  Apoi afișează fiecare variabilă pe o linie nouă.
# t = (101, 28, 75)
# nr1, nr2, nr3 = t
# print(nr1)
# print(nr2)
# print(nr3)

"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la lista de tupluri (a, b) de mai jos,
#  calculează SUMA celui de-al doilea element (b) din fiecare tuplu și
#  afișeaz-o. Folosește un for care despachetează direct fiecare tuplu
#  în două variabile.
# perechi = [(1, 120), (2, 85), (3, 240), (4, 60), (5, 175)]
# suma:int = 0
# for a, b in perechi:
#     suma += b
# print(suma)

"""=================================================================================================="""

# TODO: Ex 4 — Pornind de la lista de tupluri (a, b) de mai jos, găsește
#  tuplul cu cel mai MARE al doilea element (b) ȘI tuplul cu cel mai
#  MIC al doilea element. Folosește un SINGUR for. Afișează ambele
#  tupluri.
# import math
# perechi = [(1, 120), (2, 85), (3, 240), (4, 60), (5, 175), (6, 310), (7, 95)]
# min_b, max_b = math.inf, -math.inf
# for a, b in perechi:
#     if b < min_b:
#         min_b = b
#     if b > max_b:
#         max_b = b
# print(min_b, max_b)

"""
# =====================================================================

# Partea III

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la lista de mai jos (cu repetări), construiește
#  o listă de tupluri (element, count). Afișează rezultatul. Fiecare
#  element apare o singură dată în rezultat.
# lista = ["rosu", "verde", "albastru", "rosu", "rosu", "verde",
#          "galben", "albastru", "rosu", "verde", "negru"]


# res = []

# for i in set(lista):
#     element = (i, lista.count(i))
#     res.append(element)

# print(res)
"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la lista de numere și target-ul de mai jos,
#  găsește TOATE perechile distincte de numere din listă care, adunate,
#  dau target-ul. Returnează o listă de tupluri (a, b) cu a < b, fără
#  duplicate. Afișează rezultatul.
# numere = [2, 7, 11, 4, 3, 8, 6, 5, 1, 9]
# target = 10
#
#
# numere_unice = set(numere)
# res = []
#
# for i in numere_unice:
#     b = target - i
#     if i < b and b in numere_unice:
#         element = (i, b)
#         res.append(element)
#
# print(res)

"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la lista de numere de mai jos (în orice ordine,
#  cu posibile duplicate), găsește LUNGIMEA celei mai lungi serii de
#  numere consecutive. De exemplu, pentru [100, 4, 1, 3, 2] seria 1,2,3,4
#  are lungimea 4. Afișează doar lungimea.
numere = [100, 4, 200, 1, 3, 2, 5, 50, 51, 52, 53, 54, 55, 56]
numere = set(numere)
res = 0

for i in numere:
    cur = i + 1
    lungimea = 1
    while True:
        if cur not in numere:
            break
        lungimea += 1
        cur += 1
    if res < lungimea:
        res = lungimea

print(res)