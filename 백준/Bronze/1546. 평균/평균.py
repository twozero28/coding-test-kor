N = int(input())
number_list = list(map(int, input().split()))
M = max(number_list)

result = 0

for n in number_list:
    result += n / M * 100

print(result / N)