from tkinter import *
from tkinter import messagebox
import pygame 
root = Tk()
root.title("TIC-TOC-TOE")
root.iconbitmap("unnamed.ico")


def disabe_game():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def stop ():
    pygame.mixer.music.stop()    
        



def checkifwins():
    global checkifwins
    wins = True

    if b1["text"] == "X" and b2["text"] == "X"  and  b3["text"] == "X" :
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION X WINS.......")
        wins = False
        disabe_game()
        stop()
        
    elif  b4["text"] == "X" and b5["text"] == "X"  and  b6["text"] == "X" :
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION X WINS.......")
        wins = False
        disabe_game()
        stop()
    elif  b7["text"] == "X" and b8["text"] == "X"  and  b9["text"] == "X" :
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION X WINS.......")
        wins = False
        disabe_game()
        stop()
    elif  b1["text"] == "X" and  b4["text"] == "X"  and  b7["text"] == "X" :
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION X WINS.......")
        wins = False
        disabe_game()
        stop()
    
        

    elif  b2["text"] == "X" and b5["text"] == "X"  and  b8["text"] == "X" :
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION X WINS.......")
        wins = False
        disabe_game()
        stop()       
    elif  b3["text"] == "X" and b6["text"] == "X"  and  b9["text"] == "X" :
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION X WINS.......")
        wins = False
        disabe_game()
        stop()
    elif  b1["text"] == "X" and b5["text"] == "X"  and  b9["text"] == "X" :
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION X WINS.......")
        wins = False
        disabe_game()
        stop()
    elif  b3["text"] == "X" and b5["text"] == "X"  and  b7["text"] == "X" :
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION X WINS.......")
        wins = False
        disabe_game()
        stop()




    if b1["text"] == "O" and b2["text"] == "O"  and  b3["text"] == "O" :
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION O WINS.......")
        wins = False
        disabe_game()
        stop()
        
    
    elif b4["text"] == "O" and b5["text"] == "O"  and  b6["text"] == "O" :
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION O  WINS.......")
        wins = False
        disabe_game()
        stop()

    elif b7["text"] == "O" and b8["text"] == "O"  and  b9["text"] == "O" :
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION O  WINS.......")
        wins = False
        disabe_game()
        stop()
    

    elif b1["text"] == "O" and b4["text"] == "O"  and  b7["text"] == "O" :
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION O  WINS.......")
        wins = False
        disabe_game()
        stop()
    
    elif b2["text"] == "O" and b5["text"] == "O"  and  b8["text"] == "O" :
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION O  WINS.......")
        wins = False
        disabe_game()
        stop()
    
    elif b3["text"] == "O" and b6["text"] == "O"  and  b9["text"] == "O" :
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION O  WINS.......")
        wins = False
        disabe_game()
        stop()

    elif b1["text"] == "O" and b5["text"] == "O"  and  b9["text"] == "O" :
        b1.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION O  WINS.....")
        wins = False
        disabe_game()
        stop()





    elif b3["text"] == "O" and b5["text"] == "O"  and  b7["text"] == "O" :
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        messagebox.showinfo("TIC TAC TOE", "YES \n CONGRAGULATION O  WINS.......")
        wins = False
        disabe_game()
        stop()




def play():
    pygame.mixer.init()
    pygame.mixer.music.load("Billie_Eilish_No_Time_To_Die_320.mp3")
    pygame.mixer.music.play()

    
    




click = True
cont = 0

def b_click(b):
    global click , cont

    if b["text"] == " " and click == True:
        b["text"] = "X" 
        click = False
        cont += 1
        checkifwins()


    elif b["text"]== " " and click == False:
        b["text"] = "O" 
        click = True
        cont +=1
        checkifwins()
    else:
        messagebox.showerror("TIC TAC TOE", "hey , what are you doing...... ?\n selet another box......")


def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9 , click , cont
    click = True
    cont = 0
    pygame.mixer.init()
    pygame.mixer.music.load("Billie_Eilish_No_Time_To_Die_320.mp3")
    pygame.mixer.music.play()


    

    b1 = Button(root , text=" " , font=("TAHOMA", 20) , bg="SystemButtonFace" , height=3 , width=6 ,command= lambda: b_click(b1))
    b2 = Button(root , text=" " , font=("TAHOMA", 20) , bg="SystemButtonFace" , height=3 , width=6 ,command= lambda: b_click(b2))
    b3 = Button(root , text=" " , font=("TAHOMA", 20) , bg="SystemButtonFace" , height=3 , width=6 ,command= lambda: b_click(b3))

    b4 = Button(root , text=" " , font=("TAHOMA", 20) , bg="SystemButtonFace" , height=3 , width=6 ,command= lambda: b_click(b4))
    b5 = Button(root , text=" " , font=("TAHOMA", 20) , bg="SystemButtonFace" , height=3 , width=6 ,command= lambda: b_click(b5))
    b6 = Button(root , text=" " , font=("TAHOMA", 20) , bg="SystemButtonFace" , height=3 , width=6 ,command= lambda: b_click(b6))

    b7 = Button(root , text=" " , font=("TAHOMA", 20) , bg="SystemButtonFace" , height=3 , width=6 ,command= lambda: b_click(b7))
    b8 = Button(root , text=" " , font=("TAHOMA", 20) , bg="SystemButtonFace" , height=3 , width=6 ,command= lambda: b_click(b8))
    b9 = Button(root , text=" " , font=("TAHOMA", 20) , bg="SystemButtonFace" , height=3 , width=6 ,command= lambda: b_click(b9))

    b1.grid(column=0, row=0)
    b2.grid(column=0, row=1)
    b3.grid(column=0, row=2)

    b4.grid(column=1, row=0)
    b5.grid(column=1, row=1)
    b6.grid(column=1, row=2)

    b7.grid(column=2, row=0)
    b8.grid(column=2, row=1)
    b9.grid(column=2, row=2)


my_menu = Menu(root)
root.config(menu= my_menu)
option_menu = Menu(my_menu)
my_menu.add_cascade(label="Option", menu= option_menu)
option_menu.add_command(label="Reset Game", command=reset)
reset()
play()













mainloop()