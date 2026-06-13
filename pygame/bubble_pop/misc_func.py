import pygame, time
from random import randint
from settings import *


def random_direction() -> (float, float):
    return (randint(-45, 45) / 100, randint(-45, 45) / 100)

# location should maintain a distance from big_bubble_location
def random_location(big_bubble_location: (int, int)) -> (int, int):
    while True:
        location = (WindowWidth // 2 + randint(-WindowWidth // 3, WindowWidth // 3), 
            int(WindowHeight / 2) + randint(-WindowHeight // 3, WindowHeight // 3))
        if abs(location[0] - big_bubble_location[0]) > 100 and abs(location[1] - big_bubble_location[1]) > 100:
           break
    return location

def random_size() -> float:
    return 1 / randint(2,20)

def display_score(window, font: pygame.font.Font, score: int):
    # create a text surface object,
    text = font.render('Number of Bubbles ' + str(score), True,(50, 200, 50))
    # create a rectangular object for the text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (WindowWidth // 2, int(.973 * WindowHeight))
    window.blit(text, textRect)

def game_over(window, score: int) -> None:
    font = pygame.font.Font('resources/game_sans_serif_7.ttf', 48)
    font2 = pygame.font.Font('resources/game_sans_serif_7.ttf', 36)
    text = font.render('Game Over', True,(190, 20, 50))
    text2 = font2.render('Score = ' + str(score), True,(0, 130, 240))
    textRect = text.get_rect()
    textRect.center = (WindowWidth // 2, int(.45 * WindowHeight))

    textRect2 = text2.get_rect()
    textRect2.center = (WindowWidth // 2, int(.55 * WindowHeight))

    pygame.draw.rect(window, (250, 250, 140), pygame.Rect(310, 275, 400, 200))
    window.blit(text, textRect)
    window.blit(text2, textRect2)
    pygame.display.update()
    time.sleep(7)

def start(window, highscores, arial) -> str:
    font = pygame.font.Font('resources/CourierNew.ttf', 20)
    titlefont = pygame.font.Font('resources/FuzzyBubbles-Bold.ttf', 48)
    title_text = titlefont.render("Bubble Pop", True,"yellow")
    title_rect = title_text.get_rect()
    title_rect.center = (WindowWidth // 2, int(.06 * WindowHeight))

    directions = ["The goal of this game is to avoid popping the big bubble.  The bubble pops",
    "if it comes into contact with another bubble or hits the edge of the playing",
    "area.  The points are determined by the number of bubbles that are created",
    "during the game."]
    
    hs_lines = str(highscores).split('\n')

    prompt = "Please type your name and press Enter ===>"
    prompt_text = font.render(prompt, True,"cyan")
    prompt_rect = prompt_text.get_rect()
    prompt_rect.midleft = (WindowWidth // 8, int(.37 * WindowHeight))

    input_rect = pygame.Rect(int(.625 * WindowWidth), int(.35 * WindowHeight), 140, 32)

    running = True
    name = '_'

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return ""
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    name = user_text[:-2] + '_'

                elif event.key == pygame.K_RETURN:
                    running = False
                    break

                # Unicode standard is used for string
                else:
                    name = name[:-1].title()
                    name += event.unicode + '_'
        
        window.fill("black")
        text_surface = font.render(name, True, "cyan")
        window.blit(prompt_text, prompt_rect)
        window.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    
        # set width of textfield so that text cannot get outside of user's text input
        input_rect.w = max(100, text_surface.get_width()+10)

        window.blit(title_text, title_rect)
        
        # print directions
        y = int(.16 * WindowHeight)
        for line in directions:
            # Render the individual single line
            line_surface = font.render(line, True, "white")
            # Blit line to the target surface
            window.blit(line_surface, (WindowWidth // 17, y))
            # Move the y-coordinate down by the height of the line
            y += line_surface.get_height() + 3  # 3 pixels of padding
        
        # print high scores
        y = int(.50 * WindowHeight)
        for line in hs_lines:
            # Render the individual single line
            line_surface = font.render(line, True, "green")
            # Blit line to the target surface
            window.blit(line_surface, (WindowWidth // 4 + 28, y))
            # Move the y-coordinate down by the height of the line
            y += line_surface.get_height() + 3  # 3 pixels of padding

        window.blit(prompt_text, prompt_rect)
        pygame.display.flip()
    
    return name[:-1]