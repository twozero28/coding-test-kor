N, M = map(int, input().split())
number_list = list(map(int, input().split()))
sum_list = []
tmp_sum = 0;
for n in number_list:
    tmp_sum += n
    sum_list.append(tmp_sum)

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(sum_list[j - 1])
    else:
        print(sum_list[j - 1] - sum_list[i - 2])
