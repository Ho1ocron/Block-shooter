# All imports will be there
import UserAndMapData
import pygame
import CarPower
import time
import os
import sys
db = UserAndMapData.User()
session_data = db.get_session()[-1]  # (gm, car, level, bg)


def load_image(name):  # Load all img
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' not found.")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def change_bg():
    screen.fill((0, 0, 0))
    screen.blit(background, coordinats_changed)
    screen.blit(background, (coordinats_changed[0] % (screen_width + 1), coordinats_changed[1] % (screen_height + 1)))
    screen.blit(background, (coordinats_changed[0] % (screen_width + 1) - screen_width,
                             coordinats_changed[1] % (screen_height + 1) - screen_height))
    screen.blit(background, (coordinats_changed[0] % (screen_width + 1) - screen_width, coordinats_changed[1] %
                             (screen_height + 1)))
    screen.blit(background, (coordinats_changed[0] % (screen_width + 1), coordinats_changed[1] % (screen_height + 1) -
                             screen_height))

# Init program
pygame.init()
pygame.display.set_caption('Cold Road')

# All constants will be there
main_run = True
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
time_start = time.time()
background = pygame.transform.scale(load_image(session_data[-1]), (screen_width, screen_height))
car0 = pygame.transform.scale(load_image(session_data[1]), (screen_width // 19.2, screen_height // 10.8))
car_data = db.get_car(session_data[1])[0]  # (car, power, clutch, streamlining, max_sp, price, str)
bg_data = db.get_background(session_data[-1])[0]  # (name, clutch, price, str)
power_width_high = False
power_width_low = False
power_height_high = False
power_height_low = False
esc_button = False
last_power_height = 2
last_power_width = 2
coordinats_changed = [0, 0]


# Main cycle start
while main_run:
    clock.tick(60)
    # All events will be there
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close program
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

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                power_height_low = False
            if event.key == pygame.K_s:
                power_height_high = False
            if event.key == pygame.K_a:
                power_width_low = False
            if event.key == pygame.K_d:
                power_width_high = False

    time_end = time.time()
    print(1 / (time_end - time_start))
    time_start = time.time()
    last_power_width, last_power_height = CarPower.calculate_engine(power_width_high, power_width_low,
                                                                    power_height_high, power_height_low, time_end,
                                                                    time_start, esc_button, last_power_width,
                                                                    last_power_height, car_data,
                                                                    bg_data)  # Getting powers
    coordinats_changed = [coordinats_changed[0] + last_power_width, coordinats_changed[1] + last_power_height]
    change_bg()

    pygame.display.flip()
