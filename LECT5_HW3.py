# lst = [1, 2, 3, 4, 5]
# Result: [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# ------------------------------------------------

lst1 = [1, 2, 3, 4, 5]
lst2 = []
prev = None

for i in lst1:
    if prev is None:
        prev = i
        lst2.append(i)
        continue
    lst2.append((prev + i) / 2)
    lst2.append(i)
    prev = i
print(lst2)

