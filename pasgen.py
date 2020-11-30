from tkinter import *
import random

MF = Tk() #Main Field
MF.title('Password generator')
MF.resizable(0, 0)
WIDTH = MF.winfo_screenwidth()
HEIGHT = MF.winfo_screenheight()
canvas = Canvas(MF, width=WIDTH, height=HEIGHT, highlightthickness=0, bg='linen')
canvas.focus_set()

for i in range (0,2000,50):
    canvas.create_line(0, 10+i, WIDTH, 10+i, fill='skyblue', width=2)
    canvas.create_line(10+i, 0, 10+i, HEIGHT, fill='skyblue', width=2)
# Title
canvas.create_text(WIDTH//2, 40, text="PASSWORD GENERATOR", fill="midnightblue", font = "Times 11 italic bold")
# configuration
canvas.create_text(WIDTH//2, 90, text='password length', fill='midnightblue', font="Arial 8")
canvas.create_line(40, 135, WIDTH-40, 135, fill="midnightblue", width=5)
lenght = ["6","8","10","12","14","16","18","20"]
for i in range(len(lenght)):
    d = 40
    e = 60
    shift = i*90
    canvas.create_oval(d+shift, 125, e+shift, 145, outline="midnightblue", fill="linen", width=5)
    canvas.create_text(d+shift+10, 165, text=lenght[i], fill="midnightblue", font="Arial 8")
mv = 0
select = canvas.create_oval(42+mv, 127, 58+mv, 143, outline="linen", fill="midnightblue", width=2)
list_of_types = ['majuscules','minuscules','numbers','symbols']
# check boxes
n = 0
for i in range(2):
    shift = 350*i
    for j in range(2):
        shift2 = 100*j
        canvas.create_line(60+shift, 210+shift2, 112+shift, 210+shift2, fill='midnightblue', width=5)
        canvas.create_line(110+shift, 210+shift2, 110+shift, 262+shift2, fill='midnightblue', width=5)
        canvas.create_line(110+shift, 260+shift2, 58+shift, 260+shift2, fill='midnightblue', width=5)
        canvas.create_line(60+shift, 260+shift2, 60+shift, 208+shift2, fill='midnightblue', width=5)
        canvas.create_text(130+shift, 232+shift2, text=list_of_types[n], anchor=W, fill="midnightblue", font="Arial 8")
    n += 1
Maj = canvas.create_text(70, 208, text='X', anchor=NW, fill='midnightblue', font='Arial 12')
maj_X = 1
Min = canvas.create_text(70, 308, text='X', anchor=NW, fill='midnightblue', font='Arial 12')
min_X = 1
Num = canvas.create_text(420, 208, text='X', anchor=NW, fill='midnightblue', font='Arial 12')
num_X = 1
Sym = canvas.create_text(420, 308, text='X', anchor=NW, fill='midnightblue', font='Arial 12')
sym_X = 1

canvas.create_line(WIDTH//2-150, 410, WIDTH//2+150, 410, fill='midnightblue', width=5)
canvas.create_line(WIDTH//2+150, 408, WIDTH//2+150, 510, fill='midnightblue', width=5)
canvas.create_line(WIDTH//2-150, 510, WIDTH//2+152, 510, fill='midnightblue', width=5)
canvas.create_line(WIDTH//2-150, 510, WIDTH//2-150, 408, fill='midnightblue', width=5)
canvas.create_text(WIDTH//2, 460, text='GENERATE', fill='midnightblue', font="Arial 8")
text_field = canvas.create_text(WIDTH//2, 0, text='', fill='midnightblue', font="Arial 8")

canvas.pack()

def click(event):
    global maj_X, min_X, num_X, sym_X
    pos = canvas.coords(select)
    x = int(pos[0])
    if event.y < 200:
        if x <= event.x and x < WIDTH-60: mv = 90
        elif x >= event.x and x > 60: mv = -90
        else: mv = 0
        canvas.move(select, mv, 0)
    else:
        if event.x < 300 and event.y < 250:
            if maj_X == 1:
                canvas.itemconfig(Maj, text='')
                maj_X = 0
            else:
                canvas.insert(Maj, 12, 'X')
                maj_X = 1
        elif event.x < 300 and event.y > 250 and event.y < 350:
            if min_X == 1:
                canvas.itemconfig(Min, text='')
                min_X = 0
            else:
                canvas.insert(Min, 12, 'X')
                min_X = 1
        elif event.x < 500 and event.y < 250:
            if num_X == 1:
                canvas.itemconfig(Num, text='')
                num_X = 0
            else:
                canvas.insert(Num, 12, 'X')
                num_X = 1
        elif event.x < 500 and event.y > 250 and event.y < 350:
            if sym_X == 1:
                canvas.itemconfig(Sym, text='')
                sym_X = 0
            else:
                canvas.insert(Sym, 12, 'X')
                sym_X = 1
        elif event.y > 400 and event.y < 520 and event.x > WIDTH//2-150 and event.x < WIDTH//2+150:
            canvas.delete(text_field)
            verify()
            generate()
            result()

list_of_symbols = {'majuscules':'ABCDEFGHIJKLMNOPQRSTUVWXYZ','minuscules':'abcdefghijklmnopqrstuvwxyz','numbers':'1234567890','symbols':'@#€_&-+()/*:;!?$=~[]{}\°%,.'}
list_output, check = [],[]
password_lenght = 6

def generate():
    global check, password_lenght, lenght
    for j in range (10):
        output = ''
        for i in range (password_lenght):
            output = output + ''.join(random.choice(list_of_symbols.get(random.choice(check))))
        list_output.append(output)

def verify():
    global check, password_lenght, lenght
    pos = canvas.coords(select)
    x = int(pos[0])
    for i in range (len(lenght)):
        mv = 90*i
        if x == 42+mv : password_lenght = int(lenght[i])
        if maj_X == 1: check.append(list_of_types[0])
        if min_X == 1: check.append(list_of_types[1])
        if num_X == 1: check.append(list_of_types[2])
        if sym_X == 1: check.append(list_of_types[3])
        if check == []: check = list_of_types

def result():
    global list_output
    i = 0
    for member in list_output:
        mv = 25*i
        text_field = canvas.create_text(WIDTH//2, 584+mv, text=member, fill='midnightblue', font="Arial 8")
        i += 1
        

canvas.bind('<1>', click)

MF.mainloop() 
