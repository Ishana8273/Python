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

