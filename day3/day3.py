f = open("input", "r")


def calc_score(letter):
    score = ord(letter)
    if (score >= 97):
        score = score - 96
    else:
        score = score - 38
    return score


def calc_bag(line):
    middle = int(len(line) / 2)
    bag_a = line[0:middle] 
    bag_b = line[middle:]
    common_list = set(bag_a).intersection(bag_b)
    letter = ''
    for l in common_list:
        letter = l
    return (calc_score(letter))


def calc_bags(bagA, bagB, bagC):
    common_list_one = set(bagA).intersection(bagB)
    common_list = common_list_one.intersection(bagC)
    letter = ''
    for l in common_list:
        letter = l
    return (calc_score(letter))

def part1():
    total = 0
    for line in f:
        total += calc_bag(line.strip())
    print(total)

def part2():
    total = 0
    i = 1
    bagA = ""
    bagB = ""
    bagC = ""
    for line in f:
        if (i == 1): #BagA
            bagA = line.strip()
        elif(i == 2): #BagB
            bagB = line.strip()
        else: #BagC
            bagC = line.strip()
            i = 0
            total += calc_bags(bagA, bagB, bagC)
        i+=1
    print(total)
part2()
