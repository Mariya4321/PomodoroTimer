from tkinter import *
import pygame
import math

# ---------------------------- CONSTANTS(GLOBAL VARIABLE) ------------------------------- #
GREEN = "#9BCF53"
RED = "#C40C0C"
ORANGE = "#A73121"
BLUE = "#201658"
YELLOW = "#F2E8C6"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

pygame.mixer.init()
work_sound = "alert.mp3"
short_break_sound = "break.mp3"
long_break_sound = "Long_break.wav"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_count():
    global REPS
    REPS = 0
    window.after_cancel(str(timer))     # stop time
    canvas.itemconfig(timer_start, text="00:00")    # reset time
    Heading.config(text="Timer", fg=ORANGE, bg=YELLOW)      # Changing time
    Check.config(text="")       # remove check


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1
    if REPS % 2 != 0:       # if repetition == 2, 4 ,6 which is ShortBreak
        countdown(WORK_MIN * 60)
        Heading.config(text="Work Hard😃", fg=GREEN, bg=YELLOW)
        play_sound(work_sound)
    elif REPS % 8 == 0:     # if repetition == 8 or 16 and so on which is LongBreak
        countdown(LONG_BREAK_MIN * 60)
        Heading.config(text="Break😮‍💨", fg=BLUE, bg=YELLOW)
        play_sound(short_break_sound)
    else:                   # if repetition == 1, 3 ,5 which is WorkTime
        countdown(SHORT_BREAK_MIN * 60)
        Heading.config(text="Fresh Quickly😉", fg=RED, bg=YELLOW)
        play_sound(long_break_sound)


# ---------------------------- PLAYSOUND ------------------------------- #

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(loops=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)      # minute count
    count_sec = count % 60              # second count
    if count_sec < 10:              # to display 00, 09, 08 so on
        count_sec = f"{count_sec:02}"  # 02 stands for 2 digit and 0 before digit

    canvas.itemconfig(timer_start, text=f"{count_min}:{count_sec}")     # changing time
    if count > 0:       # to keep timer positive
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(REPS / 2)):   # counting repeats
            marks += "✔️"
        Check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato Timer")
window.config(padx=100, pady=50, bg=YELLOW)

Heading = Label(text="Timer", font=(FONT_NAME, 40, "italic"), fg=ORANGE, bg=YELLOW)
Heading.grid(column=1, row=0)

# IMAGE SETUP
canvas = Canvas(width=400, height=300, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(200, 150, image=tomato)
timer_start = canvas.create_text(200, 175, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

# START
start = Button(text="Start", font=(FONT_NAME, 15, "italic"), bd=1, fg=RED, bg=GREEN, command=start_timer)
start.grid(column=0, row=2)

# RESET
reset = Button(text="Reset", font=(FONT_NAME, 15, "italic"), bd=1, fg=RED, bg=GREEN, command=reset_count)
reset.grid(column=2, row=2)

# CHECK
Check = Label(fg=ORANGE, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
Check.grid(column=1, row=3)

window.mainloop()
