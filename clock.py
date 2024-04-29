import tkinter as tk
from time import strftime

def light_theme(): #Dif light 
    frame = tk.Frame(main)
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)  #frame set with property

    lab_light = tk.Label(frame, font=('Browallia New',50,'bold'), foreground='#00FFFF')
    lab_light.pack(anchor="s")

    def time():
        string = strftime('%I:%M:%S %p')
        lab_light.config(text=string)
        lab_light.after(1000, time)
    time()

def drak_theme(): #Dif dark
    frame = tk.Frame(main)
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)  #frame set with property

    lab_light = tk.Label(frame, font=('Browallia New',50,'bold'), background='#000000', foreground='#00FFFF')
    lab_light.pack(anchor="s")

    def time():
        string = strftime('%I:%M:%S %p')
        lab_light.config(text=string)
        lab_light.after(1000, time)
    time()




main = tk.Tk()
main.title("Clock By Helix")
canvas = tk.Canvas(main, height=100, width=500) #property
canvas.pack()

frame = tk.Frame(main,)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8) #frame set with property

lab_light = tk.Label(frame, font=('Browallia New',50,'bold'),foreground='#00FFFF')
lab_light.pack(anchor="s")

def time():
    st = strftime('%I:%M:%S %p')
    lab_light.config(text=st)
    lab_light.after(1000, time)

time()

menu = tk.Menu(main)
theme_menu = tk.Menu(menu, tearoff=0)
theme_menu.add_command(label="Light", command=light_theme) 
theme_menu.add_command(label="Dark", command=drak_theme) 
menu.add_cascade(label="Mode", menu=theme_menu)
main.config(menu=menu)

main.mainloop()
