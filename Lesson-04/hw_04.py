# Lecția 04 — Condiții (if / elif / else)
# Tema pentru acasă


"""
# =====================================================================

# Partea I — Operatori aritmetici

# =====================================================================
"""

# TODO: Ex 1 — Date a=2, b=3, c=4, d=6.
#  Calculează expresia (a * b * c + d) / 3 și afișează rezultatul.
# a=2
# b=3
# c=4
# d=6
#
# print((a * b * c + d) / 3)
"""=================================================================================================="""

# TODO: Ex 2 — Cere un număr de la utilizator și afișează cubul lui
#  (numărul ridicat la puterea 3).
# nr = int(input("Da-mi un numar:"))
#
# print(nr ** 3)
"""=================================================================================================="""

# TODO: Ex 3 — Cere un număr de la utilizator.
#  Afișează True dacă numărul este divizibil cu 5, False în caz contrar.
# nr = int(input("Da-mi un numar:"))
#
# if nr % 5 == 0:
#     print(True)
# else:
#     print(False)
"""=================================================================================================="""

# TODO: Ex 4 — Cere un cuvânt de la utilizator.
#  Afișează True dacă lungimea cuvântului este divizibilă cu 3,
#  False în caz contrar.
# cuvant = input("Da-mi un cuvant:")
#
# if len(cuvant) % 3 == 0:
#     print(True)
# else:
#     print(False)
"""=================================================================================================="""

# TODO: Ex 5 — Cere un număr de minute (ex: 145).
#  Calculează și afișează câte ore complete sunt și câte minute rămân.
#  Exemplu: 145 minute  ->  2 ore și 25 minute
# minute = int(input("Da-mi un numar de minute:"))
#
# print(f"{minute}  ->  {minute // 60} ore si {minute % 60} minute")
"""=================================================================================================="""


"""
# =====================================================================

# Partea II — if / elif / else

# =====================================================================
"""

# TODO: Ex 1 — Cere un cuvânt.
#  Dacă ultima literă a cuvântului este o vocală,
#  afișează "Se termină cu vocală", altfel "Se termină cu consoană".
# cuvant = input("Da-mi un cuvant:")
#
# if cuvant[-1] in "aeiou":
#     print("Se termina cu vocala")
# else:
#     print("Se termina cu consoana")
"""=================================================================================================="""

# TODO: Ex 2 — Cere un număr de la utilizator. Afișează:
#   - "Pozitiv" dacă numărul este mai mare decât 0
#   - "Negativ" dacă numărul este mai mic decât 0
#   - "Zero"    dacă numărul este 0
# nr = int(input("Da-mi un numar:"))
#
# if nr > 0:
#     print("Pozitiv")
# elif nr == 0:
#     print("Zero")
# elif nr < 0:
#     print("Negativ")
"""=================================================================================================="""

# TODO: Ex 3 — Cere o temperatură (în grade Celsius) și afișează categoria:
#   < 0    ->  "Înghețat"
#   < 15   ->  "Rece"
#   < 25   ->  "Plăcut"
#   altfel ->  "Cald"
# temperatura = int(input("Da-mi o temperatura in grade celsius:"))
#
# if temperatura < 0:
#     print("Inghetat🥶")
# elif temperatura < 15:
#     print("Rece😰")
# elif temperatura < 25:
#     print("Placut😎")
# else:
#     print("Cald🥵")
"""=================================================================================================="""

# TODO: Ex 4 — Cere un număr și afișează câte cifre are:
#   < 10    ->  "o cifră"
#   < 100   ->  "două cifre"
#   < 1000  ->  "trei cifre"
#   altfel  ->  "mai mult de trei cifre"
# nr = int(input("Da-mi un numar:"))
#
# if nr < 10:
#     print("O cifra")
# elif nr < 100:
#     print("Doua cifre")
# elif nr < 1000:
#     print("Trei cifre")
# else:
#     print("Mai multe cifre")
"""=================================================================================================="""

# TODO: Ex 5 — Primești un nume de fișier ca "document.pdf".
#  În funcție de ultimele 3 caractere (extensia), afișează tipul fișierului:
#   "pdf"  ->  "Document PDF"
#   "jpg"  ->  "Imagine"
#   "mp3"  ->  "Audio"
#   "mp4"  ->  "Video"
#   altfel ->  "Tip necunoscut"
#  Folosește slicing pentru a extrage ultimele 3 caractere.
# fisier = input("Da-min un nume de fisier:")
#
# if fisier[-3:] == "pdf":
#     print("Documente PDF")
# elif fisier[-3:] == "jpg":
#     print("Imagine")
# elif fisier[-3:] == "mp3":
#     print("Audio")
# elif fisier[-3:] == "mp4":
#     print("Video")
# else:
#     print("Tip necunoscut")
"""=================================================================================================="""


"""
# =====================================================================

# Partea III — Operatori logici

# =====================================================================
"""

# TODO: Ex 1 — Cere un număr de la utilizator.
#  Afișează True dacă numărul este negativ SAU zero, altfel False.
# nr = int(input())
#
# if nr == 0 or nr<0:
#     print(True)
# else:
#     print(False)
"""=================================================================================================="""

# TODO: Ex 2 — Cere o vârstă de la utilizator.
#  Afișează "Acces gratuit" dacă vârsta este sub 7 ani SAU peste 65 de ani,
#  altfel "Plătește bilet".
# n = int(input("Da-mi varsta ta:"))
#
# if n < 7 or n  < 65:
#     print("Gratuit")
# else:
#     print("Plateste biletul")
"""=================================================================================================="""

# TODO: Ex 3 — Care este rezultatul expresiei?
#
#     10 >= 5 * 2 and 3 < 4
#  Aceasta expresie are valoarea de True
"""=================================================================================================="""

# TODO: Ex 4 — Care este rezultatul expresiei?
#
#     15 - 3 * 2 > 8 and not (3 + 2 != 5)
# Aceasta expresie are valoare de True
"""=================================================================================================="""

# TODO: Ex 5 — Care este rezultatul expresiei?
#
#     not 'a' in 'xyz' and 3 ** 2 > 8 or 15 // 4 == 3
# Aceasta expresie are valoare de True