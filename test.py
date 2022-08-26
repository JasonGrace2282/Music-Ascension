import pygame, sys
import tkinter as tk
from tkinter import ttk


def copy2clipboard(self):
    variable = tk.Tk()
    variable.withdraw()
    variable.clipboard_clear()
    variable.clipboard_append('https://docs.google.com/document/d/1THAizjwlYdVoINJjOBudmcoIM79gEhlbue3cjW5E7r0/edit?usp=sharing')
    variable.update()
    variable.destroy()
    print("Copied to clipboard")



# root window
root = pygame.display.set_mode(300, 200)
root.geometry('300x200') #Window size
root.resizable(False, False)
root.title('Button Demo')

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()