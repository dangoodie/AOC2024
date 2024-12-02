list_a = []
list_b = []

def main():
    with open('input.txt') as f:
        for line in f:
            line = line.split("   ")

            list_a.append(int(line[0]))
            list_b.append(int(line[1]))

    list_a.sort()
    list_b.sort()

    output = sum(abs(list_a[i] - list_b[i]) for i in range(len(list_a)))

    return output

if __name__ == '__main__':
    print(main())