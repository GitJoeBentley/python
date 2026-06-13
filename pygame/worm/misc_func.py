import pygame, time
from settings import *

def display_status(window, font, applesEaten: int, wallCollisions: int, rockCollisions: int, score: int):
    status_str = "Apples Eaten " + str(applesEaten).ljust(6) + "Wall Collisions " + str(wallCollisions).ljust(6) + \
        "Rock Collisions " + str(rockCollisions).ljust(7) + "Score " + str(score).ljust(4)
    text = font.render(status_str, True,(50, 200, 50))
    # create a rectangular object for the text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (WindowWidth // 2, int(.97 * WindowHeight))
    window.blit(text, textRect)

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
    hsfont = pygame.font.Font('resources/CourierNew.ttf', 16)
    namefont = pygame.font.Font('resources/arial.ttf', 24)

    with open('resources/intro.txt', 'r') as f:
        lines = f.read().split('\n')
    hs_lines = str(highscores).split('\n')

    title_text = arial.render("Hungry Worm", True,"yellow")
    title_rect = title_text.get_rect()
    title_rect.center = (WindowWidth // 2, int(.06 * WindowHeight))

    prompt = "Please type your name and press Enter ===>"
    prompt_text = font.render(prompt, True,"cyan")
    prompt_rect = prompt_text.get_rect()
    prompt_rect.midleft = (WindowWidth // 8, int(.49 * WindowHeight))

    input_rect = pygame.Rect(int(.625 * WindowWidth), int(.47 * WindowHeight), 140, 32)

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
        # print directions
        y = int(.15 * WindowHeight)
        for line in lines:
            # Render the individual single line
            line_surface = font.render(line, True, "white")
            # Blit line to the target surface
            window.blit(line_surface, (WindowWidth // 14, y))
            # Move the y-coordinate down by the height of the line
            y += line_surface.get_height() + 3  # 3 pixels of padding

        # print high scores
        y = int(.60 * WindowHeight)
        for line in hs_lines:
            # Render the individual single line
            line_surface = hsfont.render(line, True, "green")
            # Blit line to the target surface
            window.blit(line_surface, (WindowWidth // 4, y))
            # Move the y-coordinate down by the height of the line
            y += line_surface.get_height() + 3  # 3 pixels of padding

        window.blit(prompt_text, prompt_rect)
        pygame.display.flip()
    
    return name[:-1]

def game_over(window, score: int) -> None:
    font = pygame.font.Font('resources/arial.ttf', 48)
    font2 = pygame.font.Font('resources/arial.ttf', 36)
    text = font.render('Game Over', True,(190, 20, 50))
    text2 = font2.render('Score = ' + str(score), True,"blue")
    textRect = text.get_rect()
    textRect.center = (WindowWidth // 2, int(.45 * WindowHeight))

    textRect2 = text2.get_rect()
    textRect2.center = (WindowWidth // 2, int(.55 * WindowHeight))

    pygame.draw.rect(window, "green", pygame.Rect(335, 280, 370, 200))
    window.blit(text, textRect)
    window.blit(text2, textRect2)
    pygame.display.update()
    time.sleep(5)

def play_again(window) -> bool:
    running: bool = True
    font = pygame.font.Font('resources/arial.ttf', 32)
    text = font.render('Play Again\n      (y/n)', True,("blue"))
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
        pygame.draw.rect(window, "green", pygame.Rect(335, 280, 370, 200))
        window.blit(text, textRect)
        pygame.display.update()
