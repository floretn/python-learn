def test_func():
    print("Hello world!")
    print("Hello world!".upper())


test_func()
test_func()
test_func()

def test(word):
    print(word)

test("Hello")
test("World")
test("!")

def sum(a, b):
    return a + b


print(sum(1, 2))
print(sum('H', 'i'))

def min(lis):
    min = lis[0]
    for i in lis:
        if i < min:
            min = i
    return min
print(min([1, -12, 43, -4343, 32]))

a = lambda x, y: x * y
print(a(4, 5))