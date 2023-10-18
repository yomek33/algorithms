import time
# n = int(input())
# t = list(map(int, input().split()))


# O(n^2)
def MinTotalWaitingTime(t, n):
    waitingTime = 0
    treated = [0] * n
    for i in range(n):
        T_min = float('inf')
        min = 0
        for j in range(n):
            if t[j] < T_min and treated[j] == 0:
                T_min = t[j]
                min = j
        treated[min] = 1
        waitingTime += T_min * (n-i-1)

    return waitingTime


start = time.time()
n = 5
t = [2, 5, 1, 3, 4]
totaltime = MinTotalWaitingTime(t, n)
end = time.time()
print(totaltime)
print("MinTotalWaitingTime: ", end - start)

start = time.time()
n = 3
t = [20, 15, 10]
totaltime = MinTotalWaitingTime(t, n)
end = time.time()
print(totaltime)
print("MinTotalWaitingTime: ", end - start)

# 20
# MinTotalWaitingTime:  1.1205673217773438e-05
# 35
# MinTotalWaitingTime:  3.814697265625e-06
