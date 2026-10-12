"""
# =====================================================================

# Partea I — break

# =====================================================================
"""
# from sympy import false

# TODO: Ex 1 — Pornind de la lista de mai jos, găsește primul număr
#  strict mai mare decât 100 și afișează-l. Oprește bucla imediat ce
#  l-ai găsit, folosind break.
# numere = [12, 45, 7, 88, 134, 22, 200, 9]
# for i in numere:
#     if i > 100:
#         print(i)
#         break
"""=================================================================================================="""

# TODO: Ex 2 — Cere utilizatorului să introducă cuvinte într-o buclă
#  while. Când scrie "stop", afișează "Gata!" și ieși din buclă cu
#  break. Pentru orice alt cuvânt, doar afișează-l.
# cuvant: str = ''
# while cuvant != 'stop':
#     cuvant = input()
#     if cuvant == 'stop':
#         print("Gata!")
#         break
#     print(cuvant)


"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la lista de cheltuieli zilnice, adună-le
#  într-o variabilă "total". În momentul în care totalul depășește 500,
#  afișează f"Buget depășit la {total}" și oprește bucla cu break.
# cheltuieli = [80, 120, 60, 90, 200, 50, 150, 40]
# suma = 0
# for i in cheltuieli:
#     suma += i
#     if suma > 500:
#         print(f"Buget depășit la {suma}")
#         break

"""=================================================================================================="""

"""
# =====================================================================

# Partea II — continue

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la lista de note, afișează doar notele care
#  sunt mai mari sau egale cu 7. Folosește continue pentru a sări peste
#  cele mai mici.
# note = [4, 8, 6, 10, 3, 9, 5, 7]
# for nota in note:
#     if nota >= 7:
#         print(nota)
#     continue

"""=================================================================================================="""

# TODO: Ex 2 — Pornind de la propoziția de mai jos, sparge-o în cuvinte
#  și afișează doar cuvintele cu mai mult de 4 litere. Pe cele scurte
#  sari peste ele cu continue.
# propozitie = "Învăț Python ca să lucrez cu date și să devin analist"
# lista: list[str] = propozitie.split()
#
# for i in lista:
#     if len(i) > 4:
#         print(i)
#     continue
"""=================================================================================================="""

# TODO: Ex 3 — Pornind de la lista de tranzacții (pozitive și negative),
#  calculează suma DOAR a tranzacțiilor pozitive. Pe cele negative sari
#  peste ele cu continue. Afișează suma la final.
# tranzactii = [120, -50, 80, -30, 200, -75, 60, -10]
# suma = 0
#
# for i in tranzactii:
#     if i > -1:
#         suma += i
# print(suma)
"""=================================================================================================="""


"""
# =====================================================================

# Partea III — pass

# =====================================================================
"""

# TODO: Ex 1 — Definește o funcție trimite_email() care deocamdată nu
#  face nimic. Folosește pass în corpul ei. Apoi apeleaz-o de două ori
#  ca să verifici că nu dă eroare.
# def trimite_email():
#     pass
# print(trimite_email())
# print(trimite_email())

"""=================================================================================================="""


"""
# =====================================================================

# Partea IV — Provocări (combinăm tot ce-am învățat)

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la un număr întreg pozitiv (de exemplu 9876),
#  afișează fiecare cifră a lui pe o linie separată, fără să-l
#  transformi în string. (Indiciu: ultima cifră a unui număr este
#  rezultatul împărțirii cu rest la 10.)

# numar = 9876
# while numar > 0:
#     print(numar % 10)
#     numar //= 10
"""=================================================================================================="""

# TODO: Ex 2 — Citește de la utilizator un n. Generează o listă cu
#  primele n numere prime și afișeaz-o. Un număr este prim dacă nu se
#  împarte exact la niciun număr între 2 și rădăcina lui pătrată.
# nr = 100
# numere_prime = []
# for n in range(2, nr):
#     is_prim = True
#     for i in range(2, int(n**0.5)):
#         if n % i == 0:
#             is_prim = False
#             break
#     if is_prim:
#         numere_prime.append(n)
# print(numere_prime)



"""=================================================================================================="""

# TODO: Ex 3 — Citește de la utilizator un an y. Găsește cel mai mic
#  an strict mai mare ca y în care toate cifrele sunt diferite între
#  ele. Afișează anul găsit.
# nr = '1999'
#
# while True:
#     nr = str(nr)
#     lungimea = len(nr)
#     este_bun = True
#     for i in range(lungimea):
#         for j in range(i + 1, lungimea):
#             if nr[i] == nr[j]:
#                 este_bun = False
#                 break
#         if not este_bun:
#             break
#     if este_bun:
#         print(nr)
#         break
#     nr = int(nr) + 1

# Reolva inca in 2 metode, fara seturi, metode al strign

# 1 metoda:
# nr = '1999'
# cate_ori: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# while True:
#     cate_ori = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     nr = str(nr)
#     este_bun = True
#     for i in nr:
#         cate_ori[int(i)] = nr.count(i)
#     for i in cate_ori:
#         if i != 1 and i != 0:
#             este_bun = False
#             break
#     if este_bun:
#         print(nr)
#         break
#     nr = int(nr) + 1

# 2 metoda:
# nr = '1999'
#
# while True:
#     nr = str(nr)
#     este_bun = True
#     este_bun = len(nr) == len(set(nr))
#     if este_bun:
#         print(nr)
#         break
#     nr = int(nr) + 1

nr = "1999"

while True:
    nr = str(nr)
    este_bun = True
    for i in range(len(nr)):
        if nr.find(nr[i]) != i:
            este_bun = False
            break
    if este_bun:
        print(nr)
        break
    nr = int(nr) +1
"""=================================================================================================="""
