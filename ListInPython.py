tea_varities = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]

print("List of Tea Varieties:")
print(tea_varities)

print(tea_varities[0]) # Accessing the first element

print(tea_varities[-1]) # Accessing the last element

print(tea_varities[1:3]) # Slicing the list

print(tea_varities[:2]) # Slicing from the beginning to the second element

print(tea_varities[2:]) # Slicing from the third to the fourth element

tea_varities[3] = "Herbal Tea"

print(tea_varities) # Modifying an element in the list

print(tea_varities[1:2]) # Slicing to get a single element as a list   

tea_varities[1:2] = "Matcha Tea" 
print(tea_varities) # Modifying a slice of the list

tea_varities = ["Black Tea", "Green Tea", "Oolong Tea", "White Tea"]

tea_varities[1:2] = ["Matcha Tea"]
print(tea_varities) # Modifying a slice of the list

print(tea_varities[1:3]) # Slicing to get multiple elements as a list

tea_varities[1:3] = ["Matcha Tea", "Chai Tea"]

print(tea_varities) # Modifying a slice of the list

print(tea_varities)

print(tea_varities[1:1]) # Slicing to get an empty list

tea_varities[1:1] = ["test", "test"]  

print(tea_varities) # Inserting elements into the list using slicing

tea_varities[1:3] = [] # Removing elements from the list using slicing

print(tea_varities)

print(len(tea_varities)) # Getting the length of the list

print(tea_varities) 

for tea in tea_varities:
    print(tea) # Iterating through the list and printing each element

for tea in tea_varities:
    print(tea.upper()) # Iterating through the list and printing each element in uppercase

for tea in tea_varities:
    print(tea.lower()) # Iterating through the list and printing each element in lowercase

for tea in tea_varities:
    print(tea, end="-") # Iterating through the list and printing each element on the same line separated by a hyphen   

    