def calculate_sleep_time_for_degni(minutes_for_finished):
    # сколько всего минут будет отведено на сон
    st = minutes_for_finished / 4
    return st

def hh_mm_to_str(mm):
    return f'{mm} м'


if __name__ == "__main__":
    t = int(input("Введите количество минут, через которое поезд прибудет в пункт назначения: "))
    tfs = calculate_sleep_time_for_degni(t)
    mm = hh_mm_to_str(tfs)
    print("Дэгни потратит на сон " + mm)

