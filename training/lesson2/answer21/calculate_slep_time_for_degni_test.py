from training.lesson2.answer21.calculate_slep_time_for_degni import calculate_sleep_time_for_degni
from training.lesson2.answer21.calculate_slep_time_for_degni import hh_mm_to_str

def test_calculate_sleep_time_2():
    mm = calculate_sleep_time_for_degni(57)
    assert (mm) == 14.25

def test_hh_mm_to_str_2():
    text = hh_mm_to_str(14.25)
    assert text == "14.25 м"

