data = [2.71, 42, 123, 2, 3.14, 1.61]

while True:
    moved = False
    for i in range(0, len(data)- 1):
        a = data[i]
        b = data[i + 1]

        if a > b:
            data[i], data[i + 1] = data[i + 1], data[i]
            moved = True
        
    if moved == False:
        break

print(data)