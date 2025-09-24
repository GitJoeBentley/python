import pygame, time
from random import randint
from star import Star
from comet import Comet
from moon import Moon
from meteor import Meteor
from direction import Direction
from settings import *

if __name__ == '__main__':
    clock = pygame.time.Clock()
    FPS = 30     # frames per second
    running = True
    # general setup
    pygame.init()
    green = (0, 255, 0)
    blue = (0, 0, 128)

    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Wandering Star")
    background_surf = pygame.image.load("resources/darksky.png").convert_alpha()

    font = pygame.font.Font('resources/OpenSans-Light.ttf', 32)

    # create a text surface object,
    text = font.render('Wandering Star', True, green)

    # create a rectangular object for the text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (140, 40)

    # wandering star and cosmic dust
    star_group: pygame.sprite.Group = pygame.sprite.Group()
    cosmic_dust_group: pygame.sprite.Group = pygame.sprite.Group()

    star_colors = ('blue','green','orange','red','white','yellow')
    star_images = {}
    for color in star_colors:
        image_file = "resources/" + color + "_star.png"
        star_images[color] = pygame.image.load(image_file).convert_alpha()
    wandering_star = Star(pygame.transform.scale(star_images['white'],(18,18)), WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    star_group.add(wandering_star)
    cosmic_dust = []
    for i in range(0, 100):
        dust_size = randint(3,6)
        min_dust_height = int(.72 * WINDOW_HEIGHT)
        dust_image = star_images[star_colors[randint(0,len(star_colors)-1)]]
        dust_pos_x, dust_pos_y = randint(1, WINDOW_WIDTH), randint(1, min_dust_height)
        if dust_pos_x < WINDOW_WIDTH / 4 and dust_pos_y > int(.65 * WINDOW_HEIGHT):
            dust_pos_y -= int(.15 * WINDOW_HEIGHT)
        dust = Star(pygame.transform.scale(dust_image,(dust_size, dust_size)), dust_pos_x, dust_pos_y)
        #cosmic_dust.append(dust)
        star_group.add(dust)
        cosmic_dust_group.add(dust)

    comet = Comet(780, 250)
    star_group.add(comet)
    moon = Moon(300, 200)
    star_group.add(moon)

    # sounds
    eat_dust_sound = pygame.mixer.Sound("resources/eat_dust.wav")
    eat_dust_sound.set_volume(0.5)
    boing_sound = pygame.mixer.Sound("resources/boing.wav")
    boing_sound.set_volume(0.5)

    pygame.mixer.init()
    pygame.mixer.music.load("resources/testmusic.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1,0.0)

    loop_counter = 0
    meteor = Meteor()
   
    while running:
        dt = clock.tick(FPS) # dt will be milliseconds since last frame
        loop_counter += 1
        wandering_star.move()
        collision = pygame.sprite.spritecollide(wandering_star, cosmic_dust_group, True)
        if collision: 
            eat_dust_sound.play()

        if pygame.sprite.collide_rect(wandering_star, moon) or pygame.sprite.collide_rect(wandering_star, comet):
            boing_sound.play()
            wandering_star.change_direction()
        if loop_counter % 500 == 100:
            meteor.start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moon.move('right')
                if event.key == pygame.K_LEFT:
                    moon.move('left')
                if event.key == pygame.K_UP:
                    comet.move('up')
                if event.key == pygame.K_DOWN:
                    comet.move('down')
                if event.key == pygame.K_m:
                    meteor.start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Left mouse button pressed!")
                    wandering_star.move_to(pygame.mouse.get_pos())

        # draw the game
        display_surface.blit(background_surf)
        star_group.clear(display_surface, background_surf)
        star_group.update(display_surface)
        star_group.draw(display_surface)
        display_surface.blit(text, textRect)
        if meteor.started:
            meteor.move()
            display_surface.blit(meteor.image, meteor.rect)

        pygame.display.update()
        #time.sleep(0.1)


pygame.quit()


    