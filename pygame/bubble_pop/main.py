import pygame, time
from random import randint
from settings import *
from bubble import Bubble
from highscores import HighScores
from datetime import date

def random_direction() -> (float, float):
    return (randint(-45, 45) / 100, randint(-45, 45) / 100)

# location should maintain a distance from big_bubble_location
def random_location(big_bubble_location: (int, int)) -> (int, int):
    while True:
        location = (WINDOW_WIDTH // 2 + randint(-WINDOW_WIDTH // 3, WINDOW_WIDTH // 3), 
            int(WINDOW_HEIGHT / 2) + randint(-WINDOW_HEIGHT // 3, WINDOW_HEIGHT // 3))
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
    textRect.center = (WINDOW_WIDTH // 2, int(.973 * WINDOW_HEIGHT))
    window.blit(text, textRect)

def game_over(window, score: int) -> None:
    font = pygame.font.Font('resources/game_sans_serif_7.ttf', 48)
    font2 = pygame.font.Font('resources/game_sans_serif_7.ttf', 36)
    text = font.render('Game Over', True,(190, 20, 50))
    text2 = font2.render('Score = ' + str(score), True,(0, 130, 240))
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH // 2, int(.45 * WINDOW_HEIGHT))

    textRect2 = text2.get_rect()
    textRect2.center = (WINDOW_WIDTH // 2, int(.55 * WINDOW_HEIGHT))

    pygame.draw.rect(window, (250, 240, 0), pygame.Rect(310, 275, 400, 200), 10)
    window.blit(text, textRect)
    window.blit(text2, textRect2)
    pygame.display.update()
    time.sleep(7)

def start(window, highscores, arial) -> str:
    font = pygame.font.Font('resources/CourierNew.ttf', 20)
    direct_str = "The goal of this game is to avoid popping the big bubble.  The bubble pops\n" \
    "if it comes into contact with another bubble or hits the edge of the playing\n" \
    "area.  The points are determined by the number of bubbles that are created\n" \
    "during the game.\n"

    title_text = arial.render("Bubble Pop", True,"yellow")
    direct_text = font.render(direct_str, True,"cyan")
    hs_text = font.render(str(highscores), True,"chartreuse2")

    title_rect = title_text.get_rect()
    direct_text_rect = direct_text.get_rect()
    hs_rect = hs_text.get_rect()

    title_rect.center = (WINDOW_WIDTH // 2, int(.1 * WINDOW_HEIGHT))
    direct_text_rect.center = (WINDOW_WIDTH // 2, int(.2 * WINDOW_HEIGHT))
    hs_rect.center = (WINDOW_WIDTH // 2, int(.7 * WINDOW_HEIGHT))

    prompt = "Please type your name and press Enter ===>"
    prompt_text = font.render(prompt, True,"cyan")
    prompt_rect = prompt_text.get_rect()
    prompt_rect.midleft = (WINDOW_WIDTH // 8, int(.35 * WINDOW_HEIGHT))

    input_rect = pygame.Rect(int(.625 * WINDOW_WIDTH), int(.33 * WINDOW_HEIGHT), 140, 32)

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
        window.blit(direct_text, direct_text_rect)
        window.blit(hs_text, hs_rect)
        window.blit(prompt_text, prompt_rect)
        pygame.display.flip()
    
    return name[:-1]


if __name__ == '__main__':
    FPS = 30     # frames per second
    running = True
    # general setup
    pygame.init()
    clock = pygame.time.Clock()
    highscores = HighScores()
    #print(highscores)

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("Bubble Pop")
    
    bubbles = []

    font = pygame.font.Font('resources/arial_narrow_7.ttf', 30)

    # sounds
    bubble_sound = pygame.mixer.Sound("resources/WormPop.wav")
    bubble_sound.set_volume(0.5)
    big_bubble_sound = pygame.mixer.Sound("resources/mypop.wav")
    big_bubble_sound.set_volume(0.5)
    endofgame_sound = pygame.mixer.Sound("resources/EndOfGame.wav")

    pygame.mixer.init()
    pygame.mixer.music.load("resources/Lawrence_welk_bubbles_in_the_wine.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1,0.0)

    bubble_group: pygame.sprite.Group = pygame.sprite.Group()

    bubble_image = pygame.image.load("resources/bubble.png").convert_alpha()
    bubble = Bubble(bubble_image, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), random_direction(), 1.0, 3)
    bubble_group.add(bubble)

    loop_counter: int = 0

    pause: bool = False
    quit: bool = False

    name = start(window, highscores, font)
    if name == "":
        quit = True;
        running = False
   
    while running:
        loop_counter += 1
        if loop_counter % 25 == 0:
            new_bubble = Bubble(bubble_image, random_location(bubble.rect.center), random_direction(), random_size(), randint(3,4), True)
            bubbles.append(new_bubble)
            bubble_group.add(new_bubble)
        dt = clock.tick(FPS) # dt will be milliseconds since last frame
        if not pause:
            bubble.move()
            # check for out of bounds
            if bubble.out_of_bounds():
                running = False
                print("game over: score =", len(bubbles))
            # check for collision with another bubble
            for bub in bubbles:
                if pygame.sprite.collide_circle(bubble,bub):
                    running = False
                    #pause = True
                    print("Collision: score =", len(bubbles))

            for bub in bubbles:
                bub.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    bubble.direction = (1.0, 0.0)
                if event.key == pygame.K_LEFT:
                    bubble.direction = (-1.0, 0.0)
                if event.key == pygame.K_UP:
                    bubble.direction = (0.0, -1.0)
                if event.key == pygame.K_DOWN:
                    bubble.direction = (0.0, 1.0)

        # draw the game
        window.fill((0,0,0))
        bubble_group.update(window)
        bubble_group.draw(window)
        pygame.draw.line(window, (60, 10, 130), (0, playing_area_bottom), (WINDOW_WIDTH, playing_area_bottom), WINDOW_HEIGHT // 15)

        display_score(window, font, len(bubbles))

        pygame.display.update()
    if not quit:
        endofgame_sound.play()
        game_over(window, len(bubbles))
        highscores.scores.append((name,len(bubbles),date.today()))
        highscores.write_to_file()

pygame.quit()
