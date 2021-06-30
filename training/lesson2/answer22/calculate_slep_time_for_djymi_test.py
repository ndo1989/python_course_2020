from training.lesson2.answer22.calculate_slep_time_for_djymi import calculate_sleep_time_for_djymi
from training.lesson2.answer22.calculate_slep_time_for_djymi import hh_mm_to_str

def test_calculate_sleep_time_2():
    hh, mm = calculate_sleep_time_for_djymi(124)
    assert (hh, mm) == (1, 2)

def test_hh_mm_to_str_1():
    text = hh_mm_to_str(1, 2)
    assert text == "1 ч 2 м"

def test_calculate_sleep_time_1():
    hh, mm = calculate_sleep_time_for_djymi(57)
    assert (hh, mm) == (0, 28)

def test_hh_mm_to_str_2():
    text = hh_mm_to_str(0, 28)
    assert text == "28 м"
