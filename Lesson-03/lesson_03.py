"""
# =====================================================================

# Partea I — Indexare și Slicing

# =====================================================================
"""

# TODO: Ex 1 — Cere utilizatorului un cuvânt și afișează:
#  a) primul caracter
#  b) ultimul caracter (folosind index negativ)
#  c) al treilea caracter
# word = "Python"
#
# print(word[0])
# print(word[-1])
# print(word[2])
"""=================================================================================================="""

# TODO: Ex 2 — Cere utilizatorului un text și un număr N. Apoi afișează:
#  a) primele N caractere din text
#  b) ultimele N caractere din text (folosind index negativ)
# word = "PYTHON"
# n = 3
#
# print(word[0:n])
# print(word[n:])
"""=================================================================================================="""

# TODO: Ex 3 — Cere utilizatorului un text de cel puțin 10 caractere.
#  Pentru un text precum "PROGRAMARE", afișează:
#  a) primele 4 caractere → "PROG"
#  b) ultimele 5 caractere → "AMARE"
#  c) caracterele de la poziția 3 până la 8 → "GRAMA"
# word = "PROGRAMARE"
#
# print(word[0:3])
# print(word[-5:])
# print(word[3:8])
"""=================================================================================================="""

# TODO: Ex 4 — Cere utilizatorului un text și afișează doar caracterele
#  de pe pozițiile pare (0, 2, 4, ...).

"""=================================================================================================="""

# TODO: Ex 5 — Cere utilizatorului un text și afișează-l fără
#  primul și fără ultimul caracter.
# word = "programare"
#
# print(word[1:-1])

"""=================================================================================================="""

# TODO: Ex 6 — Cere utilizatorului un cuvânt și afișează-l în ordine inversă.
# word = "programare"
#
# print(word[::-1])

"""=================================================================================================="""

# TODO: Ex 7 — Cere utilizatorului un cuvânt și verifică dacă este palindrom.
#  Un palindrom se citește la fel în ambele direcții (ex: "ana", "cojoc").
#  Afișează True sau False.
# a = "ANA1"
# if a == a[::-1]:
#     print(f"{a} este palindrom")
# else:
#     print(f"{a} nu este palindrom")

"""=================================================================================================="""

# TODO: Ex 8 — Cere utilizatorului un text și afișează o combinație
#  formată din primele 3 caractere lipite cu ultimele 3 caractere.
#  Exemplu: "programare" → "proare"
# word = "programare"
#
# print(word[:3] + word[-3:])

"""=================================================================================================="""


"""
# =====================================================================

# Partea II — Metode de string

# =====================================================================
"""

# TODO: Ex 1 — Cere utilizatorului un text și afișează:
#  a) tot textul cu MAJUSCULE
#  b) tot textul cu minuscule
#  c) textul cu Fiecare Cuvânt Capitalizat
#  d) textul cu doar primul caracter mare
# word = "programare"
#
# print(word.upper())
# print(word.lower())
# print(word.title())
# print(word.capitalize())


"""=================================================================================================="""

# TODO: Ex 2 — Pentru text = "data analytics with python is fun"
#  cere utilizatorului un substring și afișează:
#  a) dacă substring-ul există în text (True/False)
#  b) poziția primei apariții
#  c) câte apariții are în text
# text = "data analytics with python is fun"
# sub_string = "python"
#
# print(sub_string in text)
# print(text.find(sub_string))
# print(text.count(sub_string))
"""=================================================================================================="""

# TODO: Ex 3 — Cere utilizatorului un text și numără câte vocale conține
#  (a, e, i, o, u). Afișează totalul.
# sir = "ajvkmrkmeoshfea"
# total = 0
#
# for i in "aeiou":
#     total += sir.count(i)
#
# print(total)
"""=================================================================================================="""

# TODO: Ex 4 — Cere utilizatorului un text și verifică:
#  a) dacă textul conține doar cifre (True/False)
#  b) dacă textul conține doar litere (True/False)
# text = "programare"
#
# print(text.isdigit())
# print(text.isalpha())
"""=================================================================================================="""

# TODO: Ex 5 — Cere utilizatorului un text și un cuvânt.
#  Înlocuiește toate aparițiile cuvântului în text cu "****".
# text = "ana are mere la ana"
#
# print(text.replace("ana", "****"))
"""=================================================================================================="""

# TODO: Ex 6 — Cere utilizatorului o propoziție și numără câte cuvinte
#  conține.
#  Hint: folosește .count() pe caracterul spațiu și adaugă 1.
# text = "ana are mere la ana"
#
# print(text.count(" ")+1)

"""=================================================================================================="""

# TODO: Ex 7 — Cere utilizatorului separat numele și prenumele.
#  Generează un username format din primul caracter al numelui +
#  tot prenumele, totul cu litere mici.
#  Exemplu: "Ana" + "Popescu" → "apopescu"
text = "    Ana Popescu    "

# Pas 1
text = text.strip().lower()
# Pas 3, aflu pozitia
pos = text.find(" ") + 1
# Pas 2
print(text[0] + text[pos:])
"""=================================================================================================="""