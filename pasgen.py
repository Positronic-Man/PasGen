from tkinter import *
import random

MF = Tk() #Main Field
MF.title('Password generator')
MF.resizable(0, 0)
WIDTH = 520 #MF.winfo_screenwidth()
HEIGHT = 720 #MF.winfo_screenheight()
canvas = Canvas(MF, width=WIDTH, height=HEIGHT, highlightthickness=0, bg='linen')
canvas.focus_set()

for i in range (0,2000,30):
    canvas.create_line(0, i, WIDTH, i, fill='skyblue', width=2)
    canvas.create_line(i, 0, i, HEIGHT, fill='skyblue', width=2)
# Title
canvas.create_text(WIDTH//2, 25, text="PASSWORD GENERATOR", fill="midnightblue", font = "Times 24 italic bold")
# configuration
canvas.create_text(WIDTH//2, 55, text='password length', fill='midnightblue', font="Arial 11")
canvas.create_line(40, 85, WIDTH-40, 85, fill="midnightblue", width=5)
lenght = ["6","8","10","12","14","16","18","20"]
for i in range(len(lenght)):
    d = 40
    e = 60
    shift = i*60
    canvas.create_oval(d+shift, 75, e+shift, 95, outline="midnightblue", fill="linen", width=5)
    canvas.create_text(d+shift+10, 110, text=lenght[i], fill="midnightblue", font="Arial 11 bold")
mv = 0
select = canvas.create_oval(42+mv, 77, 58+mv, 93, outline="linen", fill="midnightblue", width=2)
list_of_types = ['majuscules','minuscules','numbers','symbols']
# check boxes
n = 0
for i in range(2):
    shift = 210*i
    for j in range(2):
        shift2 = 60*j
        canvas.create_line(69+shift, 130+shift2, 101+shift, 130+shift2, fill='midnightblue', width=3)
        canvas.create_line(100+shift, 129+shift2, 100+shift, 161+shift2, fill='midnightblue', width=3)
        canvas.create_line(101+shift, 160+shift2, 69+shift, 160+shift2, fill='midnightblue', width=3)
        canvas.create_line(70+shift, 161+shift2, 70+shift, 129+shift2, fill='midnightblue', width=3)
        canvas.create_text(130+shift, 144+shift2, text=list_of_types[n], anchor=W, fill="midnightblue", font="Arial 12 bold")
        n += 1
Maj = canvas.create_text(75, 128, text='X', anchor=NW, fill='midnightblue', font='Arial 24')
maj_X = 1
Min = canvas.create_text(75, 188, text='X', anchor=NW, fill='midnightblue', font='Arial 24')
min_X = 1
Num = canvas.create_text(285, 128, text='X', anchor=NW, fill='midnightblue', font='Arial 24')
num_X = 1
Sym = canvas.create_text(285, 188, text='X', anchor=NW, fill='midnightblue', font='Arial 24')
sym_X = 1

canvas.create_line(WIDTH//2-100, 250, WIDTH//2+100, 250, fill='midnightblue', width=5)
canvas.create_line(WIDTH//2+100, 248, WIDTH//2+100, 312, fill='midnightblue', width=5)
canvas.create_line(WIDTH//2-100, 310, WIDTH//2+100, 310, fill='midnightblue', width=5)
canvas.create_line(WIDTH//2-100, 312, WIDTH//2-100, 248, fill='midnightblue', width=5)
canvas.create_text(WIDTH//2, 280, text='GENERATE', fill='midnightblue', font="Arial 18 bold")
canvas.create_line(WIDTH//2-100, HEIGHT-70, WIDTH//2+100, HEIGHT-70, fill='midnightblue', width=5)
canvas.create_line(WIDTH//2+100, HEIGHT-72, WIDTH//2+100, HEIGHT-18, fill='midnightblue', width=5)
canvas.create_line(WIDTH//2-100, HEIGHT-20, WIDTH//2+100, HEIGHT-20, fill='midnightblue', width=5)
canvas.create_line(WIDTH//2-100, HEIGHT-18, WIDTH//2-100, HEIGHT-72, fill='midnightblue', width=5)
canvas.create_text(WIDTH//2, HEIGHT-45, text='Copy to clipboard', fill='midnightblue', font="Arial 14 bold")
canvas.create_line(WIDTH-100, HEIGHT-70, WIDTH-50, HEIGHT-70, fill='midnightblue', width=5)
canvas.create_line(WIDTH-50, HEIGHT-72, WIDTH-50, HEIGHT-18, fill='midnightblue', width=5)
canvas.create_line(WIDTH-50, HEIGHT-20, WIDTH-100, HEIGHT-20, fill='midnightblue', width=5)
canvas.create_line(WIDTH-100, HEIGHT-18, WIDTH-100, HEIGHT-72, fill='midnightblue', width=5)
canvas.create_text(WIDTH-75, HEIGHT-45, text='Quit', fill='midnightblue', font="Arial 12 bold")
canvas.pack()

list_of_symbols = {'majuscules':'ABCDEFGHIJKLMNOPQRSTUVWXYZ','minuscules':'abcdefghijklmnopqrstuvwxyz','numbers':'1234567890','symbols':'@#€_&-+()/*:;!?$=~[]{}\°%,.'}
list_output, check, text_field, pass_selection = [],[],[],[]
select2 = ''
password_lenght = 6

def click(event):
    global maj_X, min_X, num_X, sym_X, list_output, text_field, select2, limit, selected
    pos = canvas.coords(select)
    x = int(pos[0])
    if event.y < 120:
        if x <= event.x and x < WIDTH-60: mv = 60
        elif x >= event.x and x > 60: mv = -60
        else: mv = 0
        canvas.move(select, mv, 0)
    else:
        if event.x < WIDTH//2 and event.y < 190:
            if maj_X == 1:
                canvas.itemconfig(Maj, text='')
                maj_X = 0
            else:
                canvas.insert(Maj, 12, 'X')
                maj_X = 1
        elif event.x < WIDTH//2 and event.y > 130 and event.y < 250:
            if min_X == 1:
                canvas.itemconfig(Min, text='')
                min_X = 0
            else:
                canvas.insert(Min, 12, 'X')
                min_X = 1
        elif event.x > WIDTH//2 and event.y < 190:
            if num_X == 1:
                canvas.itemconfig(Num, text='')
                num_X = 0
            else:
                canvas.insert(Num, 12, 'X')
                num_X = 1
        elif event.x > WIDTH//2 and event.y > 130 and event.y < 250:
            if sym_X == 1:
                canvas.itemconfig(Sym, text='')
                sym_X = 0
            else:
                canvas.insert(Sym, 12, 'X')
                sym_X = 1
        elif event.y > 250 and event.y < 310 and event.x > WIDTH//2-100 and event.x < WIDTH//2+100:
            if list_output: clear_text_field()
            verify()
            generate()
            result()
            selection()
        elif select2 and event.y > 310 and event.y < HEIGHT-70:
            pos2 = canvas.coords(select2)
            Y = int(pos2[1])
            if event.y > Y and event.y <= int(limit[1]): mv2 = 30
            elif event.y < Y and event.y > 310: mv2 = -30
            else: mv2 = 0
            canvas.move(select2, 0, mv2)
        elif select2 and event.y > HEIGHT-70 and event.x < WIDTH-100:
            MF.clipboard_clear()
            pos2 = canvas.coords(select2)
            Y = int(pos2[1])
            for i in range (len(list_output)):
                my = 30*i
                if Y == int(start[1])+my+2:
                    MF.clipboard_append(list_output[i])
                    MF.update()
        elif event.y > HEIGHT-70 and event.x > WIDTH-100: MF.destroy()

def generate():
    global check, password_lenght, lenght, list_output
    for j in range (10):
        output,sym = '',""
        while len(output) < password_lenght:
            sym = random.choice(list_of_symbols.get(random.choice(check)))
            if sym not in output: output = output + sym
        list_output.append(output)

def verify():
    global check, password_lenght, lenght, maj_X, min_X, num_X, sym_X
    pos = canvas.coords(select)
    x = int(pos[0])
    for i in range (len(lenght)):
        mv = 60*i
        if x == 42+mv : password_lenght = int(lenght[i])
        if maj_X == 1: check.append(list_of_types[0])
        if min_X == 1: check.append(list_of_types[1])
        if num_X == 1: check.append(list_of_types[2])
        if sym_X == 1: check.append(list_of_types[3])
        if check == []: check = list_of_types

def result():
    global list_output, password_lenght, text_field, pass_selection
    i = 0
    for member in list_output:
        mv = 30*i
        text_field.append(canvas.create_text(WIDTH//2, 334+mv, text=member, fill='midnightblue', font="Courier 12 bold"))
        shift = password_lenght*8
        pass_selection.append(canvas.create_oval(WIDTH//2-16-shift, 324+mv, WIDTH//2+4-shift, 344+mv, outline="midnightblue", fill="linen", width=5))
        i += 1

def clear_text_field():
	global text_field, list_output, pass_selection
	for i in range(10):
		canvas.itemconfig(text_field[i], text='')
		canvas.delete(pass_selection[i])
	list_output.clear()
	text_field.clear()
	pass_selection.clear()
	canvas.delete(select2)
	check.clear()

def selection():
	global pass_selection, select2, limit, start
	start = canvas.coords(pass_selection[0])
	X,Y = int(start[0]),int(start[1])
	select2 = canvas.create_oval(X+2, Y+2, X+18, Y+18, outline="linen", fill="midnightblue", width=2)
	limit = canvas.coords(pass_selection[9])

canvas.bind('<1>', click)

MF.mainloop() 
