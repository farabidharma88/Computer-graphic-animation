from tkinter import *
from PIL import ImageTk,Image
import time

root = Tk()
root.title("Farabi Dharma Rizqi Utama")
root.geometry("1200x500")

canvas = Canvas(root, width = 1200, height = 500)  
canvas.pack()

background = Image.open("bgrd/roboto.png")
background = background.resize((1200, 500), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(background)


while (True):
    for i in range(41):
        canvas.delete("all")
        canvas.create_image(0, 0, anchor=NW, image=bg)

        if(0<=i<15):
            #jalan
            num = i
            img = Image.open("skeleton/skeleton_walk_" + str(num%13) + ".png")
            img = img.resize((100,100), Image.ANTIALIAS)
            x = 70+50*num
            y = 400
        elif(15<=i<28):
            # mukul
            num = i-15
            img = Image.open("skeleton/skeleton_attack_" + str(num) + ".png")
            img = img.resize((200,100), Image.ANTIALIAS)
            x = 820+20*num
            y = 400
        elif(28<=i<42):
            # mati
            num = i-28
            img = Image.open("skeleton/skeleton_die_" + str(num) + ".png")
            img = img.resize((100,100), Image.ANTIALIAS)
            x = 1000
            y = 400
        skeleton = ImageTk.PhotoImage(img)
        canvas.create_image(x, y, anchor=CENTER, image=skeleton)
        
        x = 1020
        y = 410

        if(0<=i<28):
            img = Image.open("mushroom/mushroom_1.png")
            img = img.resize((300,300), Image.ANTIALIAS)
        if(28<=i<30):
            img = Image.open("mushroom/mushroom_2.png")   
            img = img.resize((300,300), Image.ANTIALIAS)
        else:
            img = Image.open("mushroom/mushroom_3.png")
            img = img.resize((300,300), Image.ANTIALIAS)

        mushroom = ImageTk.PhotoImage(img)
        canvas.create_image(x, y, anchor=CENTER, image=mushroom)

        canvas.update()
        time.sleep(0.1)

root.mainloop()