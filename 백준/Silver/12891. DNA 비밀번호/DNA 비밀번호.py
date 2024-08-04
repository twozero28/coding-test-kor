S, P = map(int, input().split())
dna_str = input()
a, c, g, t = map(int, input().split())

a_cnt = 0
c_cnt = 0
g_cnt = 0
t_cnt = 0


for i in range(P):
    if dna_str[i] == 'A':
        a_cnt += 1
    elif dna_str[i] == 'C':
        c_cnt += 1
    elif dna_str[i] == 'G':
        g_cnt += 1
    elif dna_str[i] == 'T':
        t_cnt += 1

count = 0
if a_cnt >= a and c_cnt >= c and g_cnt >= g and t_cnt >= t:
    count += 1

start_index = 0
end_index = P

while end_index < S:
    subtract_char = dna_str[start_index]
    add_char = dna_str[end_index]
    if add_char == 'A':
        a_cnt += 1
    elif add_char == 'C':
        c_cnt += 1
    elif add_char == 'G':
        g_cnt += 1
    elif add_char == 'T':
        t_cnt += 1

    if subtract_char == 'A':
        a_cnt -= 1
    elif subtract_char == 'C':
        c_cnt -= 1
    elif subtract_char == 'G':
        g_cnt -= 1
    elif subtract_char == 'T':
        t_cnt -= 1
    
    if a_cnt >= a and c_cnt >= c and g_cnt >= g and t_cnt >= t:
        count += 1
    
    start_index += 1
    end_index += 1

print(count)
