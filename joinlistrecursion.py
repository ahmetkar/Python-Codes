# -*- coding: utf-8 -*-

"""
@Author: Ahmet Kar
Recursion fonksiyonlardan faydalanılarak içiçe listeleri birleştirme

Combining nested lists using Recursion functions
"""


# Öncelikle recursion fonksiyon kullandığımızda sorun çıkmaması için global bir bir birleşim değişkeni kullanmalıyız.
# First of all, we should use a global union variable to avoid problems when we use a recursion function.

birlesim = ""

def birlestir(liste): 
    global birlesim
    for i in liste:
        if isinstance(i,list): # her elemanının liste olup olmadığını kontrol ediyoruz #we check if every element is in list
            return birlestir(i) # listeyse fonksiyona tekrar gönderiyoruz # If it is the list, we send it to the function
        else:
            birlesim=birlesim+i+" " # artık liste değilse birlesim adlı biriktiricimize ekliyoruz.#If it is no longer the list, we add it to our spooler named 'birlesim'.
    return birlesim

liste = ["ahmet","mehmet",["ali","hasan",["can",["cenk"]]],"salih"] 

print(birlestir(liste))
