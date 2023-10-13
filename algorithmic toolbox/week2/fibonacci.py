import time
a = int(input())


def fibRecurs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibRecurs(n - 1) + fibRecurs(n - 2)


def fibList(a):
    fib = [0, 1]  # リストの初期化
    for i in range(2, a + 1):  # 2番目からa番目までのフィボナッチ数を計算
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[a]


# 実行時間の比較
start = time.time()
print("fibRecurs: ", fibRecurs(a))
end = time.time()
print("fibRecurs: ", end - start)

start = time.time()
print("fibList: ", fibList(a))
end = time.time()
print("fibList: ", end - start)


#   python3 fibonacci.py
# 20
# fibRecurs:  6765
# fibRecurs:  0.003050088882446289
# fibList:  6765
# fibList:  3.0279159545898438e-05
