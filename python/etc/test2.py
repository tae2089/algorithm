import mo

def add(a,b):
    return a+b

def test_answer():
    a = add(2,3)
    b = [1,2,3,4,5,6]
    assert a in b

def test_mo():
    a = mo
    c = a.hello.hello()
    assert "hello" == c



def test_answer2():
    a = add(2, 3)
    b = [1, 2, 3, 4, 5, 6]
    assert a not in b , "this element don 't exist in b"
