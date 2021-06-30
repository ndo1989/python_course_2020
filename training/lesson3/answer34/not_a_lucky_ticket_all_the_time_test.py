from training.lesson3.answer34.not_a_lucky_ticket_all_the_time import sum_the_first_three_digits_of_the_ticket_number
from training.lesson3.answer34.not_a_lucky_ticket_all_the_time import plus_one_to_the_original_number
from training.lesson3.answer34.not_a_lucky_ticket_all_the_time import convert_999_to_000
from training.lesson3.answer34.not_a_lucky_ticket_all_the_time import to_000

def test_sum_the_first_three_digits_of_the_ticket_number_1():
    sum_1 = sum_the_first_three_digits_of_the_ticket_number(123)
    assert sum_1 == 6

def test_plus_one_to_the_original_number_1():
    new_number = plus_one_to_the_original_number(123)
    assert new_number == 124

def test_convert_999_to_000_1():
    new_number_000 = convert_999_to_000(999)
    assert new_number_000 == "000"

def test_to_000_1():
    new_three_digits_of_the_ticket_number = to_000(11)
    assert new_three_digits_of_the_ticket_number == "011"

def test_to_000_2():
    new_three_digits_of_the_ticket_number = to_000(0)
    assert new_three_digits_of_the_ticket_number == "000"

def test_to_000_3():
    new_three_digits_of_the_ticket_number = to_000(11)
    assert new_three_digits_of_the_ticket_number == "011"

def test_to_000_4():
    new_three_digits_of_the_ticket_number = to_000(111)
    assert new_three_digits_of_the_ticket_number == "111"


