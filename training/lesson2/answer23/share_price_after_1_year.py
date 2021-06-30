def share_price_after_1_year(start_price, percentage_of_growth):
    # итоговая прибыль за 1 год (12 месяцев)
    total_price = float(start_price*((1 + percentage_of_growth)**12))
    return f'{total_price} $'

def share_price_after_1_year(start_price, percentage_of_growth):
    # итоговая прибыль за 1 год (12 месяцев)
    total_price = float(start_price*((1 + percentage_of_growth)**12))
    return f'{total_price} $'


if __name__ == "__main__":
    x = int(input("Введите начальную цену акций: "))
    k = int(input("Введите процент роста акций в виде десятичной дроби, к примеру 0.09 : "))
    s = share_price_after_1_year(x, k)
    print("Новая цена акций " + s)
