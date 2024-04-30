import math

ls_t = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6

ls_nn = sum(int(i) for i in ls_t if i >= MIN and i <= MAX)
print(ls_nn)

ls_qq = math.prod(int(i) for i in ls_t if i >= MIN and i <= MAX)
print(ls_qq)











# lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
# MIN = 3
# MAX = 6
# ...
# sum_ = 20, product = 576
