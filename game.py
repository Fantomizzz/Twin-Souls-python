import pygame

run_bool = True

screen = pygame.display.set_mode() #initialise l'écran

#écran de démarrage
fond_démarrage = pygame.image.load("fond_démarrage.png").convert() #load le fond et un bouton (les autres sont load après car utilisés dans d'autres menu)
nouvelle_partie = pygame.image.load("nouvelle_partie.png").convert_alpha()
load_sauvegarde = pygame.image.load("load_sauvegarde.png").convert_alpha()

démarrage = True  #initialise l'écran de démarrage
démarrage_suite = False

démarrer_string = "Cliquer pour continuer"  
pygame.font.init() 
démarrer_font = pygame.font.Font(None, 50) 
start_string = démarrer_font.render(démarrer_string, 1, (255, 255, 255)) 


#jeu

fond = pygame.image.load("fond.jpeg").convert() #load le fond


perso = pygame.image.load("perso.png").convert_alpha() #load le perso (le _alpha permets d'éviter que l'image est un fond)
x = 380  #coordonées du perso au début
y = 370

vie_1_perso = pygame.image.load("vie.png").convert_alpha() #load les vies 
vie_2_perso = pygame.image.load("vie.png").convert_alpha()
vie_3_perso = pygame.image.load("vie.png").convert_alpha()

argent_var = 0  #initialise l'argent 
pygame.font.init()  #initialize le font (pour afficher la variable argent)
argent_font = pygame.font.Font(None, 50) #caractéristique du fond (police et taille de ce qu'on veut afficher je cois)
argent = argent_font.render(str(argent_var), 1, (0, 0, 0)) #affiche notre variable (le (0,0,0) correspond à la couleur)


argent_image = pygame.image.load("argent.png").convert_alpha() #load l'icône qui symbolise notre argent (ici la pyramide violette)


menu_pause_bool = False #vérifie si le menu pause est ouvert
fond_menu = pygame.image.load("fond_noir.jpg").convert_alpha() #load le fond du menu pause
fond_menu.set_alpha(200)                                       # mets la transparence du fond à 200 
pygame.Surface.convert_alpha(fond_menu)                        # applique le changement de transparence 

reprendre = pygame.image.load("reprendre.png").convert_alpha() #load les images "exit" et "resume" du menu pause
exit_game = pygame.image.load("exit.png").convert_alpha() 


menu_inventaire_bool = False #vérifie si le menu "inventaire" est ouvert
carte = pygame.image.load("carte.png").convert_alpha()  
inventaire = pygame.image.load("inventaire.png").convert_alpha()
nb_menu = 2 #nombre de menu
menu_actuel = 0


while run_bool : #boucle infini qui garde le jeu ouvert
    for event in pygame.event.get(): #gère les évènements
        if event.type == pygame.QUIT: #si on appuie sur quitter(la croix pour fermer la fenêtre), la boucle s'arrête 
                run_bool = False

#écran de démarrage
    if démarrage:
        screen.blit(fond_démarrage, (0,0))
        screen.blit(start_string, (800, 920))
        keys = pygame.key.get_pressed() #vérifie si un bouton est pressé

        if event.type == pygame.MOUSEBUTTONDOWN or démarrage_suite:
            screen.blit(fond_démarrage, (0,0))
            screen.blit(fond_menu, (0,0))
            screen.blit(nouvelle_partie, (600,200))
            screen.blit(load_sauvegarde, (630,350))
            screen.blit(exit_game, (150,0))
            démarrage_suite = True

            if keys[pygame.K_m]:     #remplace le fait de pouvoir lancer le jeu pour le moment
                démarrage = False
                démarrage_suite = False

    else:

# config touche
        keys = pygame.key.get_pressed() #vérifie si un bouton est pressé

        
        if keys[pygame.K_ESCAPE]:  # si échap est pressé, ouvre le menu de pause
            pygame.time.wait(200)   # permets d'éviter que pygame considère qu'on a appuyé 2 fois alors qu'on appuie juste assez longtemps pour que la boucle s'éxécute 2 fois
            if menu_pause_bool == False: #ouvre le menu si il était fermé (active la boucle du menu)
                menu_pause_bool = True
                menu_inventaire_bool = False      #ferme le menu si il était ouvert (désactive la boucle)
                screen.blit(carte, (-8000,300))         #déplace les images du menu pour qu'elle ne soit plus visible
                screen.blit(inventaire, (-8000,300))


            else:
                menu_pause_bool = False      #ferme le menu si il était ouvert (désactive la boucle)
                screen.blit(fond_menu, (-8000, 0))   
                screen.blit(reprendre, (-8130, -150))
                screen.blit(exit_game, (-8130, -100))

        
        if menu_pause_bool == False:
            
            if keys[pygame.K_e]:        #touche e pour ouvrir le menu inventaire, carte...
                pygame.time.wait(200)   # permets d'éviter que pygame considère qu'on a appuyé 2 fois alors qu'on appuie juste assez longtemps pour que la boucle s'éxécute 2 fois
                if menu_inventaire_bool == False:     #ouvre le menu si il était fermé (active la boucle du menu)
                    menu_inventaire_bool = True
                else:
                    menu_inventaire_bool = False      #ferme le menu si il était ouvert (désactive la boucle)
                    screen.blit(carte, (-8000,300))         #déplace les images du menu pour qu'elle ne soit plus visible
                    screen.blit(inventaire, (-8000,300))

            if menu_inventaire_bool == False:
                
                 
                if keys[pygame.K_SPACE]:
                    y -= 300
                    screen.blit(fond, (0, 0))#réinitialise le fond
                    screen.blit(vie_1_perso, (0,0)) # affiche les vies aux coordonnées demandées
                    screen.blit(vie_2_perso, (80,0))
                    screen.blit(vie_3_perso, (160,0))
                    argent = argent_font.render(str(argent_var), 1, (0, 0, 0)) #affiche la variable argent
                    screen.blit(argent, (1820, 50))  # affiche aux coordonnées demandées
                    screen.blit(argent_image, (1700,15))

                    screen.blit(perso, (x,y))  #place le personnage à ses nouvelles coordonnées
                    pygame.display.flip() #mets l'écran à jour 

                    pygame.time.wait(900) 
                    y += 300
                    

                if keys[pygame.K_LEFT]:  #si flèche gauche pressé alors on déplace le joueur
                    x += -5
                elif keys[pygame.K_RIGHT]: #si flèche droite pressé
                    x += 5

#config image
        screen.blit(fond, (0, 0))#réinitialise le fond
    
        screen.blit(vie_1_perso, (0,0)) # affiche les vies aux coordonnées demandées
        screen.blit(vie_2_perso, (80,0))
        screen.blit(vie_3_perso, (160,0))


        argent = argent_font.render(str(argent_var), 1, (0, 0, 0)) #affiche la variable argent
        screen.blit(argent, (1820, 50))  # affiche aux coordonnées demandées
        screen.blit(argent_image, (1700,15))

        screen.blit(perso, (x,y))  #place le personnage à ses nouvelles coordonées


#config menu
        if menu_pause_bool:
            screen.blit(fond_menu, (0, 0))   #affiche le fond et les images des boutons du menu
            screen.blit(reprendre, (130, -150))
            screen.blit(exit_game, (130, -100))

        if menu_inventaire_bool:

            if menu_actuel % nb_menu == 0:      #affiche le menu 0 et prend en compte le cas où on dépasse le nombre de menu existant 
                screen.blit(carte, (800,300))

            if menu_actuel % nb_menu == 1:
                screen.blit(inventaire, (600,300))
           
            if keys[pygame.K_RIGHT]:           # permets de changer de menu (avec un minuteur pour éviter que pygame croit qu'on appuie plusieurs fois)
                menu_actuel += 1
                pygame.time.wait(250)

            if keys[pygame.K_LEFT]: 
                menu_actuel -= 1
                pygame.time.wait(250)


        
       
    pygame.display.flip() #mets l'écran à jour 







