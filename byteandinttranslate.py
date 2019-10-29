# Author : ahmetkar0

def bytetoNum():
 x = int(input("Bir byte kodu girin")) 
 #xe girilen sayinin rakamlarini kisa yolla döngüye alıp y ye aktar.
 y = [int(y) for y in str(x)] 

 #a sayac degişkeni k ussu surekli artirmak icin kullanilan sayac degişkeni
 #toplam 2 nin ussunu alip surekli depoladiğimiz değişken
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
  
sec = input("Byte i integer a cevirmek icin 1 e Integeri byte e cevirmek icin 2 e basin")

if(int(sec)==1):
   bytetoNum()
elif(int(sec)==2):
   numtoByte()
else:
   print("Yanlis girdi")

