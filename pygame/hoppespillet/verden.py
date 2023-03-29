import pygame
from spiller import Spiller
from hinder import Hinder

# pygame setup
pygame.init()
bredde = 1280 # bredden på vinduet
høyde = 720 # høyden på vinduet
vindu = pygame.display.set_mode((bredde, høyde))
klokke = pygame.time.Clock()
running = True
frames = 0

spiller1 = Spiller(høyde)
hindere = []

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    vindu.fill("purple")

    # --- LAG SPILLET DIT HER ---

    if frames == 180:
    # Hvis det har gått 180 frames / 3 sekunder:
        nytt_hinder = Hinder(bredde, høyde) # lag et nytt hinder-objekt
        hindere.append(nytt_hinder)  # legg det nye hinderet i listen over hindere
        frames = 0 # sett frames til å være 0

    # Flytter og tegner hindere:
    for hinder in hindere:
    # for hvert hinder i listen hindere:
        hinder.flytt()
        hinder.tegn(vindu)

    # Hopper hvis bruker trykker på mellomrom:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        spiller1.hopp()

    spiller1.fall() # spiller faller nedover
    spiller1.tegn(vindu) # tegner spiller

    frames += 1 # øker frames med 1

    # ----------

    # flip() the display to put your work on screen
    pygame.display.flip()
    klokke.tick(60)  # limits FPS to 60

pygame.quit()