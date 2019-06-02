n = int(input("masukan tinggi pyramid....."))   #input untuk menentukan tinggi pyramid
n=n+1               #input ditambah 1
while(n>1):         #selama input > 1
    b=n             #var b = input n
    while(b>1):     #selama var b>1
        print("*",end=" ")          #print * dan spasi disatu line
        b=b-1                       #b=b-1 atau var b - 1
    print()                         #pindah line baru
    n=n-1                           #n=n-1 atau n-1