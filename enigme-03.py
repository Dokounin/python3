"""
12. Les boulets de canon
Un artilleur dispose de boulets de canon répartis dans un carré par-
fait. Pour réduire l'encombrement au sol, l'artilleur réussit à empiler ses
boulets pour former une belle pyramide à base carré.
 Quel est le plus petit nombre de boulets possible dont dispose
 l'artilleur ? 
"""

#une boucle dans un liste(tableau)
# on démarre à 2 pour éviter que la boucle for principale  trouve 1 comme résultat
#
squares = [i ** 2 for i in range(2, 101)]

#fait la même chose avec une boucle for
#squares = []
#for i in range(1, 101):
#    squares.append(i ** 2)

pyramid = 1

for bullet in squares:
    pyramid += bullet

    if pyramid in squares:
        print(pyramid)
        break
