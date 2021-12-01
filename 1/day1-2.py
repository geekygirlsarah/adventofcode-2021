with open("input1.txt") as f: 
    data = f.readlines() 

print("Data: " + str(data))

increases = 0
last_three = [-1, -1, -1]
last_num_sum = 0

def num_shift(new_num):
    last_three[0] = last_three[1]
    last_three[1] = last_three[2]
    last_three[2] = new_num

def num_sum():
    return last_three[0] + last_three[1] + last_three[2]

for d in data:
    d = int(d)
    print("Item: " + str(d) + ", last sum: " + str(last_num_sum) + ", last three: " + str(last_three))
    if d == "":
        break
    if last_three[0] == -1:
        last_num_sum = 0
        num_shift(d)
        print("   skipped")
        continue
    if num_sum() > last_num_sum:
        increases += 1
    last_num_sum = num_sum()
    num_shift(d)

print("Increases: " + str(increases))