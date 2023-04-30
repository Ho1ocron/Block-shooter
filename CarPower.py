import UserAndMapData


def calculate_engine(power_width_high, power_width_low, power_height_high, power_height_low, time_end, time_start,
                     esc_button, last_power_width, last_power_height):
    if esc_button:
        return last_power_width, last_power_height
    db = UserAndMapData.User()
    data = db.get_session()  # (gm, car, level, bg)
    car_data = db.get_car(data[-1][1])  # (car, power, clutch, streamlining, max_sp, price, str)
    bg_data = db.get_background(data[-1][-1])  # (name, clutch, price, str)
    power_width = int(power_width_high) - int(power_width_low)
    power_height = int(power_height_high) - int(power_height_low)
    power_width = power_width * car_data[1] * car_data[2] * bg_data[1] * 0.125 * \
        ((1 / 60) * (1 / (time_end - time_start)))
    last_power_width += power_width
    power_height = power_height * car_data[1] * car_data[2] * bg_data[1] * 0.125 * \
        ((1 / 60) * (1 / (time_end - time_start)))
    last_power_height += power_height
    last_power_width *= 0.99 * car_data[3]
    last_power_height *= 0.99 * car_data[3]
    width = min(last_power_width, car_data[4])
    height = min(last_power_height, car_data[4])
    return width, height
