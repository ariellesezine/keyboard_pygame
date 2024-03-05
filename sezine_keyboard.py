import pygame
from pygame.locals import *


# initialisation de pygame
pygame.init()

screen_width = 600
screen_height= 500

screen = pygame.display.set_mode((screen_width, screen_height))
white =  ( 255, 255, 255)


screen.fill(white)

# Définir la police et la taille du texte
police = pygame.font.Font(None, 20)

position_y =  screen_height//10
# fonction pour ecrire sur la fenetre
def write(texte,position_y):
   
    # Rendre le texte dans une surface
    texte_surface = police.render(texte, True, (150, 0, 150))
    # on affiche le texte a l'ecran
    screen.blit(texte_surface , (screen_width //10, position_y))

    # Mettre à jour l'affichage
    pygame.display.flip()


run=True
while run:
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.unicode== '':
                if event.key == pygame.K_UP:
                    text = " vous avez appuyer  la fleche vers le haut d'identifiant    "
                    t= str(event.key)
                    text +=t
                    write(text,position_y)
                    position_y+=15

                if event.key == pygame.K_DOWN:
                    text = " vous avez appuyer  la fleche vers le bas d'identifiant     "
                    t= str(event.key)
                    text +=t
                    write(text,position_y)
                    print(event.key)
                    position_y+=15

                if event.key == pygame.K_LEFT:
                    text = " vous avez appuyer  la fleche vers la gauche d'identifiant     "
                    t= str(event.key)
                    text +=t
                    write(text,position_y)
                    position_y+=15

                if event.key == pygame.K_RIGHT:
                    text = " vous avez appuyer  la fleche vers la droite d'identifiant      "
                    t= str(event.key)
                    text +=t
                    write(text,position_y)
                    position_y+=15

                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    text = " vous avez appuyer sur Ctrl d'identifiant  "
                    t= str(event.key)
                    text +=t
                    write(text,position_y)
                    position_y+=15

                if event.key == pygame.K_LSHIFT or event.key== pygame.K_RSHIFT:
                    text = " vous avez appuyer sur shift d'identifiant      "
                    t= str(event.key)
                    text +=t
                    write(text,position_y)
                    position_y+=15

                if event.key == pygame.K_CAPSLOCK:
                    text = " vous avez appuyer sur Caps d'identifiant      "
                    t= str(event.key)
                    text +=t
                    write(text,position_y)
                    position_y+=15
                   
            elif event.unicode!='':
                unicode_char = event.unicode
                #print(f"ID de la touche : {event.key}")
                #print(f"Unicode de la touche : {unicode_char}")
                text= "Vous avez appuyer sur : "+ unicode_char
                t=" d'identifiant :  " + str(event.key)
                text+=t
                write(text,position_y)
                position_y+=15
     
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.flip()           
            

pygame.quit()
