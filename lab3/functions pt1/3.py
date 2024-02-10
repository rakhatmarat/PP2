def solve(numheads, numlegs):

    for c in range(numheads + 1):
        r = numheads - c
        if 2 * c + 4 * r == numlegs:
            return c, r
    return None, None

numheads = 35
numlegs = 94

chickens, rabbits = solve(numheads, numlegs)

if chickens is not None and rabbits is not None:
    print("Number of chickens:", chickens)
    print("Number of rabbits:", rabbits)
else:
    print("No solution found.")
