x = [-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y = [-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
run = True
count = 0
while run:
    for i in x:
        for j in y:
            if 0 < x[i]**2 - y[j]**3 < 11:
                print(f"({x[i]} , {y[j]})")
                count+=1
    print(count)
    run = False