name = input("camelCase: ")

output = ""

for char in name:
    if char.isupper():
        output += '_' + char.lower()
    else:
        output += char
        
print("snake_case:", output)