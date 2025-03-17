import tkinter

FONT1 = "Courier"

root = tkinter.Tk()
loginFrame = tkinter.Frame(root)
authFrame = tkinter.Frame(root)
#labels
usernameLabel = tkinter.Label(loginFrame, text="Username:", font=FONT1)
passwordLabel = tkinter.Label(loginFrame, text="Password:", font=FONT1)
#entries
entryUsername = tkinter.Entry(loginFrame, border=3)
entryPassword = tkinter.Entry(loginFrame, border=3, show="*")

#functions
def login():
    authFrame.tkraise()

#buttons
buttonLogin = tkinter.Button(loginFrame, text="Login", font=FONT1, border=3, command=login)


root.wm_geometry("300x300")
loginFrame.grid(column=0, row=0, sticky="news")
authFrame.grid(column=0, row=0, sticky="news")

usernameLabel.pack()
entryUsername.pack(pady=15)
passwordLabel.pack()
entryPassword.pack(pady=15)
buttonLogin.pack()

loginFrame.tkraise()


root.mainloop()