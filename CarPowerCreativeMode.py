def calculate_engine(power_width_high, power_width_low, power_height_high, power_height_low,
                     esc_button, last_power_width, last_power_height, shift):
    if esc_button:
        return last_power_width, last_power_height
    power_width = int(power_width_high) - int(power_width_low)
    power_height = int(power_height_high) - int(power_height_low)
    last_power_width += 0.5 * power_width
    last_power_height += 0.5 * power_height
    last_power_width *= abs(power_width)
    last_power_height *= abs(power_height)
    if abs(last_power_width) > 20 * (shift + 1):
        if abs(last_power_width) * (shift + 1) == last_power_width * (shift + 1):
            last_power_width = 20 * (shift + 1)
        else:
            last_power_width = -20 * (shift + 1)
    if abs(last_power_height) > 20 * (shift + 1):
        if abs(last_power_height) * (shift + 1) == last_power_height * (shift + 1):
            last_power_height = 20 * (shift + 1)
        else:
            last_power_height = -20 * (shift + 1)
    return last_power_width, last_power_height
