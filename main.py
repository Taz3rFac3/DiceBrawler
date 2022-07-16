import pygame
from fighter import Fighter
pygame.init()

# create game window
SCREEN_WDITH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WDITH, SCREEN_HEIGHT))
pygame.display.set_caption("Dice Brawler")

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#load background image
bg_image = pygame.image.load("assets/images/background/background.jpg")

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WDITH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

# create two instance of fighters
fighter_1 = Fighter(100,350)
fighter_2 = Fighter(800,350)


#game loop
run = True

while run:

    clock.tick(FPS)

    #draw background
    draw_bg()

    #move fighters
    fighter_1.move(SCREEN_WDITH)
    #fighter_2.move()

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    #update display
    pygame.display.update()
#exit pygame
pygame.quit()

