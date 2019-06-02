n = int(input("masukan tinggi pyramid....."))       #memasukan input n sebagai tinggi pyramid
n=n+2                   #n=n+2 atau n+2
for x in range(1, n):       #untuk x di range 1 sampai dengan n
    b=x                     #b=n
    while(b>1):                 #selama b>1
        print("*", end=" ")         #print * dan spasi di line yang sama
        b=b-1                       #b=b-1 atau b-1
    print()                         #pindah ke line baru
    