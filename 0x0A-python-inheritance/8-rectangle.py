#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

re = Rectangle(3, 5)

print(re)
print(dir(re))

try:
    print("Rectangle: {} - {}".format(re.width, re.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    re2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
