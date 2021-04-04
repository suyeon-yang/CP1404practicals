"""
first loop
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""
second loop
"""

for j in range(0, 100, 10):
    print(j, end=' ')
print()

"""
third loop
"""

for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""
fourth loop
"""
stars = int(input("Number of stars: "))
for j in range(stars):
    print('*', end=' ')
print()

"""
fifth loop
"""
stars = int(input("Number of stars: "))
for i in range(1, stars + 1):
    print('*' * i)
print()

