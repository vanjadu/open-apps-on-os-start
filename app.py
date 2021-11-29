import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('apps.txt'):
    with open('apps.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfile(initialdir="/", title="Select File",
                                      filetypes=(('executables', '*.app'), ('all files', '*./')))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="#9A0680")
        label.pack()


def runApps():
    for app in apps:
        os.startFile(app)


canvas = tk.Canvas(root, height=500, width=1000, bg="#79018C")
canvas.pack()

frame = tk.Frame(root, bg="#160040")
frame.place(relwidth=1, relheight=1)

openFile = tk.Button(root, text="Open File", padx=20, pady=10,
                     fg="#160040", bg="#160040", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=20,
                    pady=10, fg="#160040", bg="#160040", command=runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('apps.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
