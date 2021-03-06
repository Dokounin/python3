# exercice-algo-03

# Remarque 3.1
# Il existe pleins d'algorithmes de tri de données plus ou moins efficace.
# Un des algorithme le moins efficace est le tri bulle.
# Mais il a le mérite d'être « facile » à implémenter car il est très intuitif.
#
# 1. Prenez une liste de nombre.
# 2. Comparez le premier élément avec le second élément.
# 3. Si le premier élément est plus grand que le second, inversez leur position.
# 4. Passez à l'élément suivant et recommencez la comparaison.
# 5. Recommencez l'étape 4 jusqu'à la fin de la liste.
# 6. Si vous avez fini de parcourir la liste, recommencez depuis l'étape 2 jusqu'à ce qu'il n'y ait plus besoin d'intervertir aucun élément.
#
# « Facile », non ?

# exo 3.1
# Triez la liste suivante en ordre croissant en utilisant l'algorithme du tri bulle puis affichez la liste.
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 3.1
while True:
    moved = False
    for i in range(0, len(my_list)- 1):
        a = my_list[i]
        b = my_list[i + 1]

        if a > b:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            moved = True
        
    if moved == False:
        break

print(my_list)
