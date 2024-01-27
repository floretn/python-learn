data = input("Enter your text: ")
file = open('/test/data/test.txt', 'w')
file.write('Hello world')
file.write('!!!\n')
file.write(data)
file.close()

file = open('/test/data/test1.txt', 'r')
# print(file.read(10))
for line in file:
    print(line, end='')
file.close()