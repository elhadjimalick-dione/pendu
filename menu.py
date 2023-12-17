import pygame
import sys
import random

pygame.init()

largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Menu")

blanc = (255, 255, 255)
noir = (0, 0, 0)

background = pygame.image.load("bag.png")
background = pygame.transform.scale(background, (largeur, hauteur))

bouton_menu_rect = pygame.Rect(300, 200, 200, 50)
bouton_menu_couleur = blanc
texte_bouton = "jouer"
font = pygame.font.Font(None, 36)
texte_surface = font.render(texte_bouton, True, noir)
texte_rect = texte_surface.get_rect(center=bouton_menu_rect.center)

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if bouton_menu_rect.collidepoint(event.pos):
            
                nom_joueur = input("Entrez votre nom: ")

            
                score_joueur = random.randint(0, 1000)

                
                with open("scores.txt", "a") as file:
                    file.write(f"{nom_joueur}: {score_joueur}\n")

            
                import niveau

    
    fenetre.blit(background, (0, 0))
    pygame.mixer.music.play(1)

    pygame.draw.rect(fenetre, bouton_menu_couleur, bouton_menu_rect)
    fenetre.blit(texte_surface, texte_rect)
    
    pygame.display.flip()