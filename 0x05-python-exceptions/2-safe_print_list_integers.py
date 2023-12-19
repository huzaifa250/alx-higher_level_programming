#!/usr/bin/python3
s = 0
for i in range(x):
    try:
        print("{:d}".format(my_list[i])
        s += 1
    except (ValueError, TypeError):
        continue
print()
return s
