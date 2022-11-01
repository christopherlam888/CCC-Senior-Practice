daysNumber = int(input())
swifts = input().split(" ")
semaphores = input().split(" ")
swifts_sum = 0
semaphores_sum = 0
for i in range(daysNumber):
    swifts_sum += int(swifts[i])
    semaphores_sum += int(semaphores[i])
K = 0
counter = daysNumber
while counter > 0:
    if swifts_sum == semaphores_sum:
        K = counter
        counter = 0
    swifts_sum -= int(swifts[counter-1])
    semaphores_sum -= int(semaphores[counter-1])
    counter -= 1
print(K)
