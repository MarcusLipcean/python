"""
# =====================================================================

# Partea I — Liste: append, extend, concatenare

# =====================================================================
"""

# TODO: Ex 1 — Citește o propoziție de la utilizator.
#  Folosește .split() pentru a o împărți în cuvinte și afișează al
#  treilea cuvânt din listă.
# prop = "Eu fac lectie"
# lista = prop.split()
# print(lista)
# print(lista[2])
"""=================================================================================================="""

# TODO: Ex 2 — Pornește de la o listă goală de cumpărături.
#  Citește 3 produse de la utilizator și adaugă-le cu .append().
#  Apoi adaugă încă 3 produse dintr-o listă existentă cu .extend([...]).
#  Afișează lista finală.


"""=================================================================================================="""

# TODO: Ex 3 — Creează o listă cu 3 filme preferate. Cere utilizatorului
#  un film nou și adaugă-l în listă folosind operatorul +.
#  Afișează lista actualizată.

"""=================================================================================================="""


"""
# =====================================================================

# Partea II — remove, del, condiții și metode utile

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la lista de mai jos, cere utilizatorului un
#  produs. Dacă produsul există în listă, elimină-l cu .remove().
#  Altfel printează "Produsul nu există".
# produse = ["ou", "lapte", "făină"]
# produs = "banana"
# if produs in produse:
#     produse.remove(produs)
#     print(produse)
# else:
#     print("Produsul nu exista!")
"""=================================================================================================="""

# TODO: Ex 2 — Creează o listă cu 3 jucării. Adaugă 2 jucării noi cu
#  .extend(), apoi șterge prima jucărie cu del lista[0].
#  Afișează lista finală.
# produse = ["ou", "lapte", "făină"]
# produse_noi = ["mere", "banane"]
# produse.extend(produse_noi)
# del produse[0]
# print(produse)
"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la lista de colegi, sortează alfabetic cu
#  .sort() și afișează. Apoi inversează ordinea cu .reverse() și afișează
#  din nou. La final printează f"Sunt {len(colegi)} colegi în clasă".
# colegi = ["Mihai", "Ana", "Elena", "Dan", "Ioana"]
# colegi.sort()
# colegi.reverse()
# print(f"Sunt {len(colegi)} colegi în clasă")
"""=================================================================================================="""

# TODO: Ex 4 — Pornind de la lista de prețuri, verifică dacă primul preț
#  este mai mare decât 50. Dacă da, printează "scump", altfel "ieftin".
# preturi = [15, 20, 35, 70, 1000, 56, 45]
# res: str = "Scump!" if preturi[0] > 50 else "Ieftin!"
# print(res)
# if preturi[0] > 50:
#     print("scump!")
# else:
#     print("Ieftin!")

"""=================================================================================================="""

# TODO: Ex 5 — Pornind de la lista de studenți de mai jos:
#   1) adaugă "Ioana" cu .append()
#   2) elimină "Mihai" cu .remove()
#   3) afișează de câte ori apare "Ana" folosind .count()
#   4) afișează poziția lui "Elena" folosind .index()
#   5) afișează numărul total de studenți cu len()
# studenti = ["Ana", "Mihai", "Elena", "Dan", "Ana"]
# studenti.append("Ioana")
# studenti.remove("Mihai")
# print(studenti.count("Ana"))
# print(studenti.index("Elena"))
# print(len(studenti))
# print(studenti)
"""=================================================================================================="""


"""
# =====================================================================

# Partea III — Exerciții cu .join() și .split()

# =====================================================================
"""

# TODO: Ex 1 — Folosește .join() pentru a combina cuvintele într-o
#  propoziție (separator: spațiu).
# cuvinte = ["Ana", "are", "mere"]
# propozitie: str = " ".join(cuvinte)
# print(propozitie)
"""=================================================================================================="""

# TODO: Ex 2 — Folosește .join() pentru a separa produsele cu virgulă
#  și spațiu.
lista_cumparaturi = ["pâine", "lapte", "ouă"]


"""=================================================================================================="""

# TODO: Ex 3 — Folosește .join() cu separator newline ("\n") pentru a
#  afișa fiecare vers pe o linie separată.
# versuri = ["Mereu spre stele", "Privim adânc", "Și visăm"]
# poezie: str = "\n".join(versuri)
# print(poezie)
"""=================================================================================================="""

# TODO: Ex 4 — Folosește .split("/") pentru a descompune data în zi,
#  lună și an. Afișează rezultatul sub forma:
#   f"Ziua: {z}, Luna: {l}, Anul: {a}"
# data = "25/04/2022"
# lista: list = data.split("/")
# print(f"Ziua: {lista[0]}, Luna: {lista[1]}, Anul: {lista[2]}")
"""=================================================================================================="""

# TODO: Ex 5 — Pornind de la fraza de mai jos, afișează doar primele
#  două cuvinte.
# fraza = "Astăzi este o zi frumoasă"
# lista: list = fraza.split()
# print(lista[0:2])
"""=================================================================================================="""


"""
# =====================================================================

# Partea IV — Bucla for cu liste

# =====================================================================
"""

# TODO: Ex 1 — Parcurge lista de produse cu un for și afișează fiecare
#  element pe o linie nouă.
produse = ["ou", "lapte", "pâine"]


"""=================================================================================================="""

# TODO: Ex 2 — Parcurge lista de prețuri cu un for și afișează doar
#  prețurile mai mari decât 50.
# preturi = [15, 20, 35, 70, 1000, 56, 45]
# for pret in preturi:
#     if pret > 50:
#         print(pret)

"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la lista de note:
#   1) sortează descrescător cu .sort(reverse=True)
#   2) ia primele 5 note cu slicing [:5]
#   3) parcurge lista cu un for
#   4) printează "Excelent" dacă nota >= 9, altfel "Bun"
# note = [9, 5, 8, 10, 6, 7, 4, 9]
# note.sort(reverse=True)
# print(note[:5])
# for nota in note:
#     if nota >= 9:
#         print("Excelent")
#     else:
#         print("Bun")

"""=================================================================================================="""
# tabla_de_sah: list[list] = []
# cifre: str = "87654321"
# litere: str = "abcdefgh"
#
# for cifra in cifre:
#     rand: list[str] = []
#
#     for i in range(len(litere)):
#         culoare: str = "alb" if i % 2 == 0 else "negru"
#         celula = f"{cifra}{litere[i]}-{culoare}"   # nr litera - culoare    ex:   8a-alb
#         rand.append(celula)
#
#     tabla_de_sah.append(rand)
#
# print(tabla_de_sah)