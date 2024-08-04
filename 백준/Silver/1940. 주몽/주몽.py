N = int(input())
M = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

start_index = 0
end_index = N - 1
count = 0

while start_index < end_index:
    end_number = numbers[end_index]
    start_number = numbers[start_index]
    if end_number + start_number > M:
        end_index -= 1
    elif end_number + start_number < M:
        start_index += 1
    else:
        count += 1
        end_index -= 1
        start_index += 1

print(count)