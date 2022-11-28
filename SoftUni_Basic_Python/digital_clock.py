from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("digital_Clock")
app_window.geometry("450x140")


text_font = ('calibre', 60, 'bold')
background = "#4287f5"
foreground = "#42f5cb"
border_width = 40

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)

label.grid(row=0, column=1)


def digital_clock():
    time_live = time.strftime("%H:%M:%S %p")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()
app_window.mainloop()
