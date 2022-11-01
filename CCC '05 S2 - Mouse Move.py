def to_int(list):
    for i in range(len(list)):
        list[i] = int(list[i])
    return list

def translate(position, movements, boundary, n):
    if position[n] + movements[n] >= boundary[n]:
        position[n] = boundary[n]
    elif position[n] + movements[n] <= 0:
        position[n] = 0
    else:
        position[n] += movements[n]


boundary = to_int(input().split(" "))
movements = []
continuing = True
while continuing:
    movement = to_int(input().split(" "))
    if movement == [0, 0]:
        continuing = False
    else:
        movements.append(movement)
position = [0, 0]
for i in range(len(movements)):
    translate(position, movements[i], boundary, 0)
    translate(position, movements[i], boundary, 1)
    print("%d %d" % (position[0], position[1]))
