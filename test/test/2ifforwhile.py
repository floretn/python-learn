userData = int(input("Enter the number of: "))
flag = True
if userData >= 5 or flag and not flag:
    print("Yes")
    if userData == 5:
        print("Yes Yes!!!")
    print("End")
elif userData == 4:
    print("Govno")
elif userData == 3:
    print("Govno4")
else:
    print("No")

data = input()
number = 5 if data == 5  else 0
print(number)

for i in range(2, 7, 2):
    print(i)

cnt = 0
word = "Hello world!"
for i in word:
    # print(i * 3)
    if i == 'l':
        cnt += 1
print(cnt)

i = 5
while i > 0:
    print(i)
    i -= 1

isStartingCar = True
while isStartingCar:
    word = input()
    if word == 'Stop':
        isStartingCar = False

for i in range(1, 11, 2):
    if i >= 9:
        break
    if i % 2 == 0:
        continue
    print(i)

isFound = None
for i in "Hello":
    if i == 'l':
        isFound = True
        break
    else:
        isFound = False

print(isFound)