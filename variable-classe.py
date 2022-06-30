class Chaise:
    # variable de classe
    nombre_pieds = 4

    def __init__(self, couleur: str):
        # variable d'instance
        self.couleur = couleur



chaise1 = Chaise('noir')
chaise2 = Chaise('noir')

# modif d'une variable de classe
Chaise.nombre_pieds = 3
# modif d'une variable d'instance
chaise1.couleur = 'blanc'


# création d'une varible d'instance
chaise1.nombre_pieds = 5

print('Chaise.nombre_pieds:', Chaise.nombre_pieds)

# lecture d'une variable de classe 
print('chaise1.nombre_pieds:', chaise1.nombre_pieds )
print('chaise1.couleur:', chaise1.couleur )

print('chaise2.nombre_pieds:', chaise2.nombre_pieds )
print('chaise2.couleur:', chaise2.couleur ) 