# Number 1

name_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=name_file)
name_file.close()

# Number 2

name_open_file = open("name.txt", "r")
name = name_open_file.read().strip()
name_open_file.close()
print("Your name is", name)

# Number 3

number_file = open("numbers.txt", "r")
number1 = int(number_file.readline())
number2 = int(number_file.readline())
number_file.close()
print(number1 + number2)

# Number 4

number_file = open("numbers.txt", "r")
total = 0
for line in number_file:
    number = int(line)
    total += number
number_file.close()
print(total)