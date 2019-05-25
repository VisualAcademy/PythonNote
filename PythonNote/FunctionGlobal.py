v = 1234

def test1():
    v = "Hello"
    print(v)

test1()

def test2():
    global v 
    v = "Hello"
    print(v)

test2()
print(v)
