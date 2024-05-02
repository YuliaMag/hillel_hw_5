
ls_t = [2, 4, 6, 2, 1, 1, 9, 4, 6]
#ls_t = []

MIN = 3
MAX = 6

sum = 0
for i in ls_t:
    if i >= MIN and i <= MAX:
        sum += i
if sum != 0:
    print(sum)
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












# lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
# MIN = 3
# MAX = 6
# ...
# sum_ = 20, product = 576
