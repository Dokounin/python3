from ast import keyword
import random

firstname = "toto"
lastname = "pop"
number = random.randint(2, 10)

email = firstname + '.' + lastname + str(number) + '@example.com'
print(email)

new_emails = random.randint(0, 3)

if new_emails == 0:
    print("Vous n'avez pas de nouveux mails")
elif new_emails == 1:
    print("Vous avez reçu <strong>1</strong> nouveau mail" )
else:
    print("Vous avez reçu <strong>" + str (new_emails) + "</strong> nouveaux mails")

stock = random.randint(0, 15)

if stock == 0:
    print("Stock épuise")
elif stock == 1:
    print("Stock en tension : 1 pièce")
elif 1 < stock < 5:
    print(f"Stock en tension : {stock} pièces")
elif 5 <= stock < 10:
    print(f"Stock comfortable : {stock} pièces")
elif 10 <= stock:
    print(f"Stock en surnombre : {stock} pièces")

temperature = 10.1 + 0.1 + 0.1
print(temperature)
print(f"La temperature actuelle est de {temperature:.2f}° C")

electricite = True

# ne pas faire d'interpolation de variable booléenne si votre appli n'est pas en anglais
if electricite:
    print("electricite : vrai")
else:
    print("electricite : faux")

#@todo afficher age a partir de l'année de naissance 

print(f"La temperature actuelle est de {random.randint(0, 10)}° C")

texte = "foo bar baz"
# len == lenght == longueur
print(len(texte))

print(texte.find("ba"))
# recherche à partir du caractere 5 inclus
print(texte.find("ba", 5))
print(texte.find("banana"))

texte = "Bonjour Toto"

keyword = "Toto"

if  texte.find(keyword) >= 0:
    print("trouve")
else:
    print("non trouve")

keyword = "Titi"

if  texte.find(keyword) >= 0:
    print("trouve")
else:
    print("non trouve")

