w1 = int(input("Введите вес первого стула: "))
w2 = int(input("Введите вес второго стула: "))
w3 = int(input("Введите вес третьего стула: "))
w4 = int(input("Введите вес четвертого стула: "))
if w1 > w2 and w1 > w3 and w1 > w4:
    print("1")
if w2 > w1 and w2 > w3 and w2 > w4:
    print("2")
if w3 > w1 and w3 > w2 and w3 > w4:
    print("3")
if w4 > w1 and w4 > w2 and w4 > w3:
    print("4")