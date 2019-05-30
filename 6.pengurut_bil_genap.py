number=int(input("masukan angka...."))  #masukan input angka yang diinginkan
number=number+1                         #agar range nya sesuai dengan input angka
for x in range(0,number):               #untuk x di range 0 sampai dengan var number
    if (x==1):                          #jika x=1
        continue                        #lewati list
    cekBil=x                            #variable cekBil=x
    while(cekBil>1):                    #saat cekBil>1
        cekBil=cekBil/2                 #cekbil dibagi 2
    if(cekBil==1):                      #jika cekbil =1
        print (x, "adalah bilangan genap")          #print x dan adalah bilangan genap
    else:                                           #selain itu
        continue                                    #lewati

'''
We didn't lose. we learn
''' 