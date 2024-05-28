my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
lenght_ = len(my_list)
while a < lenght_:
    print(my_list[a])
    a = a + 1
    if my_list[a] < 0:
        break
