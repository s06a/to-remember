def separator(list):
    list1, list2 = [], []
    for l in list:
        if l % 2 == 0:
            list1.append(l)
        else:
            list2.append(l)
    return (list1, list2)

list = input()
separator(list)

