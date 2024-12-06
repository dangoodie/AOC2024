import time
import os

GUARD_CHARS = ["^", ">", "v", "<"]
DIRS = {"UP": (0, -1), "RIGHT": (1, 0), "DOWN": (0, 1), "LEFT":(-1, 0)}

def is_in_bounds(x, y, width, height):
    """Check if the coordinates are within bounds of the matrix."""
    return 0 <= x < width and 0 <= y < height

def get_direction(guard_char):
    if guard_char == "^":
        return DIRS["UP"]
    if guard_char == ">":
        return DIRS["RIGHT"]
    if guard_char == "v":
        return DIRS["DOWN"]
    if guard_char == "<":
        return DIRS["LEFT"]

def turn_right(guard_char):
    idx = GUARD_CHARS.index(guard_char)
    idx += 1
    if idx == len(GUARD_CHARS):
        idx = 0
    return GUARD_CHARS[idx]


def load_file(filename):
    map = []
    with open(filename) as f:
        for line in f:
            map.append(list(line.strip()))

    return map

def get_guard_pos(map):
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if map[y][x] in GUARD_CHARS:
                return x, y, map[y][x]

    return 0, 0

def move_guard(x, y, direction, map):
    temp_x = x + direction[0]
    temp_y = y + direction[1]
    if map[temp_y][temp_x] != "#":
        map[temp_y][temp_x] = map[y][x]
        map[y][x] = "X"
        return temp_x, temp_y, map
    else:
        map[y][x] = turn_right(map[y][x])
        return x, y, map

def count_chars(map):
    count = 0
    for row in map:
        for char in row:
            if char == "X" or char in GUARD_CHARS:
                count += 1
    return count

def print_map(map):
    #os.system("cls" if os.name == "nt" else "clear")
    for line in map:
        print("".join(line))
    print()
    #time.sleep(0.2)

def part_1(map):
    x, y, guard_char = get_guard_pos(map)
    direction = get_direction(guard_char)

    visited_positions = set()
    visited_positions.add((x, y))
    while is_in_bounds(x, y, len(map[0]), len(map)):
        # little animation for fun
        # print_map(map)
        try:
            x, y, map = move_guard(x, y, direction, map)
            guard_char = map[y][x]
            direction = get_direction(guard_char)
            visited_positions.add((x,y))
        except Exception as e:
            print(e)
            print("found end")
            break

    # print_map(map)
    return len(visited_positions)

# def part_2(rules, updates):
#     return sum(
#         reorder_nums(rules, update)[len(update) // 2]
#         for update in updates if not check_rules(rules, update)
#     )

if __name__ == '__main__':
    start_time = time.time()
    map = load_file("input.txt")
    load_time = time.time()
    print("<====== PART 1 ======>")
    print(part_1(map))
    part_1_time = time.time()
    print("<====== PART 2 ======>")
    # print(part_2(rules, updates))
    part_2_time = time.time()

    print(f"Completed in {(part_2_time - start_time) * 1000:.3f} ms")
    print(f"Loaded in {(load_time - start_time) * 1000:.3f} ms")
    print(f"Computed part 1 in {(part_1_time - load_time) * 1000:.3f} ms")
    print(f"Computed part 2 in {(part_2_time - part_1_time) * 1000:.3f} ms")