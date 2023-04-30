# All imports will be there
import UserAndMapData
import pygame
import CarPower
import time
import os
import sys
db = UserAndMapData.User()
session_data = db.get_session()  # (gm, car, level, bg)
if session_data[0] == 'creative':
    import NoCollideBlocks
else:
    pass


def load_image(name):  # Load all img
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"File with image '{fullname}' not found.")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# Init program
pygame.init()
pygame.display.set_caption('Cold Road')

# All constants will be there
main_run = True
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
time_start = time.time_ns()
background = pygame.transform.scale(load_image(session_data[-1]), (screen_width, screen_height))
car0 = pygame.transform.scale(load_image(session_data[1]), (screen_width // 19.2, screen_height // 10.8))
power_width_high = False
power_width_low = False
power_height_high = False
power_height_low = False
esc_button = False
last_power_height = 0
last_power_width = 0


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

    time_end = time.time_ns()
    last_power_width, last_power_height = CarPower.calculate_engine(power_width_high, power_width_low,
                                                                    power_height_high, power_height_low, time_end,
                                                                    time_start, esc_button, last_power_width,
                                                                    last_power_height)  # Getting powers
    time_start = time.time_ns()
