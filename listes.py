from functools import partial
from re import M


text = "foo bar baz"
splitted_text = text.split(' ')

print(splitted_text)
print(len(splitted_text))
print(splitted_text[0])
print(splitted_text[1])
print(splitted_text[2])


index = 0
splitted_text[index] = 42
splitted_text[index + 1] = 123

# interversions de valeurs dans une liste (version python)
splitted_text[index], splitted_text[index + 1] = splitted_text[index + 1], splitted_text[index]

# interversion de valeur dans une liste (version plus classique)
tmp = splitted_text[index]
splitted_text[index] = splitted_text[index + 1]
splitted_text[index + 1] = tmp

splitted_text.append(123)
print(splitted_text)

#  [start:end:step]
#  start inclus
#  end inclus
result = splitted_text[0:2]
print(result)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ultrices et nisl ac porttitor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nulla maximus est ut felis faucibus, eu tristique nisi volutpat. Cras rhoncus ligula quis eros vehicula, eget malesuada velit scelerisque. Maecenas condimentum pellentesque lacus. Vestibulum in quam lorem. Proin vel sem sed nisi blandit molestie. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis a condimentum massa. Suspendisse eu tortor at mauris porta placerat nec quis arcu. Donec lacinia, erat quis congue maximus, nisl orci pulvinar dolor, eget tempor nulla metus in mauris. Integer congue massa vel molestie facilisis."
#  Suppression des points ( remplacement par une chaine de caractéres vide)
text = text.replace('.', '')
print(text)

#  #  Suppression des verguiles ( remplacement par une chaine de caractéres vide)
splitted_text = text.split(',')
my_text = ''.join(splitted_text)
#  Suppression des points ( remplacement par une chaine de caractéres vide)
splitted_text = text.split('.')
text = ''.join(splitted_text)

splitted_text = text.split(' ')
print(len(splitted_text))


#  tous les mots de l'index de 3 inclus à l'index 7 exlus
partial_list = splitted_text[3:7]
print(partial_list)
print(splitted_text)

#  tous les mots de l'index de 3 inclus à l'index 7 exlus avec un pas de 2
partial_list = splitted_text[3:7:2]
print(partial_list)
print(splitted_text)

start = 7
end = 3
if start >= end:
    start, end = end, start

print(start, end)
partial_list = splitted_text[start:end]

partial_list = splitted_text[-7:-3]

partial_list = splitted_text[-7:-3:2]
print(splitted_text)
print(partial_list)

# exo 
# 1. recuperez dans splitted_text les mots de l'index 35 à 49 inclus
print(splitted_text[35:50])
# 2. affichez le numéro du dernier index
dernier_index = len(splitted_text) - 1
print(dernier_index)
# 3. récuperez 1 mots sur 2 de l'index 0 au dernier index
print(splitted_text[0:dernier_index + 1:2])

# 4.
liste1 = splitted_text[0:dernier_index + 1:3]
print(liste1)
liste2 = splitted_text[1:dernier_index + 1:3]
print(liste2)
liste3 = splitted_text[2:dernier_index + 1:3]
print(liste3)

# tous les éléments
# valeurs pa défaut
# - start = 0
# - end = len()
# - step = 1
result = splitted_text[::]

# copie de tous les éléments en ordre inverse
result = splitted_text[::-1]

# copie de tous les éléments à partir de start jusqu'a la fin
start = 3
result = splitted_text[start:]

# copie de tous les éléments du déput jusqu'a end
end = 10
result = splitted_text[:end]

my_list = []
# mode pile
# equivalant d'un push()
my_list.append("foo")
print(my_list)
my_list.append(123)
print(my_list)
my_list.append(3.14)
print(my_list)

last_element = my_list.pop()
print(my_list)
print(last_element)

# mode file
my_list = ["toto", "titi", "tata", "tutu"]
client = my_list.pop(0)
print(my_list)
print(client)

# mode liste
print(my_list[0])
del(my_list[0])
print(my_list)

# pour ajoute dans la liste 
my_list.insert(1, "mémé")
print(my_list)

