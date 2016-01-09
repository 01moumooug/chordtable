def get_color(chordtable, pitch_class):
    r = chordtable.weights[pitch_class] / chordtable.max_weight

    red   = 255
    green = min(-1 * r * 255 * 2 + 255 * 2, 255)
    blue  = max(-1 * r * 255 * 2 + 255, 0)

    return map(int, (red, green, blue))

def format_color(red, green, blue):
    return '#{:02x}{:02x}{:02x}'.format(red, green, blue)