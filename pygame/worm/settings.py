import pygame
import math, time
from random import randint

WindowWidth = 1024
WindowHeight = 768
BackgroundHeight = 708

rock_files = ["resources/rock1.png","resources/rock2.png","resources/rock3.png"]
Direction = ("Up", "Down", "Left", "Right")

# returns random (x, y) location that if available to position a sprite
def find_good_sprite_location(sprite_group: pygame.sprite.Group) -> (int, int):
    found: bool = False
    while not found:
        loc = (randint(50, WindowWidth - 40), randint(50, BackgroundHeight - 30))
        if distance_between_points(loc[0], loc[1], WindowWidth // 2, WindowHeight // 2) < 100:
            continue

        found = True
        for sprite in sprite_group:
            sprite_loc = sprite.rect.center
            if distance_between_points(loc[0], loc[1], sprite_loc[0], sprite_loc[1]) < 100:
                found = False
                break
        if found:
            return loc
       

def distance_between_points(x1, y1, x2, y2) -> float:
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def start(window, highscores, arial) -> str:
    font = pygame.font.Font('resources/CourierNew.ttf', 20)
    namefont = pygame.font.Font('resources/arial.ttf', 24)
    with open('resources/intro.txt', 'r') as f:
        direct_str = f.read()
    
    title_text = arial.render("Hungry Worm", True,"yellow")
    direct_text = font.render(direct_str, True,"cyan")
    hs_text = font.render(str(highscores), True,"chartreuse2")

    title_rect = title_text.get_rect()
    direct_text_rect = direct_text.get_rect()
    hs_rect = hs_text.get_rect()

    title_rect.center = (WindowWidth // 2, int(.06 * WindowHeight))
    direct_text_rect.center = (WindowWidth // 2, int(.25 * WindowHeight))
    hs_rect.center = (WindowWidth // 2, int(.7 * WindowHeight))

    prompt = "Please type your name and press Enter ===>"
    prompt_text = font.render(prompt, True,"cyan")
    prompt_rect = prompt_text.get_rect()
    prompt_rect.midleft = (WindowWidth // 8, int(.427 * WindowHeight))

    input_rect = pygame.Rect(int(.625 * WindowWidth), int(.405 * WindowHeight), 140, 32)

    running = True
    name = '_'

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return ""
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-2] + '_'

                elif event.key == pygame.K_RETURN:
                    running = False
                    break

                # Unicode standard is used for string
                else:
                    name = name[:-1].title()
                    name += event.unicode + '_'
        
        window.fill("black")
        text_surface = namefont.render(name, True, "gold")
        window.blit(prompt_text, prompt_rect)
        window.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    
        # set width of textfield so that text cannot get outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)

        window.blit(title_text, title_rect)
        window.blit(direct_text, direct_text_rect)
        window.blit(hs_text, hs_rect)
        window.blit(prompt_text, prompt_rect)
        pygame.display.flip()
    
    return name[:-1]

def game_over(window, score: int) -> None:
    font = pygame.font.Font('resources/arial.ttf', 64)
    font2 = pygame.font.Font('resources/arial.ttf', 48)
    text = font.render('Game Over', True,(190, 20, 50))
    text2 = font2.render('Score = ' + str(score), True,"white")
    textRect = text.get_rect()
    textRect.center = (WindowWidth // 2, int(.45 * WindowHeight))

    textRect2 = text2.get_rect()
    textRect2.center = (WindowWidth // 2, int(.55 * WindowHeight))

    pygame.draw.rect(window, (250, 240, 0), pygame.Rect(310, 275, 400, 200), 10)
    window.blit(text, textRect)
    window.blit(text2, textRect2)
    pygame.display.update()
    time.sleep(7)

def play_again(window) -> bool:
    running: bool = True
    font = pygame.font.Font('resources/arial.ttf', 64)
    font2 = pygame.font.Font('resources/arial.ttf', 48)
    text = font.render('Play Again\n     Y / N ', True,("blue"))
   
    textRect = text.get_rect()
    textRect.center = (WindowWidth // 2, int(.50 * WindowHeight))


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    running = False
                    return False
                elif event.key == pygame.K_y:
                    running = False
                    return True
        pygame.draw.rect(window, "green", pygame.Rect(310, 275, 400, 200))
        window.blit(text, textRect)
        pygame.display.update()
