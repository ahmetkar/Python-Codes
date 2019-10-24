def bytetoNum():
 x = int(input("Bir byte kodu girin")) 
 y = [int(y) for y in str(x)]

 a =0
 toplam =0
 k =0
 while a<len(y):
    if(y[a]==1):
      toplam+=2**k
      k+=1
      a+=1
    elif(y[a]==0):
       a+=1
       continue     
   
    
 print(toplam)

def numtoByte():
 x = int(input("Bir sayi giriniz"))
 dizi =[]
 while x!=0 and type(x)==int:
   dizi.append(x%2)
   x = int(x/2)
 for i in dizi:
  print(i)
  
sec = input("Byte i integer a cevirmek icin 1 e Integeri byte a cevirmek icin 2 e basin")

if(int(sec)==1):
   bytetoNum()
elif(int(sec)==2):
   numtoByte()
else:
   print("Yanlis girdi")

