# Test values:
# ls_t = [2, 4, 6, 2, 1, 1, 9, 4, 6]
# ls_t = [2, 3, 4, 5, 6, 7, 8]
# ls_t = []
# ls_t = [1, -1]
# ls_t = [-1, 1]
# ls_t = [1, 1, 1, 1, 1]
# ls_t = [4, 0]

ls_t = [2, 4, 6, 2, 1, 1, 9, 4, 6]

MIN = 3
MAX = 6
# MIN = -30
# MAX = 60

sum_1 = None
for i in ls_t:
    if i >= MIN and i <= MAX:
        if sum_1 is None:
            sum_1 = i
        else:
            sum_1 += i
print(sum_1)


prd = None
for i in ls_t:
    if i >= MIN and i <= MAX:
        if prd is None:
            prd = i
        else:
            prd *= i
print(prd)





