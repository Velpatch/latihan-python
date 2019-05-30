count = 1   #integer yang tersimpan dalam variable count
while (count<=8):       #selama count <= 8
    print(count)        #print count
    count+=1            #isi count ditambah 1

print("*****************")

count2 = 1      #integer yang tersimpan dalam variabel count2
while (count2<=8):          #selama count2 <=8
    print(count2)           #print count2
    if count2==4:           #jika count2 = 4
        print("break di no 4")      #print break di no 4
        break               #menghentikan loop
    count2 += 1             #isi count2 ditambah 1

print("*****************")

count3 = 0         #integer yang tersimpan dalam variabel count 3
while (count3<=10):     #selama count3 <=10
    count3+=1           #count3 + 1
    if count3==7:    #jika count3 = 7
        print("skip")   #print skip 
        continue        #lewati loop
    print(count3)       #print count 3

