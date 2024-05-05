Dictionary = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}

print("key value item")

for i, (key, value) in enumerate(Dictionary.items(), start=1):
    print(f"{key:}   {value:}    {i:}")