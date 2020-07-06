from tkinter import *

class App:
    def __init__(self, master=None):

        self.BG = "#484848"
        self.master = master
        self.master.configure(background=self.BG)
        self.master.columnconfigure(0, minsize=50)
        self.master.columnconfigure(1, minsize=50)
        self.master.columnconfigure(2, minsize=50)
        self.master.columnconfigure(3, minsize=50)
        self.master.columnconfigure(4, minsize=50)
        self.master.columnconfigure(5, minsize=50)
        self.master.columnconfigure(6, minsize=50)
        self.master.columnconfigure(7, minsize=50)
        self.master.columnconfigure(8, minsize=50)
        self.master.columnconfigure(9, minsize=50)
        
        

        self.imgLin = PhotoImage(file="images/linkedin.png")
        self.lblLin = Label(self.master, image=self.imgLin, bg= self.BG)
        self.lblLin.image = self.imgLin
        self.lblLin.grid(row=0, column=7)        

        self.imgGit = PhotoImage(file="images/github.png")
        self.lblGit = Label(self.master, image=self.imgGit, bg= self.BG)
        self.lblGit.image = self.imgGit
        self.lblGit.grid(row=0, column=8)

        self.imgIns = PhotoImage(file="images/instagram.png")
        self.lblIns = Label(self.master, image=self.imgIns, bg= self.BG)
        self.lblIns.image = self.imgIns
        self.lblIns.grid(row=0, column=9)

        self.imgLogo = PhotoImage(file="images/login_screen_logo.png")
        self.lblLogo = Label(self.master, image=self.imgLogo, bg= self.BG)
        self.lblLogo.image = self.imgLogo
        self.lblLogo.grid(row=1, column=0, columnspan=10)
        

       
        

root = Tk()
App(root)
root.geometry("{}x{}+0+0".format(500,500))
root.title("Interfaces Gráficas com Python")
root.mainloop()
