list = [1,2,1,3,5,6,4]
max = list[0] # 1
index = 0
for i in range(0, len(list)):
    if list[i] > max:
        print(list[i])
        max = list[i]
        index = i
print(f'index = {index}')