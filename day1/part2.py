from collections import Counter

list_a = []
list_b = []

def main():
    with open('input.txt') as f:
        for line in f:
            line = line.split("   ")

            list_a.append(int(line[0]))
            list_b.append(int(line[1]))


    b_counts = Counter(list_b)

    output = 0
    for num in list_a:
        if num in b_counts:
            output += b_counts[num] *  num

    return output

if __name__ == '__main__':
    print(main())