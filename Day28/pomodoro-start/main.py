from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None




# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    Check_mark.config(text="")
    title_lable.config(text='Timer')
    global  reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    global reps
    global title_lable
    reps += 1

    WORK_MIN_sec = WORK_MIN * 60
    SHORT_BREAK_MIN_sec = SHORT_BREAK_MIN * 60
    LONG_BREAK_MIN_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN_sec)
        title_lable.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50))

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN_sec)
        title_lable.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))

    else:
        count_down(WORK_MIN_sec)
        title_lable.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count > 0:
        global  timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        worksession = math.floor(reps/2)
        marks = ""
        for _ in range(worksession):
            marks += "✔"
        Check_mark.config(text=f"{marks}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('pomodoro')

window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)


title_lable = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_lable.grid(column=1, row=0)
title_lable.config(padx=20, pady=20)

Check_mark = Label(text=" ", fg=GREEN, bg = YELLOW, font=(FONT_NAME, 15, 'bold'))
Check_mark.grid(column=1, row=3)
Check_mark.config(padx=20, pady=20)

Start_button = Button(text="Start",font=(FONT_NAME,15,'bold'),command=timer_start,highlightthickness=0)
Start_button.grid(column=0, row=2)
Start_button.config(padx=20,pady=20)

Reset_button = Button(text="Reset", font=(FONT_NAME, 15, 'bold'),command=reset_timer, highlightthickness=0)
Reset_button.grid(column=2, row=2)
Reset_button.config(padx=20, pady=20)

window.mainloop()
