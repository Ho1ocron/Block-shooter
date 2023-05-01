def calculate_engine(power_width_high, power_width_low, power_height_high, power_height_low, time_end, time_start,
                     esc_button, last_power_width, last_power_height, car_data, bg_data):
    if esc_button:
        return last_power_width, last_power_height
    power_width = int(power_width_high) - int(power_width_low)
    power_height = int(power_height_high) - int(power_height_low)
    power_width = power_width * car_data[1] * car_data[2] * bg_data[1] * 0.125
    last_power_width += power_width
    power_height = power_height * car_data[1] * car_data[2] * bg_data[1] * 0.125
    last_power_height += power_height
    last_power_width *= 0.990 + 0.001 * car_data[3] * 2
    last_power_height *= 0.990 + 0.001 * car_data[3] * 2
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
    return last_power_width, last_power_height
