import pygame


def render_car(power_width_high, power_width_low, power_height_high, power_height_low, car, xy, last):
    chpx = int(power_width_high) - int(power_width_low)
    chpy = int(power_height_high) - int(power_height_low)
    if chpx > 0 and chpy > 0:
        car = pygame.transform.rotate(car, 315)
        coordinats = (xy[0] // 2 - 90, xy[1] // 2 - 100)
    elif chpx > 0 and chpy == 0:
        car = pygame.transform.rotate(car, 0)
        coordinats = (xy[0] // 2 - 90, xy[1] // 2 - 50)
    elif chpy < 0 < chpx:
        car = pygame.transform.rotate(car, 45)
        coordinats = (xy[0] // 2 - 90, xy[1] // 2 - 100)
    elif chpx == 0 and chpy < 0:
        car = pygame.transform.rotate(car, 90)
        coordinats = (xy[0] // 2 - 50, xy[1] // 2 - 90)
    elif chpx < 0 and chpy < 0:
        car = pygame.transform.rotate(car, 135)
        coordinats = (xy[0] // 2 - 90, xy[1] // 2 - 100)
    elif chpx < 0 and chpy == 0:
        car = pygame.transform.rotate(car, 180)
        coordinats = (xy[0] // 2 - 90, xy[1] // 2 - 50)
    elif chpx < 0 < chpy:
        car = pygame.transform.rotate(car, 225)
        coordinats = (xy[0] // 2 - 90, xy[1] // 2 - 100)
    elif chpx == 0 and chpy > 0:
        car = pygame.transform.rotate(car, 270)
        coordinats = (xy[0] // 2 - 50, xy[1] // 2 - 90)
    else:
        return last
    last = (car, coordinats)
    return last
