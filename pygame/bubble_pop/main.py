import pygame, time
from random import randint
from settings import *
from misc_func import *
from bubble import Bubble
from highscores import HighScores
from datetime import date

def main():
    FPS = 30     # frames per second
    running = True
    # general setup
    pygame.init()
    clock = pygame.time.Clock()
    highscores = HighScores()

    window = pygame.display.set_mode((WindowWidth, WindowHeight))

    pygame.display.set_caption("Bubble Pop")
    
    bubbles = []

    font = pygame.font.Font('resources/arial_narrow_7.ttf', 30)
    hsfont = pygame.font.Font('resources/CourierNew.ttf', 16)
    hs_lines = str(highscores).split('\n')

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
    bubble = Bubble(bubble_image, (WindowWidth // 2, WindowHeight // 2), random_direction(), 1.0, 2)
    bubble_group.add(bubble)

    loop_counter: int = 0

    pause: bool = False
    quit: bool = False

    name = start(window, highscores, font)
    if name == "":
        quit = True
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
        pygame.draw.line(window, (60, 10, 130), (0, playing_area_bottom), (WindowWidth, playing_area_bottom), WindowHeight // 15)

        display_score(window, font, len(bubbles))

        pygame.display.update()
    if not quit:
        endofgame_sound.play()
        game_over(window, len(bubbles))
        highscores.scores.append((name,len(bubbles),date.today()))
        highscores.write_to_file()

    pygame.quit()

if __name__ == '__main__':
    main()