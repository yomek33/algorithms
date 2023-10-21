def largestConcatenate(numbers):
    result = ""
    while numbers:
        maxNum = max(numbers)
        result += str(maxNum)
        numbers.remove(maxNum)
    return result


print(largestConcatenate([2, 21, 12]))
# output: 22112


def largestConcatenateRecur(numbers):
    if len(numbers) == 1:
        return str(numbers[0])
    maxNum = max(numbers)
    numbers.remove(maxNum)
    return str(maxNum) + largestConcatenateRecur(numbers)


print(largestConcatenateRecur([2, 21]))
# output: 2212


def MoneyChange(num, coins):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += num // coin
        num %= coin
    return count


print(MoneyChange(8,  [1, 4, 6]))
# output: 6
