def main():
    output = 0
    with open('input.txt') as f:
        for line in f:
            l = [int(num) for num in line.split(" ")]
            if determine_safety(l):
                output += 1

    return output

def determine_safety(l):
    dir = "Unknown"
    for i in range(len(l) - 1):
        # Determine direction for the first time
        if dir == "Unknown":
            dir = determine_direction(l[i], l[i + 1])
            if dir == "Unknown":
                return False

        # If the direction changes, it's unsafe
        if dir != determine_direction(l[i], l[i + 1]):
            return False

        # If the difference between the two numbers is less than 1 or greater than 3, it's unsafe
        val = abs(l[i] - l[i + 1])
        if val < 1 or val > 3:
            return False

    return True

def determine_direction(num1, num2):
    if num1 < num2:
        return "Increasing"
    elif num1 > num2:
        return "Decreasing"
    else:
        return "Unknown"


if __name__ == '__main__':
    print(main())