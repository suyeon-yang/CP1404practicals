import random

NUMBERS_IN_EACH_LINE = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_picks = int(input("How many quick picks?: "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_IN_EACH_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()

    print(", ".join(str(number) for number in quick_pick))


