from tkinter import *

class App:
    def __init__(self, master=None):
                
        self.BG = "#484848"
        self.master = master
        self.master.configure(background=self.BG)
        self.master.columnconfigure(0, minsize=100)
        self.master.columnconfigure(1, minsize=100)
        self.master.columnconfigure(2, minsize=100)
        self.master.columnconfigure(3, minsize=100)
        self.master.columnconfigure(4, minsize=100)
        self.master.columnconfigure(5, minsize=100)
        self.master.columnconfigure(6, minsize=100)
        self.master.columnconfigure(7, minsize=100)
        self.master.columnconfigure(8, minsize=100)
        self.master.columnconfigure(9, minsize=100)
                
        self.imgLin = PhotoImage(file="images/linkedin.png")
        self.lblLin = Label(self.master, image=self.imgLin, bg= self.BG)
        self.lblLin.image = self.imgLin
        self.lblLin.grid(row=0, column=7, pady=5)        

        self.imgGit = PhotoImage(file="images/github.png")
        self.lblGit = Label(self.master, image=self.imgGit, bg= self.BG)
        self.lblGit.image = self.imgGit
        self.lblGit.grid(row=0, column=8, pady=5)

        self.imgIns = PhotoImage(file="images/instagram.png")
        self.lblIns = Label(self.master, image=self.imgIns, bg= self.BG)
        self.lblIns.image = self.imgIns
        self.lblIns.grid(row=0, column=9, pady=5)

        self.imgLogo = PhotoImage(file="images/login_screen_logo.png")
        self.lblLogo = Label(self.master, image=self.imgLogo, bg= self.BG)
        self.lblLogo.image = self.imgLogo
        self.lblLogo.grid(row=1, column=0, columnspan=10, pady=10)        
                
        self.frame_login = Frame(self.master, highlightbackground="black", highlightthickness=3)        
        self.frame_login.columnconfigure(0, minsize=10)
        self.frame_login.columnconfigure(1, minsize=200)
        self.frame_login.columnconfigure(2, minsize=10)
        self.frame_login.configure(background="#787878")
        self.frame_login.grid(row=2, column=0, columnspan=10, pady=20, padx=20)        
        
        self.imgLogin = PhotoImage(file="images/person.png")
        self.lblLogin = Label(self.frame_login, image=self.imgLogin, bg="#787878")
        self.lblLogin.image = self.imgLogin
        self.lblLogin.grid(row=0, column=0, padx=3)
        
        self.entry_user = Entry(self.frame_login, width=23, font="Courier")
        self.entry_user.grid(row=0, column=1, columnspan=5, sticky=W, pady=10, padx=10)
        
        self.imgPass = PhotoImage(file="images/password.png")
        self.lblPass = Label(self.frame_login, image=self.imgPass, bg="#787878")
        self.lblPass.image = self.imgPass
        self.lblPass.grid(row=1, column=0, padx=3)
        
        self.entry_pass = Entry(self.frame_login, show="*", width=23, font="Courier")
        self.entry_pass.grid(row=1, column=1, columnspan=5, sticky=W, padx=10)
        
        self.btn = Button(self.frame_login, text = "Login", bg="#000000", fg="#ffffff", font="Courier 12 bold")
        self.btn["width"] = 25
        self.btn["command"] = self.login
        self.btn.grid(row=2, column=0, columnspan=3, pady=10)


    def login(self):
        self.frame_login.destroy()
        self.lblLogo.destroy()
        
        
    def change_mode(self):
        self.BG = "#ffffff"
        self.master.configure(background=self.BG)
            

        

       
        

root = Tk()
App(root)
root.geometry("{}x{}+0+0".format(1000,600))
root.title("Interfaces Gráficas com Python")
root.mainloop()
