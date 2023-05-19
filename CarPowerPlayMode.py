def calculate_engine(power_width_high, power_width_low, power_height_high, power_height_low, time_end, time_start,
                     esc_button, last_power_width, last_power_height, car_data, bg_data, car_stop):
    if esc_button:
        return last_power_width, last_power_height
    # (car, power, clutch, streamlining, max_sp, price, str)
    if not car_stop:
        power_width = int(power_width_high) - int(power_width_low)
        power_height = int(power_height_high) - int(power_height_low)
        power_width = power_width * car_data[1] * car_data[2] * bg_data[1] * 0.125
        last_power_width += power_width
        power_height = power_height * car_data[1] * car_data[2] * bg_data[1] * 0.125
        last_power_height += power_height
    last_power_width *= 0.999 - 0.001 * car_data[3]
    last_power_height *= 0.999 - 0.001 * car_data[3]
    print(last_power_height, last_power_width)
    if car_stop:
        last_power_width *= 0.999 - 0.0008 * car_data[3] * (bg_data[1] ** 2) * car_data[3]
        last_power_height *= 0.999 - 0.0008 * car_data[3] * (bg_data[1] ** 2) * car_data[3]
        return last_power_width, last_power_height
    if abs(last_power_width) > car_data[4]:
        if abs(last_power_width) == last_power_width:
            last_power_width = car_data[4]
        else:
            last_power_width = -car_data[4]
    if abs(last_power_height) > car_data[4]:
        if abs(last_power_height) == last_power_height:
            last_power_height = car_data[4]
        else:
            last_power_height = -car_data[4]
    if last_power_width ** 2 + last_power_height ** 2 > car_data[4] ** 2:
        need_to_remove = last_power_width ** 2 + last_power_height ** 2 - car_data[4] ** 2
        if last_power_width > 0:
            last_power_width -= (need_to_remove / 2) ** 0.5
        else:
            last_power_width += (need_to_remove / 2) ** 0.5
        if last_power_height > 0:
            last_power_height -= (need_to_remove / 2) ** 0.5
        else:
            last_power_height += (need_to_remove / 2) ** 0.5
    if abs(last_power_width) < 0.2 and not abs(power_width):
        last_power_width = 0
    if abs(last_power_height) < 0.2 and not abs(power_height):
        last_power_height = 0
    return last_power_width, last_power_height
