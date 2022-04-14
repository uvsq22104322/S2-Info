import tkinter as tk

##################
# Constantes
# nouvelle constant compteur 

LARGEUR = 600
HAUTEUR = 400
compteur = 0


###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    #Variable cercle défini en tant que global pour pouvoir l'appeler dans la fonction rebond
    global cercle
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    #Ajout de la variable compteur nécessaire pour arreter la balle au bout de 30 rebonds
    global compteur
    if compteur < 10:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    #Lorsque la balle rebondit (coordonnées supérieures ou inférieures) sur un côté, elle change de couleur en fonction du bord touché
    global balle, compteur, cercle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if y0 <= 0:
        balle[2] = -balle[2]
        canvas.itemconfig(cercle, fill="red")
        compteur += 1
    elif x1 >= 600:
        balle[1] = -balle[1]
        canvas.itemconfig(cercle, fill="green")
        compteur += 1
    elif y1 >= 400:
        balle[2] = -balle[2]
        canvas.itemconfig(cercle, fill="blue")
        compteur += 1
    elif x0 <= 0:
        balle[1] = -balle[1]
        canvas.itemconfig(cercle, fill="yellow")
        compteur += 1


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

#widgets traits bord visiblent
canvas.create_rectangle(0, 395, 600, 400, fill="blue")
canvas.create_rectangle(595, 0, 600,400, fill="green")
canvas.create_rectangle(0, 0, 5, 400, fill="yellow")
canvas.create_rectangle(0, 0, 600, 5, fill="red")


# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
