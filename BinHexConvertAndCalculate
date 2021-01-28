# -*- coding: utf-8 -*-
"""
Binary-Hexedecimal convertor and calculator

Created on Fri Jan 29 02:18:41 2021

@author:Ahmet Kar
"""
from time import sleep

def doOperation(num1,num2):
    op= input("Enter a operand(+,-,and,or,xor) : ")
    result = 0
    if(op=="+"):    
        result = num1+num2
        print("addition result :")
    elif(op=="-"):
        result = num1-num2
        print("subtraction result : ")
    elif(op=="and"):
       result = num1 and num2
       print("and result  : ")
    elif(op=="or"):
      result = num1 or num2
      print("or result : ")
    elif(op=="xor"):
      result = num1 ^ num2
      print("xor result : ")
    return [result,op]
  
def Splitandwritebinary(bin_number):
    #print(bin_sayi[0:4]," ",bin_sayi[4:8]," ",bin_sayi[8:12],bin_sayi[12:])
    binlength = len(bin_number)
    # 16/4 12/4 8/4 4/4,1/4 5/4 9/4 13/4,14/4 10/4 6/4,11/4 7/4 3/4
    first_idx = binlength%4
    if(first_idx!=0):
      print(bin_number[0:first_idx],end=' ')     
    for i in range(first_idx,int(binlength/4)+first_idx):
        if(i==first_idx):
          print(bin_number[first_idx:4+first_idx],end=' ')
        else:
          new_first_idx= first_idx+4*(i-first_idx)
          print(bin_number[new_first_idx:new_first_idx+4],end=' ')
          #first_idx=2 i=3 6+4  f_i=2 i=4 10+4 f_i=2 i=5 14+4
          #first_idx=1 i=2 5+4  f_i=1 i=3 9+4 f_i=1 i=4 13+4
          #first_idx=3 i=4 7+4  f_i=3 i=5 11+4 f_i=3 i=6 15+4
          #2-4 ok,but -> 4-4-4 -> 6-10 10-14 14-18
     
    
while(True):
  a = input("1-(hex-bin) 2-(bin-hex), choose one :")
  if(a=='q'):
    print('bitti')
    sleep(2)	
    break
  if(a=="2"):
    n1 = input('Enter 1.binary number :') 
    n1 = n1.replace(" ","")
    n2 = input('Enter 2.binary number :')
    n2 = n2.replace(" ","")
    
    n1 = int(n1,2)
    n2 = int(n2,2)
    
    execute = doOperation(n1,n2)
    result = execute[0]  
    if(execute[1] in ['+','-']):
       print("decimal : ",n1," , ",n2," and result : ",result)    
    print("hexedecimal : ",hex(n1)," , ",hex(n2)," and result : ",hex(result))
    bin_result = str(bin(result)).replace("0b","")
    print("binary result :",end='')
    Splitandwritebinary(bin_result)
    
  elif(a=="1"): 
    n1 = input('Enter 1.hex number :').strip()  
    n1 = n1.replace(" ","")
    n2 = input('Enter 2.hex number :').strip()
    n2 = n2.replace(" ","")
    
    n1 = int(n1,16)
    n2 = int(n2,16)
    execute = doOperation(n1,n2)
    result = execute[0]
    
    if(execute[1] in ['+','-']):
      print("decimal : ",n1,",",n2," and result : ",result)
     
    bin1= str(bin(n1)).replace("0b","")
    bin2= str(bin(n2)).replace("0b","")
    bin_res = str(bin(result)).replace("0b","")
    print("binary :",end='')
    Splitandwritebinary(bin1)
    print(execute[1],end='')
    Splitandwritebinary(bin2)
    print('\n')
    print("binary result :",end='')
    Splitandwritebinary(bin_res)
    print('\n')
    print("hex result : ",hex(result))  
    
    
