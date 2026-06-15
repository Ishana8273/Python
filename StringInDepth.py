chai = "Lemon Chai"
print(chai)

print(chai[0])

slice_chai = chai[0:5]
print(slice_chai)

print(chai[-1])

print(chai[-4:-1])

num_list = "0123456789"
print(num_list[:10])

print(num_list[::2])

print(num_list[3:10:3])

print(chai.upper())

print(chai.lower())

chai_one= "     Ginger Chai     "

print(chai_one.strip())

print(chai_one.lstrip())

print(chai_one.rstrip())

print(chai.replace("Lemon","Masala"))

chai_two = "Lemon, Ginger, Masala"

print(chai_two.split())
# ['Lemon,', 'Ginger,', 'Masala']

print(chai_two.split(", "))
# ['Lemon', 'Ginger', 'Masala']

print(chai_two.find("Ginger"))
# 7

print(chai_two.find("lemon"))
# -1

chai_three = "Lemon chai Chai chai"

print(chai_three.count("chai"))
# 2

chai_type = "Masala"
quantity = 2

order = "I would like {} cups of {} chai"
print(order.format(quantity, chai_type))

chai_variety = ["Lemon", "Ginger", "Masala"]

print(chai_variety)

print("".join(chai_variety))

print(", ".join(chai_variety))


print(" and ".join(chai_variety))
# Lemon and Ginger and Masala

chai = "Lemon Chai"

print(len(chai))

for letter in chai:
    print(letter)

# printing string with double quotes inside it
chai1 = "He Said, \"I love Chai!\""

print(chai1)

chai2 = "Masala\nchai"

print(chai2)

chai2 = r"Masala\nchai"

print(chai2)

# path = r"C:\Users\ChaiLover\Documents\chai.txt"
# print(path)

# path printing
path = r"C:\Users\ChaiLover\Documents\chai.txt"
print(path)

# conataining query
chai = "Masala Chai"

print("Chai" in chai)

print("Ginger" in chai)

qr = """i
am
vansh
malik"""

print(qr)

