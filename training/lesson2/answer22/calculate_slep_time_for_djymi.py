def calculate_sleep_time_for_djymi(minutes_for_finished):
    # сколько всего минут будет отведено на сон
    st = minutes_for_finished // 2
    # сколько целых часов будет длится сон
    h = st // 60
    # сколько минут (учитывая часы) будет длится сон
    m = st % 60
    return h, m

def hh_mm_to_str(hh, mm):
    if hh == 0:
        return f'{mm} м'
    return f'{hh} ч {mm} м'


if __name__ == "__main__":
    t = int(input("Введите количество минут до конца поездки: "))
    hh, mm = calculate_sleep_time_for_djymi(t)
    hm = hh_mm_to_str(hh, mm)
    print("Джими потратит на сон " + hm)

