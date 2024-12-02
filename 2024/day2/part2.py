def main():
    output = 0
    with open('input.txt') as f:
        for line in f:
            l = [int(num) for num in line.split(" ")]
            if loop_level(l) or try_dampener(l):
                output += 1

    return output

def loop_level(l):
    dir = None
    dir = determine_direction(l[0], l[1])
    if dir is None:
        return False

    for i in range(len(l) - 1):
        if dir != determine_direction(l[i], l[i + 1]):
            return False
        if not determine_safety(l[i], l[i + 1]):
            return False

    return True

def try_dampener(l):
    for i in range(len(l)):
        temp_l = l[:i] + l[i + 1:]
        if loop_level(temp_l):
            return True
    return False


def determine_direction(num1, num2):
    if num1 < num2:
        return 1
    elif num1 > num2:
        return 0
    else:
        return None

def determine_safety(num1, num2):
    val = abs(num1 - num2)
    if val < 1 or val > 3:
        return False
    else:
        return True

if __name__ == '__main__':
    print(main())