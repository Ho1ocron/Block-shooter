# All imports will be there
import UserAndMapData
import CarRender
import pygame
import time
import os
import sys
import NoCollideBlocks
db = UserAndMapData.User()
session_data = db.get_session()[-1]  # (gm, car, level, bg)
if session_data[0] == 'creative':
    import CarPowerCreativeMode as CarPower
    import CreativePer
    import PreRenderBlocks
else:
    import CarPowerPlayMode as CarPower


def load_image(name):  # Load all img
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' not found.")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def change_bg():
    screen.fill((0, 0, 0))
    screen.blit(background, coordinates_changed)
    screen.blit(background, (coordinates_changed[0] % (screen_width + 1), coordinates_changed[1] % (screen_height + 1)))
    screen.blit(background, (coordinates_changed[0] % (screen_width + 1) - screen_width,
                             coordinates_changed[1] % (screen_height + 1) - screen_height))
    screen.blit(background, (coordinates_changed[0] % (screen_width + 1) - screen_width, coordinates_changed[1] %
                             (screen_height + 1)))
    screen.blit(background, (coordinates_changed[0] % (screen_width + 1), coordinates_changed[1] % (screen_height + 1) -
                             screen_height))


# Init program
pygame.init()
pygame.display.set_caption('Cold Road')

# All constants will be there
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
time_start = time.time() - 0.0167
background = pygame.transform.scale(load_image('GameFiles/' + session_data[-1]), (screen_width, screen_height))
car0 = pygame.transform.scale(load_image('GameFiles/' + session_data[1]), (180, 100))
now_car = (car0, (screen_width // 2 - 90, screen_height // 2 - 50))
car_data = db.get_car(session_data[1])[0]  # (car, power, clutch, streamlining, max_sp, price, str)
bg_data = db.get_background(session_data[-1])[0]  # (name, clutch, price, str)
fps_in_game = pygame.font.Font(pygame.font.get_default_font(), 36)
all_sprites = pygame.sprite.Group()
now_block = '1'
main_run = True
power_width_high = False
power_width_low = False
power_height_high = False
power_height_low = False
esc_button = False
car_stop = False
place_block = False
delete_block = False
last_power_height = 0
last_power_width = 0
coordinates_changed = [0, 0]


# Main cycle start

NoCollideBlocks.load_map(db.load_map_data(session_data[2]))
while main_run:
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()
    # All events will be there
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close program
            map_save = NoCollideBlocks.save_map()
            db.save_map_data(session_data[2], map_save)
            main_run = False

        elif event.type == pygame.KEYDOWN:  # Checking control keys
            if event.key == pygame.K_w:
                power_height_low = True
            if event.key == pygame.K_s:
                power_height_high = True
            if event.key == pygame.K_a:
                power_width_low = True
            if event.key == pygame.K_d:
                power_width_high = True
            if event.key == pygame.K_ESCAPE:
                esc_button = not esc_button
            if event.key == pygame.K_SPACE:
                car_stop = True
            if session_data[0] == 'creative':
                if CreativePer.type_block(event) is not None:
                    now_block = CreativePer.type_block(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                place_block = True
            elif event.button == 3:
                delete_block = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                power_height_low = False
            if event.key == pygame.K_s:
                power_height_high = False
            if event.key == pygame.K_a:
                power_width_low = False
            if event.key == pygame.K_d:
                power_width_high = False
            if event.key == pygame.K_SPACE:
                car_stop = False

    # All time-dependent physic
    time_end = time.time()
    if session_data[0] == 'creative':
        last_power_width, last_power_height = CarPower.calculate_engine(power_width_high, power_width_low,
                                                                        power_height_high, power_height_low,
                                                                        esc_button, last_power_width, last_power_height)
    else:
        last_power_width, last_power_height = CarPower.calculate_engine(power_width_high, power_width_low,
                                                                        power_height_high, power_height_low, time_end,
                                                                        time_start, esc_button, last_power_width,
                                                                        last_power_height, car_data,
                                                                        bg_data, car_stop)  # Getting powers

    time_start = time.time()
    # End all operations with time

    # Work with sprites start
    # THIS is global state of changing coordinates!
    coordinates_changed = [coordinates_changed[0] - int(last_power_width), coordinates_changed[1] -
                           int(last_power_height)]
    # RENDER AT THE END!
    # Starting render there
    change_bg()
    now_car = CarRender.render_car(power_width_high, power_width_low, power_height_high, power_height_low, car0,
                                   (screen_width, screen_height), now_car)
    screen.blit(now_car[0], now_car[1])
    if session_data[0] == 'creative':
        PreRenderBlocks.draw(screen, now_block, (mouse_pos[0] - (mouse_pos[0] + int(last_power_width)) % 5,
                                                 mouse_pos[1] - (mouse_pos[1] + int(last_power_height)) % 5))
        if place_block:
            place_block = False
            NoCollideBlocks.create_sprite(mouse_pos, now_block)
        if delete_block:
            delete_block = False
            NoCollideBlocks.delete_sprites(mouse_pos)
    NoCollideBlocks.update_sprites((last_power_width, last_power_height))
    NoCollideBlocks.draw_sprites(screen)
    screen.blit(fps_in_game.render(f'FPS: {str(clock.get_fps())[:4]}', True, 'white'), dest=(10, 10))
    pygame.display.flip()
