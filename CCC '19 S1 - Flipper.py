grid = [[1, 2], [3, 4]]
flips = list(input())
for i in range(len(flips)):
    if flips[i] == "H":
        temp = grid[0][0]
        grid[0][0] = grid[1][0]
        grid[1][0] = temp
        temp = grid[0][1]
        grid[0][1] = grid[1][1]
        grid[1][1] = temp
    elif flips[i] == "V":
        temp = grid[0][0]
        grid[0][0] = grid[0][1]
        grid[0][1] = temp
        temp = grid[1][0]
        grid[1][0] = grid[1][1]
        grid[1][1] = temp
print("%d %d" % (grid[0][0], grid[0][1]))
print("%d %d" % (grid[1][0], grid[1][1]))
