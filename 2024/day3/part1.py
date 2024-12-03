import re
def main():
    output = 0
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    with open('input.txt') as f:
        l = re.findall(pattern, f.read())
        for i in l:
            nums = re.findall(r"\d{1,3}", i)
            output += int(nums[0]) * int(nums[1])

    return output

if __name__ == '__main__':
    print(main())