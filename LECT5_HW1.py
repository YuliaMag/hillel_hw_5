orig_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(orig_list)


lst1 = []
for i in range(len(orig_list)):
    if i % 3 == 0 and i % 5 != 0:
        lst1.append(i)
print(lst1)


lst2 = []
for i in range(len(orig_list)):
    if i % 3 != 0 and i % 5 == 0:
        lst2.append(i)
print(lst2)


lst3 = []
for i in range(len(orig_list)):
    if i % 3 == 0 and i % 5 == 0:
        lst3.append(i)
print(lst3)










# ER:
# [3, 6, 9, 12]  # elements divided by 3
# [5, 10]  # elements divided by 5
# [0, 15]  # elements divided by 3 and by 5


