def testuj_zbiory():
    zbior_liczb = {1, 2, 3, 4, 5, 6, 7, 3, 1}
    print(zbior_liczb)
    print("Czy '7' znajduje się w zbiorze:", 7 in zbior_liczb)
    print("Czy '9' znajduje się w zbiorze:", 9 in zbior_liczb)
    print("Ilość elementów zbioru:", len(zbior_liczb))
    print()

    zbior_liczb.add(8)
    zbior_liczb.add(9)
    print(zbior_liczb)
    print("Czy '9' znajduje się w zbiorze:", 9 in zbior_liczb)
    print("Ilość elementów zbioru:", len(zbior_liczb))
    print()

    zbior_liczb.remove(4)
    zbior_liczb.remove(6)
    print(zbior_liczb)
    print()

    zbior_liczb.pop()
    zbior_liczb.pop()
    print(zbior_liczb)
    print()

    zbior_a = {1, 2, 3, 5, 8}
    zbior_b = {5, 6, 7, 8, 9}
    print("Zbiór A:", zbior_a, "\t\tZbiór B:", zbior_b)
    print("Zbiór A suma B:", zbior_a | zbior_b)
    print("Zbiór A iloczyn B:", zbior_a & zbior_b)
    print("Zbiór A różnica B:", zbior_a - zbior_b)
    print("Zbiór A różnica symetryczna B:", zbior_a ^ zbior_b)
    pass


testuj_zbiory()
