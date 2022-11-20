def print_in_color(value, color):
    colors = {
        "purple": '\033[95m',
        "blue": '\033[94m',
        "cyan": '\033[96m',
        "green": '\033[92m',
        "yellow": '\033[93m',
        "red": '\033[91m',
        "end_color": '\033[0m',
    }

    print(colors[color] + str(value) + colors["end_color"])



