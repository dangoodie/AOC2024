import re

def find_power_set(games):
    min_colors = {"red": 0, "green": 0, "blue": 0}
    for game in games:
        for string in game.split(","):
            count = int(re.search(r"\d+", string).group())
            color = re.search(r"[a-z]+", string).group()
            min_colors[color] = max(count, min_colors.get(color))

    return min_colors.get("red") * min_colors.get("green") * min_colors.get("blue")

def main():
    total_output = 0
    with open('input.txt') as f:
        for line in f:
            games = line.split(":")[1].split("; ")
            total_output += find_power_set(games)

    return total_output

if __name__ == '__main__':
    print(main())
