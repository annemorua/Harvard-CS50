from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
#Hay que instalar pip install pytest.
#Se pone en la terminal "pytest test1_calculator.py".
