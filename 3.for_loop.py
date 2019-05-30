#normal for loop
world = ["one", "two", "three", "four", "five"]     #variabel for berisikan string dari one to five
for eachNumber in world:         #untuk setiap string di variable world
    print(eachNumber)           #print setiap string
    

print("*************************")

#for loop per huruf
for eachAlphabet in "ayaka":        #untuk setiap alphabet di string ayaka
    print(eachAlphabet)             #print setiap alphabet di string ayaka
    
print("*************************")

#for loop break
feeling = ["sorry :)", "but i wont give up", "on you", "im tired"] #list string yang terdapat di variabel feeling
for eachVoice in feeling:       #untuk setiap sting di variabel feeling
    if eachVoice == "im tired":     #jika di setiap string terdapat kata "im tired"
        break       #hentikan program
    print(eachVoice)        #print setiap string dalam variable feeling
    
print("*************************")

#for loop continue 
hardWork = ["effort", "lazy", "fight", "study", "dont give up", "useless"]  #list dalam variabel hardwork
for eachWord in hardWork:       #untuk setiap string pada variabel hardwork
    if eachWord == "lazy" or eachWord == "useless":     #jika di setiap string terdapat kata "lazy" atau "useless"
        continue        #lewati
    print(eachWord)     #print eachWord
print("*************************")

#for loop dengan range
y = int (input())       #untuk menginput nilai integer yang diinginkan
for number in range(1,y):       #untuk setiap angka di range antara 1 sampai dengan input y
    print (number)          #print angka dalam number