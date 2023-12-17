import pygame
import random
import sys

pygame.init()

largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu du Pendu")

blanc = (255, 255, 255)
noir = (0, 0, 0)


images_pendu = [pygame.image.load(f"./images_pendu/{i}.png") for i in range(1, 8)]

current_image_index = 0

background = pygame.image.load("écran.png")
background = pygame.transform.scale(background, (largeur, hauteur))


try:
    with open("mots.txt", "r") as fichier_mots:
        mots = fichier_mots.read().splitlines()

    if len(mots) < 15:
        raise FileNotFoundError
except FileNotFoundError:
    mots = ['python', 'programmation', 'jeu', 'pendu', 'pygame', 'informatique', 'developpement', 'ordinateur',
            'algorithme', 'intelligence', 'artificielle', 'apprentissage', 'machine', 'code', 'openai']
    with open("mots.txt", "w") as fichier_mots:
        fichier_mots.write('\n'.join(mots))


mot = random.choice(mots)
mot_affiche = ['_'] * len(mot) 

font = pygame.font.Font(None, 36)

essais_restants = 7  

running = True

while running:
    fenetre.blit(background, (0, 0))

    texte = font.render(' '.join(mot_affiche), True, (255, 255, 255))
    fenetre.blit(texte, (20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            lettre = pygame.key.name(event.key).lower()
            if lettre not in mot:
                print("Erreur : La lettre ne se trouve pas dans le mot.")
                essais_restants -= 1
                if essais_restants == 0:
                    print("Dommage ! Vous avez perdu. Le mot était :", mot)
                    running = False
                else:
                    current_image_index += 1

            else:
                for i in range(len(mot)):
                    if mot[i] == lettre:
                        mot_affiche[i] = lettre

                if '_' not in mot_affiche:
                    print("Félicitations ! Vous avez gagné.")
                    running = False

    # Affichage de l'image du pendu correspondante
    fenetre.blit(images_pendu[current_image_index], (largeur //  200, 225))

    keys = pygame.key.get_pressed()

    pygame.display.update()

pygame.quit()
sys.exit()