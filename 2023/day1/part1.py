def main():
    output = 0
    with open('input.txt') as f:
        for line in f:
            digits = [char for char in line if char.isnumeric()]
            output += int(digits[0] + digits[-1])
    return output

if __name__ == '__main__':
    print(main())