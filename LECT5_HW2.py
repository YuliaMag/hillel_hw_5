# Test values:
# ls_t = [2, 4, 6, 2, 1, 1, 9, 4, 6]
# ls_t = [2, 3, 4, 5, 6, 7, 8]
# ls_t = []
# ls_t = [1, -1]
# ls_t = [-1, 1]
# ls_t = [1, 1, 1, 1, 1]

ls_t = [2, 4, 6, 2, 1, 1, 9, 4, 6]


MIN = 3
MAX = 6

sum_1 = 0
for i in ls_t:
    if i >= MIN and i <= MAX:
        sum_1 += i
if sum_1 != 0:
    print(sum_1)
else:
    print(None)


prd = 0
for i in ls_t:
    if i >= MIN and i <= MAX:
        if prd == 0:
            prd = i
        else:
            prd *= i
if prd != 0:
    print(prd)
else:
    print(None)




