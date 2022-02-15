"""
    Cours : Structures conditionnelles
    Exercice : Racines d'un polynôme de degré deux
"""

a, b, c = 2, 5, 2
a, b, c = 1, -4, 5

if a == 0:  # polynome de degre 1
    assert (b != 0), "pas d'inconnue, pas de solution"
    nombreRacines = 1
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:  # le polynome admet deux racines reelles
    nombreRacines = 2
elif discriminant < 0:  # le polynome admet deux racines complexes conjuguees
    nombreRacines = 0
else:  # dans ce cas, le discriminant est nul et le polynome admet une solution double
    nombreRacines = 1

import math

assert (a != 0), "Le polynome est d'ordre 1. La solution est -c/b"

discriminant = b ** 2 - 4 * a * c
if discriminant > 0:  # le polynome admet deux racines reelles
    r1 = (-b - math.sqrt(discriminant)) / (2 * a)
    r2 = (-b + math.sqrt(discriminant)) / (2 * a)
elif discriminant < 0:  # le polynome admet deux racines complexes conjuguees
    r1 = complex(-b / (2 * a), - math.sqrt(-discriminant) / (2 * a))
    r2 = complex(-b / (2 * a), + math.sqrt(-discriminant) / (2 * a))
else:  # dans ce cas, le discriminant est nul et le polynome admet une solution double
    r1 = -b / (2 * a)

print(nombreRacines)
print(r1, r2)
