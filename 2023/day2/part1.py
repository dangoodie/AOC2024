import re

MAX_COUNTS = {'red': 12, 'green': 13, 'blue': 14}


def parse_color_data(colors_str):
    for color_str in colors_str:
        count = int(re.search(r"\d+", color_str).group())
        color = re.search(r"[a-z]+", color_str).group()
        if count > MAX_COUNTS.get(color):
            return False
    return True


def main():
    total_output = 0
    with open('input.txt') as f:
        for line in f:
            game_idx, game_str = line.split(":")
            game_idx = int(re.search(r'\d+', game_idx).group())
            games = game_str.split("; ")

            if all(parse_color_data(game.split(",")) for game in games):
                total_output += game_idx

    return total_output


if __name__ == '__main__':
    print(main())
