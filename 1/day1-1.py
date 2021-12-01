with open("input1.txt") as f: 
    data = f.readlines() 

print("Data: " + str(data))

increases = 0
last_num = -1

for d in data:
    d = int(d)
    print("Item: " + str(d) + ", last_num: " + str(last_num))
    if d == "":
        break
    if last_num == -1:
        last_num = d
        continue
    if d > last_num:
        increases += 1
    last_num = d

print("Increases: " + str(increases))