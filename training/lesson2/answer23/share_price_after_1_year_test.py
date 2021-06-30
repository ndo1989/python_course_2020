from training.lesson2.answer23.share_price_after_1_year import share_price_after_1_year

def test_share_price_after_1_year_1():
    s = share_price_after_1_year(100, 0.12)
    assert s == "389.5975992546981 $"

def test_share_price_after_1_year_2():
    s = share_price_after_1_year(500, 1)
    assert s == "2048000.0 $"

def test_share_price_after_1_year_3():
    s = share_price_after_1_year(1, 1)
    assert s == "4096.0 $"

def test_share_price_after_1_year_4():
    s = share_price_after_1_year(1, 0.01)
    assert s == "1.1268250301319698 $"