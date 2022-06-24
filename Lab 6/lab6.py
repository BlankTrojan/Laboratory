import tkinter as tk

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="push button")
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="push any button")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="push button")
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()