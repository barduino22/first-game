import pygame
#https://www.pygame.org/docs/

pygame.init()

# bepaal de grootte van het scherm
window = (1024, 576)

# activeer de game loop
while True:
    #maak het game-window
    pygame.display.set_mode(window)

# check voor events
    events = pygame.event.get()
    pygame.display.flip()

    for e in events:
        # dit zorgt ervoor da ge uw scherm kunt sluiten
        # als ge u scherm ni gesloten krijgt moet ctrl + c doen in de terminal
        if e.type == pygame.QUIT:
            quit()

        