from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

#README !!!
#Para tener una collection de tests, crear un directioro solo con los tests.
#Se puede tratar como un package.
#Se puede testear solo poniendo "pytest test" (suponiendo que el directorio se llama test).
