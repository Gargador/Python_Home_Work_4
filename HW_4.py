# Задача 22:
n, m = map(int, input().split())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
intersection = sorted(list(set1.intersection(set2)))
print(*intersection)


# Задача 24:
n = int(input())
berries = list(map(int, input().split()))

def maxBerries(berries):
    max_sum = 0
    for i in range(len(berries)):
        sumBerries = sum(berries[i:i+3])
        if sumBerries > max_sum:
            max_sum = sumBerries
    return max_sum

print(maxBerries(berries))
