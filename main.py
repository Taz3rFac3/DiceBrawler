import pygame
from fighter import Fighter

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dice Brawler")

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#define colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0] #player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 200

#define fighter variables
FIRE_WIZARD_SIZE = 153
FIRE_SCALE = 1.5
FIRE_OFFSET = [72, 3]
FIRE_DATA = [FIRE_WIZARD_SIZE, FIRE_SCALE, FIRE_OFFSET]
ICE_WIZARD_SIZE = 153
ICE_SCALE = 1.5
ICE_OFFSET = [25, 3]
ICE_DATA = [ICE_WIZARD_SIZE, ICE_SCALE, ICE_OFFSET]

#load background image
bg_image = pygame.image.load("assets/images/background/background.jpg")

#load character images
fire_wizard_sheet = pygame.image.load('assets/images/wizard_fire/fire_wizard_sprite.png').convert_alpha()
ice_wizard_sheet = pygame.image.load('assets/images/wizard_ice/ice_wizard_sprite.png').convert_alpha()

#load victory image
victory_img = pygame.image.load('assets/images/victory/victory.png').convert_alpha()

#define number of steps in each animation
FIRE_WIZARD_STEPS = [1, 3, 4, 1, 4, 3]
ICE_WIZARD_STEPS = [1, 3, 4, 1, 4, 3]

#define fonts
count_font = pygame.font.Font("assets/fonts/Turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/Turok.ttf", 30)

#function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

#function for drawing healthbars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, BLUE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, BLUE, (x, y, 400 * ratio, 30))

#create two instance of fighters
fighter_1 = Fighter(1, 100, 350, False, FIRE_DATA, fire_wizard_sheet, FIRE_WIZARD_STEPS)
fighter_2 = Fighter(2, 800, 350, True, ICE_DATA, ice_wizard_sheet, ICE_WIZARD_STEPS)

#game loop
run = True

while run:
    #set clock
    clock.tick(FPS)

    #draw background
    draw_bg()

    #show player health bars
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #update countdown
    if intro_count <= 0:
        #move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)

    else:
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()

    #update fighters
    fighter_1.update()
    fighter_2.update()

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #check for player defeat
    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        #display victory image
        screen.blit(victory_img, (315, 150 ))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            fighter_1 = Fighter(1, 100, 350, False, FIRE_DATA, fire_wizard_sheet, FIRE_WIZARD_STEPS)
            fighter_2 = Fighter(2, 800, 350, True, ICE_DATA, ice_wizard_sheet, ICE_WIZARD_STEPS)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()

#exit pygame
pygame.quit()

