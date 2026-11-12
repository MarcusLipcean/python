"""
# =====================================================================

# Partea I — Dicționarul de bază

# =====================================================================
"""
from collections import Counter

# TODO: Ex 1 — Creează un dicționar numit `produs` cu cheile "nume",
#  "pret" și "stoc". Afișează dicționarul.
# produs = {
#     "nume": "aspirator",
#     "pret": 1000,
#     "stoc": 5,
# }
# print(produs)
"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la dicționarul de mai jos, afișează prețul.
#  Apoi afișează valoarea pentru cheia "reducere" — care nu există —
#  fără ca programul să se oprească.
# produs = {"nume": "Laptop", "pret": 14000, "stoc": 7}
# print(produs["pret"])
# print(produs.get("reducere", 0))

"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la dicționarul de mai jos, verifică dacă
#  există cheia "stoc" și afișează un mesaj corespunzător.
# produs = {"nume": "Laptop", "pret": 14000, "stoc": 7}
# mesaj = "Este!" if produs.get("stoc") else "Nu este!"
# print(mesaj)
"""=================================================================================================="""

# TODO: Ex 4 — Pornind de la dicționarul de mai jos, adaugă cheia nouă
#  "garantie" cu valoarea 24 și modifică valoarea cheii "pret" la 12500.
#  Afișează dicționarul.
# produs = {"nume": "Laptop", "pret": 14000, "stoc": 7}
#
# produs["garantie"] = 24
# produs["pret"] = 12500
#
# print(produs)
"""=================================================================================================="""

# TODO: Ex 5 — Pornind de la dicționarul de mai jos, scoate cheia "stoc"
#  și păstrează valoarea ei într-o variabilă. Afișează valoarea scoasă
#  și dicționarul rămas. La final, golește tot dicționarul.
# produs = {"nume": "Laptop", "pret": 14000, "stoc": 7}
#
# cate_sunt = produs["stoc"]
# produs.pop("stoc")
# produs.clear()
#
# print(produs)
"""
# =====================================================================

# Partea II — keys, values, items și for

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la dicționarul de mai jos, afișează separat
#  toate numele elevilor și toate notele lor.
note = {"Ana": 9, "Ion": 6, "Maria": 10, "Vlad": 8}


"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la același dicționar, parcurge-l și afișează
#  fiecare pereche sub forma "nume — notă", pe câte o linie.
note = {"Ana": 9, "Ion": 6, "Maria": 10, "Vlad": 8}


"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la același dicționar, calculează și afișează
#  media notelor.
note = {"Ana": 9, "Ion": 6, "Maria": 10, "Vlad": 8}


"""=================================================================================================="""

# TODO: Ex 4 — Pornind de la același dicționar, găsește și afișează
#  numele elevului cu nota cea mai mare.
note = {"Ana": 9, "Ion": 6, "Maria": 10, "Vlad": 8}


"""=================================================================================================="""

# TODO: Ex 5 — Pornind de la dicționarul de prețuri de mai jos,
#  construiește un dicționar nou care conține doar produsele cu prețul
#  mai mare de 100. Afișează-l.
preturi = {"caiet": 25, "ghiozdan": 350, "pix": 8, "tableta": 2200, "penar": 120}


"""
# =====================================================================

# Partea III — Dicționar de frecvențe

# =====================================================================
"""
# TODO: Ex 1 — Pornind de la lista de numere de mai jos, găsește și
#  afișează primul număr care apare de mai multe ori — acela a cărui
#  primă apariție este cea mai timpurie.
numere = [10, 5, 3, 4, 3, 5, 6]
# Rezultat așteptat:
# 5
# freq = Counter(numere)
#
# for n in numere:
#     if freq[n] > 1:
#         print(n)
#         break
# TODO: Ex 2 — Pornind de la lista de cuvinte de mai jos (cu repetări),
#  construiește un dicționar care numără câte ori apare fiecare cuvânt.
#  Afișează dicționarul.
cuvinte = ["mar", "para", "mar", "nuca", "mar", "para", "pruna", "nuca"]
# Rezultat așteptat:
# {'mar': 3, 'para': 2, 'nuca': 2, 'pruna': 1}
# print(Counter(cuvinte))

"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la textul de mai jos, găsește și afișează
#  primul caracter care apare o singură dată în text.
text = "abracadabra"
# Rezultat așteptat:
# c
# freq = {}
# for c in text:
#     freq[c] = freq.get(c, 0) + 1
# for c in text:
#     if freq[c] == 1:
#         print(c)
#         break

"""=================================================================================================="""

# TODO: Ex 4 — Pornind de la lista de cuvinte de mai jos, grupează la un
#  loc cuvintele care sunt anagrame (au exact aceleași litere). Afișează
#  grupurile rezultate.
cuvinte = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Rezultat așteptat:
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# grup = {}
# for cuvant in cuvinte:
#     cheie = "".join(sorted(cuvant))
#     if not cheie in grup:
#         grup[cheie] = []
#     grup[cheie].append(cuvant)
# print(list(grup.values()))
