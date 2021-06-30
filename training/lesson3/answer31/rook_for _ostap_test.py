from training.lesson3.answer31.rook_for_ostap import rook_hit_or_not

def test_rook_hit_or_not_1():
    yon = rook_hit_or_not("B",5,"B",8)
    assert yon == "YES"

def test_hit_or_not_2():
    yon = rook_hit_or_not("B",5,"E",5)
    assert yon == "YES"

def test_hit_or_not_3():
    yon = rook_hit_or_not("B",5,"E",4)
    assert yon == "NO"
z


