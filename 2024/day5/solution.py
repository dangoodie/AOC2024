import time

def load_rules(string):
    return tuple(map(int, string.split("|")))

def load_updates(string):
    return [int(num) for num in string.strip().split(",")]



def load_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    rules = [load_rules(line) for line in lines if "|" in line]
    updates = [load_updates(line) for line in lines if "," in line]

    return rules, updates

def check_rule(rule, update):
    if rule[1] not in update:
        return True
    return update.index(rule[0]) < update.index(rule[1])



def check_rules(rules, update):
    return all(check_rule(rule, update) for rule in rules if rule[0] in update)



def part_1(rules, updates):
    return sum(update[len(update) // 2] for update in updates if check_rules(rules, update))


def reorder_nums(rules, update):
    update = update.copy()

    changed = True
    while changed:
        changed = False
        for before, after in rules:
            if before in update and after in update:
                idx_before = update.index(before)
                idx_after = update. index(after)
                if idx_before > idx_after:
                    update[idx_before], update[idx_after] = update[idx_after], update[idx_before]
                    changed = True

    return update

def part_2(rules, updates):
    return sum(
        reorder_nums(rules, update)[len(update) // 2]
        for update in updates if not check_rules(rules, update)
    )

if __name__ == '__main__':
    start_time = time.time()
    rules, updates = load_file("input.txt")
    load_time = time.time()
    print("<====== PART 1 ======>")
    print(part_1(rules, updates))
    part_1_time = time.time()
    print("<====== PART 2 ======>")
    print(part_2(rules, updates))
    part_2_time = time.time()

    print(f"Completed in {(part_2_time - start_time) * 1000:.3f} ms")
    print(f"Loaded in {(load_time - start_time) * 1000:.3f} ms")
    print(f"Computed part 1 in {(part_1_time - load_time) * 1000:.3f} ms")
    print(f"Computed part 2 in {(part_2_time - part_1_time) * 1000:.3f} ms")