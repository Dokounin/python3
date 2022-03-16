nombre = -123
print(nombre)
print(type(nombre))

nombre = -3.14
print(nombre)
print(type(nombre))

nombre = "-123"
print(nombre)
print(type(nombre))

text = "lorem ipsum"
print(text)
print(type(text))

is_day = True
print(is_day)
print(type(is_day))

has_sugar = False
print(has_sugar)
print(type(has_sugar))

has_accepted_ula = None
print(has_accepted_ula)
print(type(has_accepted_ula))

html_code = '<h1>Titre de mon blog</h1>'
print(html_code)

nickname = "Jonh \"Dead\" Doe"
nickname = 'Jonh O\'Connar'
print(nickname)

multiline_text = """'foo'
"bar"
baz"""
print(multiline_text)

multiline_text = "foo \nbar \nbaz"
print(multiline_text)

nombre = "5"
print(type(nombre))
nombre = int(nombre)
print(nombre)
print(type(nombre))

nombre = "2.71"
print(type(nombre))
nombre = float(nombre)
print(nombre)
print(type(nombre))

nombre = 3.14
print(nombre)
print(type(nombre))
nombre = int(nombre)
print(nombre)
print(type(nombre))

nombre = 3
print(nombre)
print(type(nombre))
nombre = float(nombre)
print(nombre)
print(type(nombre))

texte = str(nombre)
print(texte)
print(type(texte))

my_var = 0
my_var = bool(my_var)
print(my_var)

my_var = 1
my_var = bool(my_var)
print(my_var)

my_var = 123
my_var = bool(my_var)
print(my_var)

my_var = ""
my_var = bool(my_var)
print(my_var)

my_var = "123"
my_var = bool(my_var)
print(my_var)

my_var = "-123"
my_var = bool(my_var)
print(my_var)

my_var = [123, "abc", False]
my_var = bool(my_var)
print(my_var)

my_var = [False]
my_var = bool(my_var)
print(my_var)

my_var = []
my_var = bool(my_var)
print(my_var)

# swap

#  méthode a moi
a = 42
b = 123

d = a
a = (b - d) + d
b = (b + d) - b


if a == 123 and b == 42:
    print("Vous avez reussi a interchanger les valeurs des variables")

#  méthode arithméthique

a = a + b
b = a - b
a = a - b

# méthode python et JS mais pas en PHP

a, b = b, a

#arrondi
import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

print(Decimal("0.5").quantize(Decimal("1")))

print(Decimal("1.5").quantize(Decimal("1")))