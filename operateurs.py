# + - * /
result = 123 + 4.14
print(result)

# ()
result = (1 + 2) * 3
print(result)

# // % **
# division entière
result = 1 // 3
print(result)

# modulo
result = 10 % 3
print(result)

result = 13 % 2
print(result)

# puissance
# dans certains langages c'est : ^, pow()
result = 3 ** 3
print(result)

# racine carrée
result = 3 ** (1 / 2)
print(result)

# racine cubique
result = 3 ** (1 / 3)
print(result)

# | = ou
# & = et
# 0 | 0       0
# 0 | 1       1
# 1 | 0       1
# 1 | 1       1

# 0 & 0       0
# 0 & 1       0
# 1 & 0       0
# 1 & 1       1

# 00000000    0
# 00000001    1
# 00000010    2
# 00000011    3
# 00000100    4
# 00000101    5
# 00000110    6
# 00000111    7

# << 00001110     14
# >> 00000011     3


#     00000011    3
# |   00000100    4
# =   00000111    7

#     00000011    3
# &   00000100    4
# =   00000000    0result = True and True # True
result = False and True # False
result = True and False # False
result = False and False # False
result = True and True # True
result = False and True # False
result = True and False # False
result = False and False # False

# s'il n'y a que des "and", l'ordre n'est pas important
result = True and False and True and False # False

# opérateur booléen "or"
result = True or True # True
result = False or True # True
result = True or False # True
result = False or False # False

# s'il n'y a que des "or", l'ordre n'est pas important
result = True or False or True or False # True

# opérateur booléen "xor", le "ou exclusif"
result = True ^ True # False
result = False ^ True # True
result = True ^ False # True
result = False ^ False # False

# opérateurs composés

# n'existe pas en python
# c++ <=> c = c + 1

number = 42
# number = number + 1
n = 1
number += n

# encadrement