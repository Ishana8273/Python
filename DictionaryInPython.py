chai_types = {"Masala": "Spicy", "Ginger": "Zingy", "Lemon": "Tangy"}
print(chai_types)

print(chai_types["Masala"] )

print(chai_types.get("Masala"))

print(chai_types.get("Lemonn"))

# print(chai_types["Lemonn"])  gives error

chai_types["Lemonn"] = "Citrusy"

for chai in chai_types:
    print(chai) 

for chai in chai_types:
    print(chai, chai_types[chai])

    
for key,value in  chai_types.items():
    print(key,value)

if "Masala" in  chai_types:
    print("Masala chai is exists in the dictionary")            

print(len(chai_types))

print(chai_types)

chai_types["Earl Grey"] = "Citrus"

print(chai_types)

chai_types.pop("Masala")

print(chai_types)

chai_types.popitem() # Removes the last inserted item (Earl Grey in this case)
print(chai_types)

del chai_types["Ginger"] # Removes the item with the specified key (Ginger in this case)

print(chai_types)

tea_types_copy = chai_types.copy()

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zingy", "Lemon": "Tangy"},
    "tea": {"Black": "Bold", "Green": "Fresh", "Oolong": "Smooth"}
}

print(tea_shop)

print(tea_shop["chai"])

print(tea_shop["tea"]["Green"])

squared_num = {x:x**2 for x in range(10)}
print(squared_num)

squared_num.clear()

keys = ["Masala", "Ginger", "Lemon"]

default_value = "Delicious"

new_dict = dict.fromkeys(keys,default_value)
print(new_dict)

new_dict= dict.fromkeys(keys,keys)
print(new_dict)

