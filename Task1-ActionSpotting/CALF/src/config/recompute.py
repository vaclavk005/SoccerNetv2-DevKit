list = [[-40, -8, -37, -39, -12, -30, -38, -30],
        [-20, -4, -18, -20, -6, -14, -19, -15],
        [20, 24, 18, 20, 6, 14, 19, 15],
        [40, 36, 37, 39, 12, 30, 38, 30]]

for sublist in list:
    for i in range(len(sublist)):
        sublist[i] = int(sublist[i] * 2)

print(list)