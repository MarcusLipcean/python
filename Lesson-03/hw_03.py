# Lecția 03 — String-uri în detaliu
# Tema pentru acasă


# Toate exercițiile se rezolvă DOAR cu f-string-uri, slicing
# și metode de string. Nicio bibliotecă externă.


"""
# =====================================================================

# Partea I — Indexare și Slicing

# =====================================================================
"""

# TODO: Ex 1 — Cere utilizatorului un cuvânt și afișează:
#  a) al doilea caracter
#  b) penultimul caracter (folosind index negativ)
#  c) (ADIȚIONAL) caracterul din mijlocul cuvântului
#     Hint: folosește operatorul de floor division  //  (împărțire întreagă)
#     Documentație: https://www.w3schools.com/python/python_operators_arithmetic.asp
# word = input("Da-mi un cuvant:")
#
# print(word[1])
# print(word[-2])
# print(word[len(word) // 2])
"""=================================================================================================="""

# TODO: Ex 2 — Cere utilizatorului o propoziție și afișează:
#  a) primul cuvânt (caracterele până la primul spațiu)
#  b) (ADIȚIONAL) ultimul cuvânt (caracterele de după ultimul spațiu)
#     Hint: trucul cu inversarea — inversează string-ul cu [::-1],
#     folosește .find(" ") pe varianta inversată, apoi taie cu slicing.
# propozitie = input("Da-mi o propozitie:")
# pos = propozitie.find(" ")
#
# print(propozitie[0:pos])
#
# pos = propozitie[::-1].find(" ")
# pos = pos - pos * 2
#
# print(propozitie[pos:])

"""=================================================================================================="""

# TODO: Ex 3 — Cere utilizatorului un text de cel puțin 11 caractere.
#  Pentru un text precum "INFORMATICA", afișează:
#  a) primele 4 caractere → "INFO"
#  b) ultimele 5 caractere → "ATICA"
#  c) caracterele de la poziția 2 până la 7 → "FORMA"
# word = input("Da-mi un cuvant:")
#
# print(word[:4])
# print(word[-5:])
# print(word[2:7])
"""=================================================================================================="""

# TODO: Ex 4 — Cere utilizatorului un text și afișează doar caracterele
#  de pe pozițiile impare (1, 3, 5, ...).
# word = input("Da-mi un cuvant:")
#
# print(word[1::2])
"""=================================================================================================="""

# TODO: Ex 5 — Cere utilizatorului un text și afișează-l fără
#  primele 2 și fără ultimele 2 caractere.
# word = input("Da-mi un cuvant:")
#
# print(word[2:-2])
"""=================================================================================================="""

# TODO: Ex 6 — Cere utilizatorului un text și inversează doar a doua jumătate.
#  Prima jumătate rămâne neschimbată.
#  Exemplu: "abcdef" → "abcfed"
# word = input("Da-mi un cuvant:")
#
# jum1 = word[0:len(word) // 2]
# jum2 = word[len(word) // 2:]
# jum2 = jum2[-1::-1]
#
# print(jum1 + jum2)

"""=================================================================================================="""

# TODO: Ex 7 — Cere utilizatorului un cuvânt și verifică dacă începe
#  și se termină cu aceeași literă (ignoră majuscule/minuscule).
#  Afișează True sau False.
#  Exemplu: "Ana" → True, "Pop" → False
# word = input("Da-mi un cuvant:")
#
# print(word[0] == word[-1])
"""=================================================================================================="""

# TODO: Ex 8 — Cere utilizatorului un cuvânt cu cel puțin 3 litere.
#  Înlocuiește prima și ultima literă cu caracterul "*".
#  Exemplu: "python" → "*ytho*"
# word = input("Da-mi un cuvant:")
#
# word = "*" + word[1:]
# word = word[:-1] + "*"
#
# print(word)
"""=================================================================================================="""


"""
# =====================================================================

# Partea II — Metode de string

# =====================================================================
"""

# TODO: Ex 1 — Cere utilizatorului un text care conține spații
#  la începutul și la sfârșitul lui. Apoi afișează:
#  a) lungimea textului înainte de curățare
#  b) lungimea textului după curățarea spațiilor
# prop = input("Da-mi o propozitie:")
#
# print(len(prop))
# print(len(prop.replace(" ", "")))
"""=================================================================================================="""

# TODO: Ex 2 — Cere utilizatorului un nume de fișier (ex: "raport.csv").
#  Găsește și afișează poziția punctului din nume.
# fisier = input("Da-mi un nume de fisier:")
#
# print(fisier.find(".")+1)


"""=================================================================================================="""

# TODO: Ex 3 — Cere utilizatorului un text și numără câte consoane conține.
#  (Toate literele care NU sunt vocale: a, e, i, o, u.)
#  Afișează totalul.
# text = input("Da-mi un text:")
#
# vocale = "aeiou"
# k = 0
#
# for j in range(0, len(text)):
#     if text[j] not in vocale and text[j] != " ":
#         k+=1
#
# print(k)
"""=================================================================================================="""

# TODO: Ex 4 — Cere utilizatorului un cod poștal și verifică:
#  a) dacă are exact 4 caractere
#  b) dacă conține doar cifre
#  Afișează rezultatul fiecărei verificări.
# cod = input("Da-mi un cod:")
#
# print(len(cod)==4)
# print(cod.isdigit())
"""=================================================================================================="""

# TODO: Ex 5 — Cere utilizatorului un nume complet (ex: "Ana Maria Popescu")
#  și afișează același text dar cu spațiile înlocuite cu underscore.
#  Exemplu: "Ana Maria Popescu" → "Ana_Maria_Popescu"
# nume = input("Da-mi un nume complet:")
#
# print(nume.replace(" ", "_"))
"""=================================================================================================="""

# TODO: Ex 6 — Cere utilizatorului un text format din mai multe propoziții
#  (separate prin punct). Numără câte propoziții conține.
# text = input("Da-mi un text:")
#
# k = 0
# 
# k+=text.count(".")
# k+=text.count("?")
# k+=text.count("!")
#
# print(k)
"""=================================================================================================="""