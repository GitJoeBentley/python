import pygame, time
from random import randint
from settings import *
from rock import Rock
from apple import Apple
from worm import Worm
from highscores import HighScores
from datetime import date


def display_status(font, applesEaten: int, wallCollisions: int, rockCollisions: int, score: int):
    status_str = "Apples Eaten " + str(applesEaten).ljust(6) + "Wall Collisions " + str(wallCollisions).ljust(6) + \
        "Rock Collisions " + str(rockCollisions).ljust(7) + "Score " + str(score).ljust(4)
    text = font.render(status_str, True,(50, 200, 50))
    # create a rectangular object for the text surface object
    textRect = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (WindowWidth // 2, int(.97 * WindowHeight))
    window.blit(text, textRect)


if __name__ == '__main__':
    clock = pygame.time.Clock()
    FPS = 30     # frames per second
    frame_sleep_time = 0.15
    running = True
    # general setup
    pygame.init()

    #local variables
    gameOverFlag: bool = False
    pause: bool = False
    playAgain: bool = True
    
    window = pygame.display.set_mode((WindowWidth, WindowHeight))
    pygame.display.set_caption("Joe's Hungry Worm")
    background = pygame.image.load("resources/grass.png").convert_alpha()
    statusBar = pygame.Surface((WindowWidth, 56))
    statusBarRect = statusBar.get_frect()
    statusBarRect.bottomleft = (0, WindowHeight)
    statusBar.fill("black")

    arial = pygame.font.Font('resources/arial.ttf', 32)

    # sounds
    doh_sound = pygame.mixer.Sound("resources/homer_doh.wav")
    doh_sound.set_volume(0.5)
    ouch_sound = pygame.mixer.Sound("resources/ouch.wav")
    ouch_sound.set_volume(0.5)
    bite_sound = pygame.mixer.Sound("resources/apple_bite.wav")
    bite_sound.set_volume(0.5)
    endofgame_sound = pygame.mixer.Sound("resources/endofgame.wav")
    endofgame_sound.set_volume(0.5)

    sprite_group = pygame.sprite.Group()
    worm_group = pygame.sprite.Group()
    rock_group = pygame.sprite.Group()

    # create apple
    apple_image = pygame.image.load("resources/apple.png").convert_alpha()
    apple_image.set_colorkey((34,177,76))
    
    highscores = HighScores()

    name = start(window, highscores, arial)
    while playAgain:
        #loopCounter: int = 0
        applesEaten: int = 0
        wallCollisions: int = 0
        rockCollisions: int = 0
        score: int = 0
        # create rocks
        rock_images = [pygame.image.load(file).convert_alpha() for file in rock_files]
        for i in range(21):
            rock = Rock(rock_images[i % 3], sprite_group, rock_group)
        # create worm
        worm = Worm(worm_group)
        # create apple
        apple = Apple(apple_image, sprite_group)
        
        while running:
            dt = clock.tick(FPS) # dt will be milliseconds since last frame
            #loopCounter += 1
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause = not pause

                    if not pause and event.key == pygame.K_UP:
                        worm.direction = "Up"
                    if not pause and event.key == pygame.K_DOWN:
                        worm.direction = "Down"
                    if not pause and event.key == pygame.K_LEFT:
                        worm.direction = "Left"
                    if not pause and event.key == pygame.K_RIGHT:
                        worm.direction = "Right"
            if not pause:
                match worm.move(rock_group, apple):
                    case "apple":
                        bite_sound.play()
                        apple = Apple(apple_image, sprite_group)
                        worm.add_segment(sprite_group)
                        applesEaten += 1
                        if applesEaten % 3 == 0:
                            Rock(rock_images[i % 3], sprite_group, rock_group)
                        frame_sleep_time *= 0.94
                    case "rock":
                        ouch_sound.play()
                        rockCollisions += 1
                    case "edge":
                        doh_sound.play()
                        wallCollisions += 1
                    case _:
                        pass

                score = 10 * applesEaten - wallCollisions - rockCollisions                

            # draw the game
            window.blit(background)
            window.blit(statusBar, statusBarRect)
            sprite_group.clear(window, background)
            sprite_group.update(window)
            sprite_group.draw(window)
            worm_group.update(window)
            worm_group.draw(window)
            display_status(arial , applesEaten, wallCollisions, rockCollisions, score)

            pygame.display.update()
            time.sleep(frame_sleep_time)
            if wallCollisions + rockCollisions == 10:
                running = False
        endofgame_sound.play()
        game_over(window, score)
        if score > 0:
            highscores.scores.append((name,score,applesEaten,date.today()))
        highscores.write_to_file()
        playAgain = play_again(window)
        if playAgain:
            rock_group.empty()
            worm_group.empty()
            sprite_group.empty()
            running = True
    pygame.quit()
