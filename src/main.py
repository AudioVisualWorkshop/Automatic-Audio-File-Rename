# Main Tkinter GUI application

import tkinter as tk
from gui import MainWindow


#Initialize TKinter
def main():
    root = tk.Tk() #gui.py uses this as a parameter
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
# root.title("Audio File Renamer") # defined in gui.py

#Makes root window expand
# root.columnconfigure(0, weight=1)
# root.rowconfigure(3, weight=1)

# frame = ttk.Frame(root, padding = 10)
# frame.grid(row=3, column=0, sticky="nsew")

# #Makes Frame expand when window expands
# frame.columnconfigure(0, weight=1)
# frame.columnconfigure(1, weight=1)
# frame.columnconfigure(2, weight=1)
# frame.columnconfigure(3, weight=1)
# frame.rowconfigure(3, weight=1)



# root.mainloop()
