#62055003ตั๊ก
w = [2, 10, 5 ,5]
v = [20, 50, 30, 10]
W = 16
picked = [0,0,0,0]
RemainingCapacity = W
currentValue = 0
currentWeight = 0
maxValue = 0


#for i in w:
#    print(i)
for i in range(len(w)) :
    print(w[i])
for j in range(len(v)):
    print(v[j])

for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):

                currentValue =0
                currentWeight = 0
              
                #if (i1 != i2) and (i1 != i3) and (i1 != i4) and (i2 != i3) and (i2 != i4) and (i3 != i4):
                if i1 == 1:
                    currentValue += v[0]
                    currentWeight += w[0]

                if i2 == 1:
                    currentValue += v[1]
                    currentWeight += w[1]
                if i3 == 1:
                    currentValue += v[2]
                    currentWeight += w[2]
                if i4 == 1:
                    currentValue += v[3]
                    currentWeight += w[3]

                if  currentValue > maxValue and currentWeight <= W:
                    maxValue = currentValue 
                    #print("bbb")
                    picked = [0,0,0,0]
                    if  i1 == 1:
                        picked[0] = 1
                    if  i2 == 1:
                        picked[1] = 1 
                    if  i3 == 1:
                        picked[2] = 1
                    if  i4 == 1:
                        picked[3] = 1
                        

                print(i1, " ", i2, " ", i3, " ", i4, " val = ", currentValue,"Weight =", currentWeight,"Max", maxValue)
                print("OverWeight",picked)
