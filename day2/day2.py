f = open("input", "r")

mooves_A = ['A', 'B', 'C']
mooves_B = ['X', 'Y', 'Z']
desc = ["Rock", "Paper", "Scissors"]
result = ["LOSS", "DRAW", "WIN"]

def calc_result(moove_a, moove_b):
    index_a = mooves_A.index(moove_a)
    index_b = mooves_B.index(moove_b)
    if (index_a == index_b):
        print (desc[index_a] + " vs " + desc[index_b] + " DRAW")
        return (3 + index_b + 1) #draw
    elif((index_a < index_b and (abs(index_a - index_b) == 1))  or (index_a == 2 and index_b == 0)):
        print (desc[index_a] + " vs " + desc[index_b] + " WIN")
        return (6 + index_b + 1) #win
    else:
        print (desc[index_a] + " vs " + desc[index_b] + " LOSS")
        return (0 + index_b + 1) #loss


def choose_moove(moove_a, outcome):
    index_a = mooves_A.index(moove_a)
    index_b = -1
    if outcome == "Y": #draw
        print ("WE WANT DRAW")
        index_b = index_a
    elif outcome == "Z": #win
        print ("WE WANT WIN")
        index_b = index_a + 1
        if index_b == 3:
            index_b = 0
    else: #loose
        print ("WE WANT LOOSE")
        index_b = index_a - 1
        if index_b == -1:
            index_b = 2
    
    return calc_result(moove_a, mooves_B[index_b])

def part1():
    total = 0
    for line in f:
        moove_a, moove_b = line.split()
        total += (calc_result(moove_a, moove_b))
    print(total)

def part2():
    total = 0
    for line in f:
        moove_a, moove_b = line.split()
        total += (choose_moove(moove_a, moove_b))
    print(total)

part2()