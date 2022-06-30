# exercice-algo-01

# note 1.1
#
# Connaissez-vous la suite de Fibonacci ?
# Cette suite est calculée en additionnant les nombres des deux rangs
# précédent. Le rang 0 et le rang 1 sont fixés à 0 et 1 respectivement.
#
# Voici la formule de la suite :
# F0 = 0
# F1 = 1
# Fn = Fn-2 + Fn-1
#
# Un démonstration rendra les choses plus claires.
#
# On a dit que les deux premiers rangs (c-à-d nombres) de la suite de
# Fibonacci étaient 0 et 1.
# On a donc :
# F0 = 0 et F1 = 1
# 
# Pour obtenir F2, on additionne F0 et F1.
# On a donc :
# F2 = F0 + F1 = 0 + 1 = 1
# Ce qui donne F2 = 1
#
# Pour obtenir F3, on additionne F1 et F2.
# On a donc :
# F3 = F1 + F2 = 1 + 1 = 2
# Ce qui donne F3 = 2
#
# Et ainsi de suite.
#
# Maintenant on peut généraliser.
# Pour obtenir Fn, on addition Fn-2 et Fn-1.
# Ce qui donne la formule :
# Fn = Fn-2 + Fn-1

# exo 1.1
#
# Ajoutez les 10 premiers nombres de la suite de Fibonacci, que vous
# aurez calculé « à la main », dans une liste. Puis affichez cette
# liste en utilisant une boucle de type « for each ».
# Note : la suite doit démarre à 0.

# réponse 1.1
liste_fibonacci = [0,1,1,2,3,5,8,13,21,34]

for i in liste_fibonacci:
    print(i)
# exo 1.2
#
# Reprenez votre boucle de type « for each » et modifiez-là de façon à
# utiliser un index et la fonction `range()` pour parcourir le liste
# des nombres de Fibonacci.

# réponse 1.2
for i in range(len(liste_fibonacci)):
    print(liste_fibonacci[i])

# exo 1.3
#
# Écrivez une fonction nommé `fibonacci_1_3()` qui :
# - renvoit `0` si on lui passe `0` en paramètre
# - renvoit `1` si on lui passe `1` en paramètre
# - renvoit `None` dans les autres cas
#
# Appelez votre fonction dans une boucle qui va de `0` à `2` en
# utilisant un index et la fonction `range()`.

# réponse 1.3
def fibonacci_1_3(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return None

for i in range(3):
    print(fibonacci_1_3(i))
# exo 1.4
#
# Reprenez votre fonction `fibonacci_1_3`, renommez-là `fibonacci_1_4`.
# Puis modifiez-là de façon à ce que la fonction :
# - renvoit la somme de `fibonacci_1_4(0)` et
# `fibonacci_1_4(1)` si on lui passe `2` en paramètre.
# - renvoit `None` dans les autres cas
#
# Appelez votre fonction dans une boucle qui va de `0` à `2` en
# utilisant un index et la fonction `range()`.

# réponse 1.4
def fibonacci_1_4(n):
    if n == 0 or n == 1:
        return n
    elif n == 2:
        return fibonacci_1_4(0) + fibonacci_1_4(1)
    else:
        return None

for i in range(4):
    print(fibonacci_1_4(i))
# exo 1.5
#
# Reprenez votre fonction `fibonacci_1_4`, renommez-là `fibonacci_1_5`.
# Puis modifiez-là de façon à ce que la somme de `fibonacci_1_4(0)` et
# `fibonacci_1_4(1)` utilise la vraiable `n` au lieu de valeurs
# constantes.
#
# Appelez votre fonction dans une boucle qui va de `0` à `2` en
# utilisant un index et la fonction `range()`.
#
# Indice : comment obtenir `0` quand `n == 2` ? Comment obtenir `1`
# quand `n == 2` ?
#
# ATTENTION : n'oubliez pas que maintenant vous devez appeler la
# fonction `fibonacci_1_5()` et plus `fibonacci_1_4()`.

# réponse 1.5
def fibonacci_1_5(n):
    if n == 0 or n == 1:
        return n
    elif n == 2:
        return fibonacci_1_5(n-2) + fibonacci_1_5(n-1)

for i in range(4):
    print(fibonacci_1_5(i))
# exo 1.6
#
# Reprenez votre fonction `fibonacci_1_5`, renommez-là `fibonacci_1_6`.
# Vous êtes mûr pour finir le travail et rendre la fonction
# opérationnelle au delà de `2`.
#
# Appelez votre fonction dans une boucle qui va de `0` à `10` en
# utilisant un index et la fonction `range()`.

# réponse 1.6
def fibonacci_1_6(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_1_6(n-2) + fibonacci_1_6(n-1)

for i in range(0, 10):
    print(fibonacci_1_6(i))
# exo 1.7
#
# Ça vous semble bon ? On va vérifier en créant un test.
#
# Appelez la fonction `fibonacci_1_6()` dans une boucle qui va de `0` à
# 10` en utilisant un index et la fonction `range()`. Utilisez cet index
# pour récupérer le nombre du rang correspondant dans la liste
# `fibonacci_numbers` puis comparez le résultat de votre fonction. S'il
# y a une différence, affichez un message d'erreur suivi du rang et des
# deux valeurs.

# réponse 1.7

for i in range(0, 10):
    if liste_fibonacci[i] == fibonacci_1_6(i):
        print("Rang", i, ":ok")
    else:
        print("Rang", i, ":erreur")


