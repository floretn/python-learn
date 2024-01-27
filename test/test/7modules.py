import time

time.sleep(10)
print("Hello World")

import datetime as d
print(d.datetime.now())
print(d.datetime.now().time().minute)

import sys, os, platform
print(sys.path)
print(os.name)
print(platform.system())

from math import sqrt as s
from math import sqrt
print(sqrt(100))
print(s(100))

from test import testmodule as my

print(my.name)
my.hello()

from test.testmodule import add_three_numbers as add
print(add(1, 2, 3))

import cowsay
cowsay.cow("Hello World!")