from tkinter import *
from random import randint
from tkinter import ttk

#main window
root = Tk()
root.title("Rock,Paper,Scissors")
root.geometry("500x450")
root.iconbitmap('C:/Users/Sujith/Documents/Rock,paper,scissors/game_icon.ico')
root.resizable(False,False)

#bgimage
bgimage = PhotoImage(file = 'C:/Users/Sujith/Documents/Rock,paper,scissors/bg.png')
photolabel = Label(root,image= bgimage)
photolabel.place(relx = 0,rely = 0,relheight = 1,relwidth = 1)

#images for rps
Rock = PhotoImage(file = 'C:/Users/Sujith/Documents/Rock,paper,scissors/rock.png')
Paper = PhotoImage(file = 'C:/Users/Sujith/Documents/Rock,paper,scissors/paper.png')
Scissors = PhotoImage(file = 'C:/Users/Sujith/Documents/Rock,paper,scissors/scissors.png')
photo_list = [Rock , Paper , Scissors]
pick_no = randint(0,2)
label = Label(root, image = photo_list[pick_no],bd = 0)
label.pack(pady = 5)

#SPIN

def spin():
    pick_no = randint(0,2)
    label.config(image = photo_list[pick_no])

    if user_choice.get() == 'Rock': 
        user_choice_value = 0
    elif user_choice.get() == 'Paper':
        user_choice_value = 1
    if user_choice.get() == 'Scissors':
        user_choice_value = 2

#WIN OR LOSE
        
    if user_choice_value == 0:#Rock  [Rock,paper,scissors]
        if pick_no == 0:
            win_lose_label.config(text = 'It is a Tie! Spin again...')
        if pick_no == 1:
            win_lose_label.config(text = 'Paper Cover Rock.. YOU LOSE!')
        if pick_no == 2:
            win_lose_label.config(text = 'Rock smashes Scissors!.. YOU WIN!!!')

    if user_choice_value == 1:#Paper
        if pick_no == 0:
            win_lose_label.config(text = 'Paper cover Rock .. YOU WIN!!!')
        if pick_no == 1:
            win_lose_label.config(text = 'It is a Tie! Spin again...')
        if pick_no == 2:
            win_lose_label.config(text = 'Scissors cuts Paper .. YOU LOSE!')

    if user_choice_value == 2:#Scissors
        if pick_no == 0:
            win_lose_label.config(text = 'Rock smashes Scissors.. YOU LOSE!')
        if pick_no == 1:
            win_lose_label.config(text = 'Scissors cuts Paper .. YOU WIN!!!')
        if pick_no == 2:
            win_lose_label.config(text = 'It is a Tie! Spin again...')
            
#COMBOBOX
            
user_choice = ttk.Combobox(root,value = ('Rock','Paper','Scissors'))
user_choice.current(0)
user_choice.pack(pady = 5)

#SPINBUTTON
    
spin_button = Button(root,text = 'Spin!',bg = '#80aaff',fg = '#001133',padx = 10,command = spin) 
spin_button.pack()

#WIN/LOSE

win_lose_label = Label(root,text = '',font =('Helvetica',18))
win_lose_label.pack(pady = 50)






root.mainloop()
