list_1 = [["a", "c", "e"],
          ["f", "b", "a"],
          ["a", "n", "k"],
          ["e", "l", "i"]]

list_2 = [sorted([list_1[y][x] for y in range(len(list_1))]) for x in range(len(list_1[0]))]

list_3 = [([list_2[y][x] for y in range(len(list_2))]) for x in range(len(list_2[0]))]
for y in list_3:
    for x in y:
        print(x, end=", ")
    print("")

