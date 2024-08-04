N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

count = 0
for n in range(N):
    K = numbers[n]
    i = 0
    j = N - 1
    while i < j:
        if numbers[i] + numbers[j] > K:
            j -= 1
        elif numbers[i] + numbers[j] < K:
            i += 1
        else:
            if i != n and j != n:
                count += 1
                break
            elif i == n:
                i += 1
            elif j == n:
                j -= 1

print(count)