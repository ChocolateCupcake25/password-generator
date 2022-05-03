# -*- coding: utf-8 -*-
"""
Created on Sun May  1 09:24:43 2022

@author: Ziyah Virani
"""
from tkinter import*
import random
root=Tk()
root.title("array 3d")
root.geometry("400x400")

label=Label(root)
enter_password=Entry(root)
label_guess=Label(root,text="guessed password:  ")

array_3d = [[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
             ["heads","tail","king","queen","princess","cupcake","gamer"],
             ["A","B","C","D","E","F","G","H","I","J","k","l","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
             ["!","@","#","$","%",'^',"&","*","(",")","-","_","+","=","{","}","[","]","|"]
             ]]
print(array_3d)

def newPassword():
    guessed_password=enter_password.get()
    label_guess["text"]="Guessed Password=  " + guessed_password
    
    random_1= random.randint(0,19)
    random_2= random.randint(0,6)
    random_3= random.randint(0,25)
    random_4= random.randint(0,18)
    
    
    letter1=str(array_3d[0][0][random_1])
    letter2=str(array_3d[0][1][random_2])
    letter3=str(array_3d[0][2][random_3])
    letter4=str(array_3d[0][3][random_4])
    label["text"]=letter1 + letter2 + letter3 + letter4
    
btn=Button(root, text="New Password", command=newPassword)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)
label_guess.place(relx=0.5,rely=0.4,anchor=CENTER)
enter_password.place(relx=0.5,rely=0.3,anchor=CENTER)

root.mainloop() 