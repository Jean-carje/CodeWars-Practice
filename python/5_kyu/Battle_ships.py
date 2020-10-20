# Kata link:
# https://www.codewars.com/kata/58d06bfbc43d20767e000074

# -------------------------------------
# Solution 1:
import math
def damaged_or_sunk(board, attacks):
    result = {
        'sunk': 0,
        'damaged': 0,
        'not_touched': 0,
        'points': 0
    }
    # how many boats there are and length [length, damaged, tauch_control, total_length]
    boats = {el:[0, 0, 1, 0] for b in board for el in b if el > 0}
    for i in boats.keys():
        result['not_touched'] += 1
        for b in board:
            boats[i][0] += b.count(i)
        boats[i][3] += boats[i][0]

    for a in attacks:
        pos = board[a[1] * -1][a[0] - 1]

        if pos != 0:
            # Decrease boat length
            boats[pos][0] -= 1

            # damaged of boat 
            boats[pos][1] += 0.5

            # change touch 
            boats[pos][2] = 0
            if boats[pos][0] == 0:
                # Sunken boats
                result['sunk'] += 1
                result['points'] += 1

    for tp in boats.values():
        if tp[2] == 0:
            result['not_touched'] -= 1

        if tp[0] > 0:
            result['damaged'] += tp[1]

    result['points'] += 0.5 * (len(boats.keys()) - result['not_touched'] - result['sunk'])
    result['points'] -= result['not_touched']

    if math.modf(result['points'])[0] == 0.0:
        result['points'] = round(result['points'])


    if math.modf(result['damaged'])[0] == 0.5:
        result['damaged'] = math.ceil(result['damaged'])
    else:
        result['damaged'] = round(result['damaged'])
    return result

# -------------------------------------
# Basic Tests


board = [ [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0] ]

attacks = [[3, 1], [3, 2], [3, 3]];
result = damaged_or_sunk(board, attacks)

print("Game 1 result: { 'sunk': 1, 'damaged': 0 , 'not_touched': 0, 'points': 1}")
print(result['sunk'], 1)
print(result['damaged'], 0)
print(result['not_touched'], 0)
print(result['points'], 1)

board = [ [3, 0, 1],
          [3, 0, 1],
          [0, 2, 1],
          [0, 2, 0] ]

attacks = [[2, 1], [2, 2], [ 3, 2], [3, 3]]
result = damaged_or_sunk(board, attacks)
print("Game 2 result: { 'sunk': 1, 'damaged': 1 , 'not_touched': 1, 'points': 0.5}")
print(result['sunk'], 1)
print(result['damaged'], 1)
print(result['not_touched'], 1)
print(result['points'], 0.5)
print(result)
