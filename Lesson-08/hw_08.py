"""
# =====================================================================

# Partea I — Sets

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la lista de mai jos (cu duplicate), află și
#  afișează câte numere UNICE conține.
# numere = [85, 92, 70, 85, 65, 92, 70, 78, 85, 100]
# print(len(set(numere)))

"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la setul de mai jos: adaugă numerele 7 și 22,
#  scoate numărul 15, și încearcă să scoți numărul 99 — care nu există
#  — fără să se oprească programul. Afișează setul final.
# s = {12, 15, 23, 31, 40}
# s.add(7)
# s.add(22)
# s.remove(15)
# s.discard(99)
# print(s)
"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la cele două seturi de mai jos, afișează:
#  câte elemente sunt comune (în ambele), câte sunt doar în a, și câte
#  sunt doar în b.
# a = {1, 2, 3, 4, 5, 6}
# b = {4, 5, 7, 8, 9}
# print(len(a | b))
# print(len(a - b))
# print(len(b - a))
"""
# =====================================================================

# Partea II — Tuples

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la tuplul de mai jos cu 3 elemente,
#  despachetează-l în trei variabile separate într-O SINGURĂ linie.
#  Apoi afișează fiecare variabilă pe o linie nouă.
# t = ("luni", 14, 203)
# ziua, data, anul = t
# print(ziua)
# print(data)
# print(anul)

"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la lista de tupluri (a, b) de mai jos, numără
#  CÂTE tupluri au al doilea element (b) strict mai mare ca 70.
#  Folosește un for care despachetează direct fiecare tuplu.
# perechi = [(1, 65), (2, 80), (3, 90), (4, 55), (5, 75), (6, 70), (7, 88)]
# k:int = 0
# for a, b in perechi:
#     if b > 70:
#         k += 1
# print(k)
"""
# =====================================================================

# Partea III — Provocare

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la string-ul de mai jos, construiește o listă
#  de tupluri (caracter, count). Fiecare caracter apare o singură dată
#  în rezultat. Afișează rezultatul.
# text = "programare"
# text_unic: list[str] = []
# for i in text:
#     text_unic.append(i)
# text_unic = set(text_unic)
# res = []
# for i in text_unic:
#     element = (i, text.count(i))
#     res.append(element)
# print(res)