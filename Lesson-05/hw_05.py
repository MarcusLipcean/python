# Lecția 05 — Liste și bucla for
# Tema pentru acasă


"""
# =====================================================================

# Partea I — Liste: append, extend, concatenare

# =====================================================================
"""

# TODO: Ex 1 — Citește o propoziție de la utilizator.
#  Folosește .split() pentru a o împărți în cuvinte și afișează ultimul
#  cuvânt din listă.
# propozitie = input("Da-mi o propozitie:")
# lista = []
#
# lista = propozitie.split()
#
# print(lista[-1])
"""=================================================================================================="""

# TODO: Ex 2 — Pornește de la o listă goală de cărți.
#  Citește 3 titluri de la utilizator și adaugă-le cu .append().
#  Apoi adaugă încă 3 titluri dintr-o listă existentă cu .extend([...]).
#  Afișează lista finală.
# carti = []
# carti_noi = ["Pax", "Copacul cu 13 etaje", "Bunicuta hotomana"]
#
# for i in range(3):
#     carte = input("")
#     carti.append(carte)
#
# carti.extend(carti_noi)
#
# print(carti)
"""=================================================================================================="""

# TODO: Ex 3 — Creează o listă cu 3 melodii preferate. Cere utilizatorului
#  o melodie nouă și adaug-o în listă folosind operatorul +.
#  Afișează lista actualizată.
# muzici = ["Miorita", "Mamaligamania", "Trenuletul"]
#
# # CUM SA ADAUGAM UN STRING LA O LISTA ???
#
# muzici = muzici + muzica
#
# print(muzici)
"""=================================================================================================="""


"""
# =====================================================================

# Partea II — remove, del, condiții și metode utile

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la lista de mai jos, cere utilizatorului un
#  animal. Dacă animalul există în listă, elimină-l cu .remove().
#  Altfel printează "Animalul nu există".
# animale = ["pisică", "câine", "papagal"]
#
# animal = input("Da-mi un nume de animal:")
#
# if animal in animale:
#     animale.remove(animal)
# else:
#     print("Animalul nu exista")
"""=================================================================================================="""

# TODO: Ex 2 — Creează o listă cu 3 ingrediente. Adaugă 2 ingrediente
#  noi cu .extend(), apoi șterge ultimul ingredient cu del lista[-1].
#  Afișează lista finală.
# ingrediente: list = ["ou", "banane", "lapte"]
# ingrediente_noi: list = ["paste", "iaurt"]
#
# ingrediente.extend(ingrediente_noi)
# del ingrediente[-1]
#
# print(ingrediente)
"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la lista de orașe, sortează alfabetic cu
#  .sort() și afișează. Apoi inversează ordinea cu .reverse() și afișează
#  din nou. La final printează f"Am vizitat {len(orase)} orașe".
# orase = ["Chișinău", "București", "Iași", "Cluj", "Brașov"]
#
# print(sorted(orase))
# print(sorted(orase, reverse=True))
# print(f"Am vizitat {len(orase)} orașe")
"""=================================================================================================="""

# TODO: Ex 4 — Pornind de la lista de temperaturi, verifică dacă prima
#  temperatură este mai mică decât 0. Dacă da, printează "frig",
#  altfel "cald".
# temperaturi = [-5, 12, 18, 22, -2, 8, 15]
#
# temperatura = "frig" if temperaturi[0] < 0 else "cald"
#
# print(temperatura)
"""=================================================================================================="""

# TODO: Ex 5 — Pornind de la lista de fructe de mai jos:
#   1) adaugă "portocală" cu .append()
#   2) elimină "pară" cu .remove()
#   3) afișează de câte ori apare "măr" folosind .count()
#   4) afișează poziția lui "kiwi" folosind .index()
#   5) afișează numărul total de fructe cu len()
# fructe = ["măr", "pară", "banană", "măr", "kiwi"]
#
# fructe.append("portocala")
# fructe.remove("pară")
#
# print(fructe.count("măr"))
# print(fructe.index("kiwi"))
# print(len(fructe))
"""=================================================================================================="""


"""
# =====================================================================

# Partea III — Exerciții cu .join() și .split()

# =====================================================================
"""

# TODO: Ex 1 — Folosește .join() pentru a uni numele cu separatorul " și ".
#  Rezultat așteptat: "Ana și Maria și Elena"
# nume = ["Ana", "Maria", "Elena"]
#
# nume_noi: str = " si ".join(nume)
#
# print(nume_noi)
"""=================================================================================================="""

# TODO: Ex 2 — Folosește .join() pentru a separa orașele cu " - "
#  (linie cu spații în jur).
# orase = ["Chișinău", "București", "Iași"]
#
# orase_traseu: str = " - ".join(orase)
#
# print(orase_traseu)
"""=================================================================================================="""

# TODO: Ex 3 — Folosește .join() cu separator newline ("\n") pentru a
#  afișa fiecare pas pe o linie separată.
# pasi_reteta = ["1. Pune apa la fiert", "2. Adaugă pastele", "3. Scurge pastele"]
#
# pasi: str = "\n".join(pasi_reteta)
#
# print(pasi)
"""=================================================================================================="""

# TODO: Ex 4 — Folosește .split("-") pentru a descompune codul în țară,
#  an și număr. Afișează rezultatul sub forma:
#   f"Țara: {t}, Anul: {a}, Numărul: {n}"
# cod = "MD-2025-001"
#
# codul: list = cod.split("-")
#
# print(f"Țara: {codul[-3]}, Anul: {codul[-2]}, Numărul: {codul[-1]}")
"""=================================================================================================="""

# TODO: Ex 5 — Pornind de la fraza de mai jos, afișează doar ultimele
#  două cuvinte.
# fraza = "Astăzi este o zi frumoasă"
#
# cuvinte: list[str] = fraza.split()
#
# print(cuvinte[-2:])
"""=================================================================================================="""


"""
# =====================================================================

# Partea IV — Bucla for cu liste

# =====================================================================
"""

# TODO: Ex 1 — Parcurge lista de animale cu un for și afișează fiecare
#  animal pe o linie nouă.
# animale = ["pisică", "câine", "iepure", "papagal"]
#
# for animal in animale:
#     print(animal)
"""=================================================================================================="""

# TODO: Ex 2 — Parcurge lista de vârste cu un for și afișează doar
#  vârstele mai mari sau egale cu 18.
# varste = [12, 17, 20, 35, 8, 45, 16, 22]
#
# for varsta in varste:
#     if varsta >= 18:
#         print(varsta)

"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la lista de salarii:
#   1) sortează crescător cu .sort()
#   2) ia ultimele 3 salarii cu slicing [-3:]
#   3) parcurge lista cu un for
#   4) printează "Ridicat" dacă salariul > 5000, altfel "Mediu"
# salarii = [3500, 7200, 4100, 9000, 2800, 5500, 6300, 4800]
#
# salarii.sort()
#
# print(salarii[-3:])
#
# for salariu in salarii:
#     ce_salariu: str = "Ridicat" if salariu > 5000 else "Mediu"
#     print(ce_salariu)
"""=================================================================================================="""
