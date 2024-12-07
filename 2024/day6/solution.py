from tqdm import tqdm

FREE = "."
OBJECT = "#"
GUARD_CHARS = {"^", ">", "v", "<"}
ROTATE = {"^": ">", ">": "v", "v": "<", "<": "^"}
DIRECTION_DELTAS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def read_input(input_file):
    """Read the input map and extract the guard's starting position and direction."""
    with open(input_file) as f:
        lab = [list(line.strip()) for line in f]

    starting_position = None
    starting_direction = None

    for r, row in enumerate(lab):
        for c, char in enumerate(row):
            if char in GUARD_CHARS:
                starting_direction = char
                starting_position = (r, c)
                lab[r][c] = FREE  # Replace guard position with FREE space
                break
        if starting_position is not None:
            break

    return lab, DIRECTION_DELTAS[starting_direction], starting_position


def is_free(pos, lab):
    """Check if the position is free (contains a dot)."""
    return lab[pos[0]][pos[1]] == FREE


def is_object(pos, lab):
    """Check if the position contains an obstacle (hash)."""
    return lab[pos[0]][pos[1]] == OBJECT


def in_grid(pos, lab):
    """Check if the position is within the grid bounds."""
    rows, cols = len(lab), len(lab[0])
    return 0 <= pos[0] < rows and 0 <= pos[1] < cols


def next_neighbour2(pos, direction):
    """Get the next position based on the current direction."""
    delta_r, delta_c = direction
    return pos[0] + delta_r, pos[1] + delta_c


def part1(input):
    """Solve Part 1: Count distinct positions visited by the guard."""
    lab, starting_direction, starting_position = input

    guard_position = starting_position
    guard_direction = starting_direction
    visited = set([starting_position])

    # Convert delta to arrow for ROTATE lookup
    delta_to_arrow = {v: k for k, v in DIRECTION_DELTAS.items()}

    while True:
        next_position = next_neighbour2(guard_position, guard_direction)

        if not in_grid(next_position, lab):
            break
        elif is_free(next_position, lab):
            guard_position = next_position
            visited.add(guard_position)
        elif is_object(next_position, lab):
            # Convert delta to arrow, rotate, and back to delta
            guard_arrow = delta_to_arrow[guard_direction]
            guard_direction = DIRECTION_DELTAS[ROTATE[guard_arrow]]
        else:
            raise ValueError(f"Unexpected position state at {next_position}")

    return len(visited), visited


def part2(input, visited_part1):
    """Solve Part 2: Count valid obstruction positions."""
    result = 0
    lab, starting_direction, starting_position = input

    # Convert delta to arrow for ROTATE lookup
    delta_to_arrow = {v: k for k, v in DIRECTION_DELTAS.items()}

    with tqdm(total=len(visited_part1), desc="Calculating Part 2") as pbar:
        for new_object_pos in visited_part1:
            # Skip the guard's starting position or positions that already have objects
            if new_object_pos == starting_position or is_object(new_object_pos, lab):
                pbar.update(1)
                continue

            guard_position = starting_position
            guard_direction = starting_direction
            visited = set()

            while True:
                next_position = next_neighbour2(guard_position, guard_direction)

                if not in_grid(next_position, lab):
                    break
                elif is_object(next_position, lab) or next_position == new_object_pos:
                    cur_pos_dir = (guard_position, guard_direction)

                    if cur_pos_dir in visited:  # Loop detected
                        result += 1
                        break
                    else:
                        visited.add(cur_pos_dir)
                        # Convert delta to arrow, rotate, and back to delta
                        guard_arrow = delta_to_arrow[guard_direction]
                        guard_direction = DIRECTION_DELTAS[ROTATE[guard_arrow]]
                elif is_free(next_position, lab):
                    guard_position = next_position
                else:
                    raise ValueError(f"Unexpected position state at {next_position}")

            pbar.update(1)

    return result

def main():
    input_file = "input.txt"
    input = read_input(input_file)
    test_input = read_input("test.txt")

    # Part 1
    test_result, test_visited = part1(test_input)
    assert test_result == 41, f"Test Part 1 failed: Expected 41, got {test_result}"
    result, visited = part1(input)
    print(f"Part 1: Distinct positions visited = {result}")

    # Part 2
    test_part2_result = part2(test_input, test_visited)
    assert test_part2_result == 6, f"Test Part 2 failed: Expected 6, got {test_part2_result}"
    part2_result = part2(input, visited)
    print(f"Part 2: Valid obstruction positions = {part2_result}")


if __name__ == "__main__":
    main()
