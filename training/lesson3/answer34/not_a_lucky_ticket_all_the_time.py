def sum_the_first_three_digits_of_the_ticket_number(first_three_digits_of_the_ticket_number):
    # вычисляем первое число
    a = first_three_digits_of_the_ticket_number
    a1 = a // 100
    # вычисляем второе число
    a2 = (a % 100) // 10
    # вычисляем третье число
    a3 = a - a1*100 - a2*10
    # сумма 3-х чисел в биллете
    sum1 = int(a1) + int(a2) + int(a3)
    return sum1

def sum_the_second_three_digits_of_the_ticket_number(second_three_digits_of_the_ticket_number):
    # вычисляем первое число
    a = second_three_digits_of_the_ticket_number
    a1 = a // 100
    # вычисляем второе число
    a2 = (a % 100) // 10
    # вычисляем третье число
    a3 = a - a1*100 - a2*10
    # сумма 3-х чисел в биллете
    sum2 = int(a1) + int(a2) + int(a3)
    return sum2


def plus_one_to_the_original_number(second_three_digits_of_the_ticket_number):
    new_second_three_digits_of_the_ticket_number = second_three_digits_of_the_ticket_number + 1
    return  new_second_three_digits_of_the_ticket_number

def convert_999_to_000(second_three_digits_of_the_ticket_number):
    second_three_digits_of_the_ticket_number = to_000(0)
    return second_three_digits_of_the_ticket_number

# преобразовываем число "0" в "000"
def to_000(second_three_digits_of_the_ticket_number):
    new_three_digits_of_the_ticket_number = str(second_three_digits_of_the_ticket_number).zfill(3)
    return new_three_digits_of_the_ticket_number

 
if __name__ == "__main__":
    num_1 = int(input("Введите первые три цифры номера билета(первая цифра не может быть равна 0): "))
    num_2 = int(input("Введите вторые три цифры номера: "))
    sum_1 = sum_the_first_three_digits_of_the_ticket_number(num_1)
    sum_2 = sum_the_second_three_digits_of_the_ticket_number(num_2)
    if sum_1 != sum_2:
        print(str(num_1) + str(to_000(num_2)))
    elif sum_1 == sum_2 and num_2 == 999:
        print(str(num_1) + str(to_000(convert_999_to_000(num_2))))
    else:
        print(str(num_1) + str(to_000(plus_one_to_the_original_number(num_2))))


