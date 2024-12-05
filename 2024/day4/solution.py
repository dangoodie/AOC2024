import time

PART_1_DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
PART_2_DIRECTIONS = [(1,1), (-1,-1), (1,-1), (-1,1)]

def is_in_bounds(x, y, width, height):
    """Check if the coordinates are within bounds of the matrix."""
    return 0 <= x < width and 0 <= y < height


def search_word(text, start_x, start_y, direction, word):
    """Search for a word in a specific direction."""
    max_width = len(text[0])
    max_height = len(text)
    temp_x, temp_y = start_x, start_y

    for char in word:
        if not is_in_bounds(temp_x, temp_y, max_width, max_height) or text[temp_y][temp_x] != char:
            return False
        temp_x += direction[0]
        temp_y += direction[1]

    return True

def search_word_center(text, start_x, start_y, direction, word):
    max_width = len(text[0])
    max_height = len(text)

    temp_x = start_x - (len(word)//2 * direction[0])
    temp_y = start_y - (len(word)//2 * direction[1])

    for char in word:
        if not is_in_bounds(temp_x, temp_y, max_width, max_height) or text[temp_y][temp_x] != char:
            return False
        temp_x += direction[0]
        temp_y += direction[1]

    return True


def load_file(filename):
    text = []

    # Read and process the input text file
    with open(filename) as f:
        for line in f:
            text.append(line.strip())

    max_height = len(text)
    max_width = len(text[0]) if max_height > 0 else 0

    print("Max Width: ", max_width)
    print("Max Height: ", max_height)
    return text, max_width, max_height

def part1(text, max_height, max_width):
    """Count all occurrences of the word 'XMAS' in the matrix."""
    output = 0

    # Traverse each character in the grid
    for y in range(max_height):
        for x in range(max_width):
            if text[y][x] == "X":
                # Check all directions for the word "XMAS"
                for direction in PART_1_DIRECTIONS:
                    if search_word(text, x, y, direction, "XMAS"):
                        output += 1

    return output


def part2(text, max_height, max_width):
    output = 0

    for y in range(max_height):
        for x in range(max_width):
            if text[y][x] == "A":
                # Check all directions for crossing MAS's
                found = 0
                for direction in PART_2_DIRECTIONS:
                    if search_word_center(text, x, y, direction, "MAS"):
                       found += 1
                if found == 2:
                    output += 1
                    continue

    return output

if __name__ == '__main__':
    start_time = time.time()
    text, max_height, max_width = load_file("input.txt")
    load_time = time.time()
    print("<====== PART 1 ======>")
    print(part1(text, max_height, max_width))
    part_1_time = time.time()
    print("<====== PART 2 ======>")
    print(part2(text, max_height, max_width))
    part_2_time = time.time()

    print(f"Completed in {part_2_time - start_time:.5f} seconds")
    print(f"Loaded in {load_time - start_time:.5f} seconds")
    print(f"Computed part 1 in {part_1_time - load_time:.5f} seconds")
    print(f"Computed part 2 in {part_2_time - part_1_time:.5f} seconds")
