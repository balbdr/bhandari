from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def update_time():
    current_time = strftime("%I:%M:%S %p")  # Get current time
    clock_label.config(text=current_time)  # Update the label
    clock_label.after(1000, update_time)  # Update every 1 second

clock_label = Label(root, font=("calibri", 50, "bold"), bg="purple", fg="white")
clock_label.pack(anchor="center")

update_time()  # Start the clock
root.mainloop()
