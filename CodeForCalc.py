from tkinter import *

root = Tk()
root.title("Standard Calculator")
root.configure(bg="#2c2f33")

StrVar = StringVar()
StrVar.set("")

btn_config = {
    "height":2,
    "width":6,
    "font": ("Arial", 14),
    "bg": "#7289da",
    "fg": "white",
    "activebackground": "#99aab5",
    "bd": 0
}

Label(root, textvariable=StrVar, height=2, bg="#23272a", fg="white",
      font=("Arial", 20), anchor="e").grid(row= 0 , column=0,columnspan=4, sticky="we", padx=10, pady=10)


def HandleClick(BtnVal):
    exp = StrVar.get()
    if BtnVal == "=":
        try:
            exp = str(eval(exp))
        except:
            exp = "Error"
    elif BtnVal == "C":
        exp = ""
    elif BtnVal in ["⌫", "back"]:
        exp = exp[:-1]
    else:
        exp += str(BtnVal)
    StrVar.set(exp)

buttons = [
    ["C", "⌫", None, "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

for i , row in enumerate(buttons):
    for j , val in enumerate(row):
        if val:
            Button(root, text=val, command=lambda v= val:HandleClick(v), **btn_config).grid(row=i+1, column=j, padx=5, pady=5)

def HandleKey(event):
    key = event.char
    if key in "0123456789+-*/.=":
        HandleClick(key)
    elif event.keysym == "Return":
        HandleClick("=")
    elif event.keysym == "BackSpace":
        HandleClick("back")
    elif event.keysym == "Escape":
        HandleClick("C")

root.bind("<Key>", lambda event: HandleKey(event))

root.mainloop()