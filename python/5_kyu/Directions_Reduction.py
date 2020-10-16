# Kata link:
# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
# -------------------------------------
# Solution 1:

def dirReduc(arr):
    for _ in range(len(arr) // 2):
        if len(arr) > 1:
            for x in range(len(arr) - 1):
                if arr[x] == 'NORTH' and arr[x+1] == 'SOUTH' or arr[x] == 'SOUTH' and arr[x+1] == 'NORTH':
                    del arr[x:x+2]
                    break
                elif arr[x] == 'EAST' and arr[x+1] == 'WEST' or arr[x] == 'WEST' and arr[x+1] == 'EAST':
                    del arr[x:x+2]
                    break
        else:
            break
    return arr

# Solution 2:

# opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

# def dirReduc(plan):
    # new_plan = []
    # for d in plan:
        # if new_plan and new_plan[-1] == opposite[d]:
            # new_plan.pop()
        # else:
            # new_plan.append(d)
    # return new_plan

# -------------------------------------
# Basic Tests


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

print(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]

print(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])

