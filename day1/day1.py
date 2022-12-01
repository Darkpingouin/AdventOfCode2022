f = open("input", "r")

def part1():
    current_caltotal = 0
    elves_totals = []
    for line in f:
        line = line.strip()
        if line == "":
            elves_totals.append(current_caltotal)
            current_caltotal = 0
        else:
            current_caltotal += int(line)
    elves_totals.append(current_caltotal)
    print(max(elves_totals))


def part2():
    current_caltotal = 0
    elves_totals = []
    for line in f:
        line = line.strip()
        if line == "":
            elves_totals.append(current_caltotal)
            current_caltotal = 0
        else:
            current_caltotal += int(line)
    elves_totals.append(current_caltotal)
    print(sum(sorted(elves_totals, reverse=True)[0:3]))

part2()