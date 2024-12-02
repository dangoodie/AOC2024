digit_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def main():
    output = 0
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            digits = [char for char in translate(line) if char.isnumeric()]
            output += int(digits[0] + digits[-1])
    return output

def translate(line):
    for num, name in enumerate(digit_names):
        line = line.replace(name, f"{name}{num}{name}")
    return line

if __name__ == '__main__':
    print(main())