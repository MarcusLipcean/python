
"""
# =====================================================================

# Partea I — Recapitulare: liste și dicționare

# =====================================================================
"""

# TODO: Ex 1 — Pornind de la lista de mai jos, scoate ultimul element și
#  păstrează-l într-o variabilă. Adaugă apoi 7 la final. Afișează elementul
#  scos, ultimul element curent și câte elemente are lista acum.
# numere:list = [3, 8, 1, 9, 4]
# ultimul:int = numere[-1]
# numere.pop(-1)
# numere.append(7)
# print(ultimul)
# print(numere[-1])
# print(len(numere))
"""=================================================================================================="""

# TODO: Ex 2 — Numără de câte ori apare fiecare literă în cuvântul de mai jos
#  și afișează litera care apare cel mai des, împreună cu numărul de apariții.
cuvant = "matematica"
# freq = {}
# for litera in cuvant:
#     freq[litera] = freq.get(litera, 0) + 1
# litera_max = max(freq, key=freq.get)
# print(litera_max, freq[litera_max])
# max = 0
# litera_max = ""
# for litera, valoarea in freq.items():
#     if valoarea > max:
#         max = valoarea
#         litera_max = litera
# print(max, litera_max)

# from collections import Counter
# freq = Counter(cuvant)
# print(freq.most_common(1))
"""=================================================================================================="""


"""
# =====================================================================

# Partea II — Stiva (LIFO)

# =====================================================================
"""

# TODO: Ex 1 — Simulează butonul Undo al unui editor. Parcurge acțiunile de
#  mai jos: o acțiune obișnuită se adaugă în istoric, iar „undo” anulează
#  ultima acțiune rămasă. Afișează istoricul final.
actiuni = ["scrie a", "scrie b", "undo", "scrie c", "scrie d", "undo", "undo", "scrie e"]
# istoric = []
# for actiune in actiuni:
#     if actiune == 'undo':
#         istoric.pop()
#     else:
#         istoric.append(actiune)
#     print(istoric)
"""=================================================================================================="""

# TODO: Ex 2 — Pentru fiecare șir de mai jos, verifică dacă parantezele
#  (), [] și {} sunt deschise și închise corect. Afișează șirul și True/False.
# expresii = ["([]{})", "([)]", "((()", "{[()()]}", "", ")("]
# # pas 1 - creeam o lista booleana, care o sa aiba rezoltatele
# # pas 2 - facem un for dupa fiecare expresie
# # pas 3 - veficam daca paranteza curenta are pereche
# # pas 4 - daca paranteza are pereche atunci in lista de raspunsuri punem true, else false
# raspunsuri:list[bool] = []
# paranteze = {')': '(', ']': '[', '}': '{'}
# for expresie in expresii:
#     stiva = []
#     expresie_valida = True
#     for paranteza in expresie:
#         if paranteza in '([{':
#             stiva.append(paranteza)
#         elif not stiva or stiva.pop() != paranteze[paranteza]:
#             raspunsuri.append(False)
#             expresie_valida = False
#             break
#         print(stiva)
#     raspunsuri.append(expresie_valida)
#     print(expresie_valida)
#     print("*" * 50)
#
# print(raspunsuri)
"""=================================================================================================="""

# TODO: Ex 3 — Expresii valide (etapa locală 2023, varianta scurtă). Pentru
#  expresia de mai jos, afișează poziția (de la 0) primei paranteze care
#  strică expresia. Dacă expresia este corectă, afișează -1.
# expresie = "(2 + 3) * [4 - (5 + 1]) + 7"
# paranteze = {')': '(', ']': '[', '}': '{'}
# pos = -1
# stiva = []
# for i, c in enumerate(expresie):
#     if c not in '([{}])':
#         continue
#     if c in '([{':
#         stiva.append(c)
#     elif not stiva or stiva.pop() != paranteze[c]:
#         pos = i
#         break
# print(pos)
"""=================================================================================================="""


"""
# =====================================================================

# Partea III — Stiva monotonă

# =====================================================================
"""

# TODO: Ex 1 — Pentru fiecare zi din lista de mai jos, afișează câte zile
#  trebuie așteptate până la o temperatură mai mare. Dacă nu există o
#  astfel de zi, scrie 0. Soluția trebuie să parcurgă lista o singură dată.
# temperaturi = [73, 74, 75, 71, 69, 72, 76, 73]
# for i in range(len(temperaturi)):
#     zile = 0
#     for j in range(i + 1, len(temperaturi)):
#         if temperaturi[j] > temperaturi[i]:
#             zile = j - i
#             break
#     print(zile)


"""=================================================================================================="""

# TODO: Ex 2 — Pentru fiecare număr din lista de mai jos, afișează primul
#  număr mai mare aflat în dreapta lui. Dacă nu există, scrie -1.
numere = [4, 5, 2, 10, 8, 1, 6]
# rez = []
# for i in range(len(numere)):
#     nr = -1
#     for j in range(i+1, len(numere)):
#         if numere[j] > numere[i]:
#             nr = numere[j]
#             break
#     rez.append(nr)
# print(rez)
rez = [-1] * len(numere)
stiva = []
for i, x in enumerate(numere):
    while stiva and numere[stiva[-1]] < x:
        rez[stiva.pop()] = x
    stiva.append(i)
print(rez)
"""=================================================================================================="""


"""
# =====================================================================

# Partea IV — Coada (FIFO)

# =====================================================================
"""

# TODO: Ex 1 — Simulează o coadă la casă. Parcurge evenimentele de mai jos:
#  „vine X” pune persoana la coadă, „pleacă” servește prima persoană din
#  coadă. Afișează, în ordine, persoanele servite și cine a rămas la coadă.
evenimente = ["vine Ana", "vine Dan", "pleacă", "vine Ion", "vine Mia", "pleacă", "pleacă", "vine Eva"]


"""=================================================================================================="""

# TODO: Ex 2 — Compară timpul necesar pentru a goli o coadă de 100 000 de
#  elemente în două moduri: cu list.pop(0) și cu deque.popleft().
#  Afișează cei doi timpi în secunde, cu 3 zecimale.


"""=================================================================================================="""


"""
# =====================================================================

# Partea V — Coada → BFS pe grilă

# =====================================================================
"""

# TODO: Ex 1 — Harta de mai jos are 0 = liber și 1 = zid. Afișează lungimea
#  celui mai scurt drum din colțul stânga-sus în colțul dreapta-jos, mergând
#  doar sus/jos/stânga/dreapta pe celule libere. Dacă nu există drum, -1.
harta = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
]


"""=================================================================================================="""

# TODO: Ex 2 — Pe aceeași hartă, afișează câte celule libere pot fi atinse
#  pornind din colțul stânga-sus (inclusiv celula de start).


"""=================================================================================================="""

# TODO: Ex 3 — Pădurea de mai jos are 1 = copac, 2 = copac care arde,
#  0 = apă. În fiecare minut focul trece la copacii vecini (sus/jos/stânga/
#  dreapta). Afișează după câte minute ard toți copacii. Dacă un copac nu
#  poate fi atins de foc, afișează -1.
padure = [
    [2, 1, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 2],
]
