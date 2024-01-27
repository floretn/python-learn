try:
    x = int(input("Enter number: "))
    x += 5
    print(x)
except ValueError:
    print("Invalid input ")

try:
    x = 5 / 1
    x = int(input())
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
else:
    print("The result")
finally:
    print('Finally')

try:
    file = open('test.txt', 'r')
    file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close() #file not ex

try:
    with open('data/test.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found')