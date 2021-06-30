def rook_hit_or_not(first_coordinate_of_the_white_rook, second_coordinate_of_the_white_rook,
                     first_coordinate_of_the_black_rook, second_coordinate_of_the_black_rook):
    if first_coordinate_of_the_white_rook == first_coordinate_of_the_black_rook or second_coordinate_of_the_white_rook == second_coordinate_of_the_black_rook:
        print("YES")
    else:
        print("NO")
    return

if __name__ ==  "__main__":
    w1 = input("Введите букву координаты белой ладьи: ")
    w2 = int(input("Введите цифру координаты белой ладьи: "))
    b1 = input("Введите букву координаты черной ладьи: ")
    b2 = int(input("Введите цифру координаты черной ладьи: "))
    r = rook_hit_or_not(w1,w2,b1,b2)