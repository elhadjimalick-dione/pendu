import pygame
import sys

pygame.init()

largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("niveau")

blanc = (255, 255, 255)
noir = (0, 0, 0)

background = pygame.image.load("niveau.png")
background = pygame.transform.scale(background, (largeur, hauteur))

font = pygame.font.Font(None, 36)


bouton1_menu_rect = pygame.Rect(300, 200, 200, 50)
bouton1_menu_couleur = noir
texte_bouton1 = "difficile"
texte_surface1 = font.render(texte_bouton1, True, blanc)
texte_rect1 = texte_surface1.get_rect(center=bouton1_menu_rect.center)

bouton2_menu_rect = pygame.Rect(300, 300, 200, 50)
bouton2_menu_couleur = blanc
texte_bouton2 = "facile"
texte_surface2 = font.render(texte_bouton2, True, noir)
texte_rect2 = texte_surface2.get_rect(center=bouton2_menu_rect.center)

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if bouton1_menu_rect.collidepoint(event.pos):
                print("Difficile selected")
          
            
                import main
            elif bouton2_menu_rect.collidepoint(event.pos):
                print("Facile selected")
                import main

    
    fenetre.blit(background, (0, 0))

    
    pygame.draw.rect(fenetre, bouton1_menu_couleur, bouton1_menu_rect)
    fenetre.blit(texte_surface1, texte_rect1)

    pygame.draw.rect(fenetre, bouton2_menu_couleur, bouton2_menu_rect)
    fenetre.blit(texte_surface2, texte_rect2)

    
    pygame.display.flip()
    pygame.mixer.music.play(-1)  

pygame.quit()
sys.exit()
