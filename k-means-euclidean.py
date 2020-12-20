import math

iteration = int(input("Enter How Many Data Table : "))
iteration = 6
pattern = []
# pattern = [['185', '72'], ['170', '56'], ['168', '60'], ['179', '68'], ['182', '72'], ['188', '77']]

i=1
while i<=iteration:
    temp = input(f'Enter Data Table {i} : ')
    convert_to_list = temp.split(',')
    pattern.append(convert_to_list)
    i+=1

print(f'\nInputed Data = {pattern}\n')

def euclidean(x,y,a,b):
    D = (x-a)**2+(y-b)**2
    D = (math.sqrt(D))
    r = round(D,2)
    return r

def manhattan(x,y,a,b):
    D = abs(x-a)+abs(y-b)
    r = round(D,2)
    return r

def smallest(s_list):
    small = s_list[0]
    for s in s_list:
        if s < small:
            small = s
    return s_list.index(small)        




initial=[]
final_assignment = []

k = int(input("Enter Value of K : "))
type = input("Enter auto/manual : ")

a = 0
booked = []
if type == 'a':
    while a<k:
        initial.append(pattern[a])
        booked.append(a)
        a+=1
else:
    t = input('Enter TIDS: ').split(',')
    for i in t:
        initial.append(pattern[int(i)-1])
        booked.append(int(i)-1)

print(booked)
print(f'\nInitial Centroid = {initial}\n')

print('-----------INITIAL STEP---------')
b=1
c=1
updated_centeroid = []
temp_list = []
for i in initial:
    print(f'-------Cluser{c}-------')
    for j in initial:
        n = euclidean(int(i[0]),int(i[1]),int(j[0]),int(j[1]))
        temp_list.append(n)
        print(f'Disrance from clusrer {b} ({j}) = √({j[0]}-{i[0]})^2 + ({j[1]}-{i[1]})^2 = {n}')
        b+=1
    sm = smallest(temp_list)
    assignment = sm+1
    temp_list.append(assignment)
    updated_centeroid.append(temp_list)
    temp_list = []
    temp_list.append(i[0])
    temp_list.append(i[1])
    temp_list.append(c)
    final_assignment.append(temp_list)
    temp_list = []
    b=1
    c+=1
print(f'Updated Cluster Centroid {updated_centeroid}')
print('-----------END INITIAL STEP---------')

b=1
c=1
updated_centeroid = []
temp_list = []

for i in pattern:
    if pattern.index(i) not in booked:
        print(f'\n----------Calculating distance form next dataset ({i})----------')
        for j in initial:
            n = euclidean(int(i[0]),int(i[1]),int(j[0]),int(j[1]))
            temp_list.append(n)
            print(f'Disrance from clusrer {b} ({j}) = √({i[0]}-{j[0]})^2 + ({i[1]}-{j[1]})^2 = {n}')
            b+=1
        
        sm = smallest(temp_list)
        assignment = sm+1
        temp_list.append(assignment)    
        updated_centeroid.append(temp_list)
        print(f'For dataset table : {temp_list}')
        select = initial[sm]
        update_x = (int(select[0]) + int(i[0]))/2
        update_y = (int(select[1]) + int(i[1]))/2
        print(f'({select[0]} + {i[0]})/2 = {update_x}')
        print(f'({select[1]} + {i[1]})/2 = {update_y}')
        initial[sm][0] = update_x
        initial[sm][1] = update_y
        print(f'Updated Cluster Centroid {initial}')
        temp_list = []
        temp_list.append(i[0])
        temp_list.append(i[1])
        temp_list.append(assignment)
        final_assignment.append(temp_list)
        temp_list = []
        b=1  

print('\n-------------Final Assignment---------------')
print(f'{final_assignment}')