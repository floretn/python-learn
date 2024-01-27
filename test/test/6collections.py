nums = [1, 3, 5, 21, 43, 21, True, 'gh', [1, 2, False]]
nums[2] = 60
print(nums)
print(nums[len(nums) - 1][0])
print(nums[-1][-1])

numbers = [6, 12, 34, 12, 32]
numbers.insert(1, 1000)
numbers.append(6)
numbers.extend([5, 6, 8])
print(numbers)
numbers.sort()
print(numbers)
numbers.pop()
numbers.remove(6)
numbers.reverse()
print(numbers)
print(numbers.count(6))

numbers = [5, 2, 1, "50", False]
for i in numbers:
    print(i * 2)

n = int(input("Enter len: "))
userList = []

for i in range(0, n):
    userList.append(input("Enter element #" + str(i) + ": "))
print(userList)

word = 'itproger'
print(word[3])
print(len(word))
print(word.count('r'))
print(word.upper())
print(word.islower())
print(word.capitalize())
print(word.find('b'))
print(word.split('r'))

word = "football, basketball, skate, volleyball"
hobbies = word.split(', ')
for i in range(len(hobbies)):
    hobbies[i] = hobbies[i].capitalize()
print(hobbies)
result = ", ".join(hobbies)
print(result)

word = "Football"

print(word[0:4])
print(word[4:])
print(word[0::2])

lis = [6, 1, "fsd", True, 1.2]
print(lis[::-2])

data = (1, 3, 5, 32, 4565, "fsd", 21.21, True)
print(data[::-1])
print(data.count(3))
print(len(data))
print(data)

data = 1, 32, 132, True, "tre"
for i in data:
    print(i)
print(data)
data = (5)
print(data)
data = (5,)
print(data)
data = 5,
print(data)
nums = [1, 2, 3, 4]
new_nums = tuple(nums)
print(new_nums)
word = tuple("Hello world!")
print(word)

country = {4: 3, 1: 2, "Europe": 4, "Spain": 2, (1, 2): 123}
country = {'code': 'RU', 'name': 'Russia', 'population': 144}
print(country)
country = dict(code='RU', name='Russia')
print(country)
print(country['name'])
print(country.items())
for key, value in country.items():
    print(key, '-', value)

print(country.get('name'))
# country.clear()
print(country)
# print(country.pop('name'))
# print(country.popitem())
# print(country)
country['population'] = 1223
print(country.values())
print(country.keys())

persons = {
    'user_1': {
        'first_name': 'Ivan',
        'last_name': 'Sofronov',
        'email': 'some@some.some',
        'age': 123,
        'hobbies': ['football', 'swimming', 'drawing']
    },
    'user_2': {
        'first_name': 'Vlad',
        'last_name': 'Smirnov',
        'email': 'so@so.so',
        'age': 21
    }
}

print(persons['user_1']['hobbies'][2])

data = set('hello')
data = {1, 4, 5, 4, 5}
data.add(54)
print(data)
data.update([1, 32, 43, 54])
print(data.pop())
data.remove(5)
print(data)

data = [1, 2, 2, 5, 1, 43, 423, 123]
data = set(data)
print(data)

data = frozenset([1, 4, 213, 43, 65, 4])
print(data)