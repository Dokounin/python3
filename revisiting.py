import random
# Exo 1.1
# Affichez le type de donnée des variables a et b.

a = 3.14
b = 3

# Réponse 1.1
print(type(a))
print(type(b))
# Exo 1.2
# En utilisant les variables a et b, affichez les chiffres après la virgule de la variable a.

a = 3.14
b = 3

# Réponse 1.2
print(round(a - b, 2))
# Exo 1.3
# Affichez le type de données de la variable n.

n = random.randint(10, 99) / 10

# Réponse 1.3
print(type(n))
# Exo 1.4
# Convertissez n en un nombre entier, stockez le résultat dans une variable et affichez le résultat.

n = random.randint(10, 99) / 10

# Réponse 1.4
n = int(n)
print(n)
# Exo 1.5
# Affichez :
# - les nombres avant la virgule de la variable n
# - les nombres après la virgule de la variable n

n = random.randint(10, 99) / 10

# Réponse 1.5
print(int(n))
print(n - int(n))
# Exo 1.6
# Stockez dans une variable si la variable n est un nombre entier ou non.

n = random.randint(10, 99) / 10
# Réponse 1.6
# is_int = n == int(n)
# print(is_int)
if n == int(n):
    print(n, ": le nombre est entier")
else:
    print(n, ": le nombre n'est pas entier")



# Exo 2.1
n = random.randint(0, 9)
print(n)
if n < 5:
    print("foo")

# Exo 2.2
if random.randint(0, 9) < 5:
    print("foo")

# Exo 2.3
while random.randint(0, 9) < 5:
    print("foo")