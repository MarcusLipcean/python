"""
# =====================================================================

# Partea I — Dicționarul de bază

# =====================================================================
"""
from collections import Counter
# TODO: Ex 1 — Creează un dicționar numit `carte` cu cheile "titlu",
#  "autor" și "pagini". Afișează dicționarul.


"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la dicționarul de mai jos, afișează numărul de
#  pagini. Apoi afișează valoarea pentru cheia "editura" — care nu
#  există — fără ca programul să se oprească.
carte = {"titlu": "Maitreyi", "autor": "Mircea Eliade", "pagini": 232}


"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la dicționarul de mai jos, verifică dacă
#  există cheia "autor" și afișează un mesaj corespunzător.
carte = {"titlu": "Maitreyi", "autor": "Mircea Eliade", "pagini": 232}


"""=================================================================================================="""

# TODO: Ex 4 — Pornind de la dicționarul de mai jos, adaugă cheia nouă
#  "an" cu valoarea 1933 și modifică valoarea cheii "pagini" la 248.
#  Afișează dicționarul.
carte = {"titlu": "Maitreyi", "autor": "Mircea Eliade", "pagini": 232}


"""=================================================================================================="""

# TODO: Ex 5 — Pornind de la dicționarul de mai jos, scoate cheia
#  "pagini" și păstrează valoarea ei într-o variabilă. Afișează valoarea
#  scoasă și dicționarul rămas. La final, golește tot dicționarul.
carte = {"titlu": "Maitreyi", "autor": "Mircea Eliade", "pagini": 232}


"""
# =====================================================================

# Partea II — keys, values, items și for

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la dicționarul de mai jos, afișează separat
#  toate numele angajaților și toate salariile lor.
salarii = {"Andrei": 9000, "Elena": 12000, "Maria": 7500, "Radu": 15000}


"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la același dicționar, parcurge-l și afișează
#  fiecare pereche sub forma "nume — salariu", pe câte o linie.
salarii = {"Andrei": 9000, "Elena": 12000, "Maria": 7500, "Radu": 15000}


"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la același dicționar, calculează și afișează
#  salariul mediu.
salarii = {"Andrei": 9000, "Elena": 12000, "Maria": 7500, "Radu": 15000}


"""=================================================================================================="""

# TODO: Ex 4 — Pornind de la același dicționar, găsește și afișează
#  numele angajatului cu salariul cel mai mare.
salarii = {"Andrei": 9000, "Elena": 12000, "Maria": 7500, "Radu": 15000}


"""=================================================================================================="""

# TODO: Ex 5 — Pornind de la dicționarul de populații de mai jos,
#  construiește un dicționar nou care conține doar orașele cu populația
#  mai mare de 100000. Afișează-l.
populatii = {"Chișinău": 520000, "Bălți": 150000, "Cahul": 39000, "Orhei": 33000, "Tiraspol": 130000}


"""
# =====================================================================

# Partea III — Dicționar de frecvențe

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la lista de culori de mai jos (cu repetări),
#  construiește un dicționar care numără câte ori apare fiecare culoare.
#  Afișează dicționarul.
# culori = ["rosu", "verde", "rosu", "albastru", "verde", "rosu", "galben", "verde"]
#
# print(Counter(culori))
"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la lista de nume de mai jos, găsește și
#  afișează primul nume care apare de mai multe ori — acela a cărui
#  primă apariție este cea mai timpurie.
nume = ["Vlad", "Ana", "Ion", "Ion", "Ana", "Maria"]
# Rezultat așteptat:
# 5
# freq = Counter(nume)
#
# for n in nume:
#     if freq[n] > 1:
#         print(n)
#         break

"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la textul de mai jos, găsește și afișează
#  primul caracter care apare o singură dată în text.
# text = "succes"
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
# cuvinte = ["arc", "rac", "car", "ton", "not", "porc"]
# grup = {}
# for cuvant in cuvinte:
#     cheie = "".join(sorted(cuvant))
#     if not cheie in grup:
#         grup[cheie] = []
#     grup[cheie].append(cuvant)
# print(list(grup.values()))