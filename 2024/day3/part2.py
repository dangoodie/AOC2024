import re
def main():
    output = 0
    mul_patter = r"mul\(\d{1,3},\d{1,3}\)"
    nums_pattern = r"\d{1,3}"
    enable_pattern = r"do\(\)"
    disable_pattern = r"don't\(\)"

    with open('input.txt') as f:
        enabled = True

        for line in f:
            tokens = re.finditer(rf"{enable_pattern}|{disable_pattern}|{mul_patter}", line)
            for token in tokens:
                match = token.group()
                if match == "do()":
                    enabled = True
                if match == "don't()":
                    enabled = False
                if enabled and re.match(mul_patter, match):
                    nums = re.findall(nums_pattern, match)
                    output += int(nums[0]) * int(nums[1])

    return output

if __name__ == '__main__':
    print(main())