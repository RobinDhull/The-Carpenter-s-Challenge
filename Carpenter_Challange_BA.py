''' author: Robin 
    Roll No: 1710991932
'''
# n denotes number of wooden pieces
# x, y and z are the dimensions of wooden pieces
# Assume all dimensions to be in metres.
n = int(input("Enter the total number of wooden pieces: "))
wood = []
x, y, z = [], [], []
for i in range(n):
   x.append(int(input("Enter the length of piece: ")))
   y.append(int(input("Enter the breadth of piece: ")))
   z.append(int(input("Enter the height of piece: ")))
   wood.append(x[i]*y[i]*z[i])

# m denotes the total number of boxes that carpenter wants to make from given pieces of wood.
# m here is optional to keep the wastage minimum.
l, b, h = [], [], []
q = input("Do you want to input the total number of boxes(type 'Y/y' or 'N/n'): ")
if q == 'Y' or q == 'y':
    m = int(input("Enter the total number of boxes you want to make: "))
    query = input("Do you want to input the dimension of boxes(type 'Yes' or 'No'): ")
    boxes = []
    defaultLength = 5
    defaultBreadth = 3
    defaultHeight = 2
    if query == "Yes":
        #  Default value will be considered as l,b,h if user doesn't enter a valid value
        #  l, b and h are the dimensions of wooden boxes
        for i in range(m):
            l.append(int(input(f"Enter the length of box {i+1}: ") or defaultLength))
            b.append(int(input(f"Enter the breadth of box {i+1}: ") or default))
            h.append(int(input(f"Enter the height of box {i+1}: ") or default))
    elif query == 'No':
        for i in range(m):
            l.append(defaultLength)
            b.append(defaultBreadth)
            h.append(defaultHeight)
else:
    m = n
    for i in range(m):
        l.append(5)
        b.append(3)
        h.append(2)

wastage = 0
requiredVol = []

for i in range(m):
    requiredVol.append(l[i]*b[i]*h[i])

requiredVol.sort()
bestIndex = -1
count = 0

for i in range(m):
    bestIndex = -1
    req_vol = requiredVol[i]
    for j in range(n):
        if wood[j] >= req_vol:
            if bestIndex == -1:
                bestIndex = j
            elif wood[j] < wood[bestIndex]:
                bestIndex = j
    if bestIndex != -1:
        wood[bestIndex] -= req_vol
        count += 1
    else:
        break
    
if i == m:
    for j in range(len(wood)):
        if wood[j] != x[j]*y[j]*z[j]:
            wastage += wood[j]
            print("Wastage for wood piece number ", j+1, ":", wood[j], 'm^3')
    print('Total wastage in making', m, 'boxes is' , 'm^3')   
else:
    print('Some boxes could not found best fit from available wood pieces.')
    print(count, "boxes could be formed using single wood pieces. Now combining the rest over material")
    available_vol = 0
    new_count = 0
    for j in range(n):
        available_vol += wood[j]
    # New boxes can be made from extra wood to minimize wastage
    while requiredVol[i] <= available_vol:
        available_vol -= requiredVol[i]
        new_count += 1

    if i == m:
        print('All the boxes could be formed with a total wastage of ', available_vol)
    else:
        print('Only', new_count, ' more boxes could be made')
        print('Total Wastage : ', available_vol)

        if new_count < m:
            print('No. of boxes left : ', m - (count + new_count))
        else:
            print('No. of boxes made :', new_count)
