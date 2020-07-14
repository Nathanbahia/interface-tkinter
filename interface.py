from tkinter import *

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

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
        self.lblLin.grid(row=0, column=1, pady=5)

        self.txtLin = Label(self.master, text=r"linkedin.com/in/nathanbahia", bg=self.BG, fg="#ffffff", font="Courier 12 bold").grid(row=0, column=2, pady=5)

        self.imgGit = PhotoImage(file="images/github.png")
        self.lblGit = Label(self.master, image=self.imgGit, bg= self.BG)
        self.lblGit.image = self.imgGit
        self.lblGit.grid(row=0, column=3, pady=5)

        self.txtGit = Label(self.master, text=r"github.com/nathanbahia", bg=self.BG, fg="#ffffff", font="Courier 12 bold").grid(row=0, column=4, pady=5)

        self.imgIns = PhotoImage(file="images/instagram.png")
        self.lblIns = Label(self.master, image=self.imgIns, bg= self.BG)
        self.lblIns.image = self.imgIns
        self.lblIns.grid(row=0, column=5, pady=5)

        self.txtIns = Label(self.master, text=r"instagram.com/noobpythonbr", bg=self.BG, fg="#ffffff", font="Courier 12 bold").grid(row=0, column=6, pady=5)

        self.imgLogo = PhotoImage(file="images/login_screen_logo.png")
        self.lblLogo = Label(self.master, image=self.imgLogo, bg= self.BG)
        self.lblLogo.image = self.imgLogo
        self.lblLogo.grid(row=1, column=0, columnspan=9, pady=50)        
                
        self.frame_login = Frame(self.master, highlightbackground="#000000", highlightthickness=3)        
        self.frame_login.columnconfigure(0, minsize=10)
        self.frame_login.columnconfigure(1, minsize=200)
        self.frame_login.columnconfigure(2, minsize=10)
        self.frame_login.configure(background="#787878")
        self.frame_login.grid(row=2, column=0, columnspan=9, pady=50, padx=50)        
        
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
        self.btn["width"] = 28
        self.btn["command"] = self.login
        self.btn.grid(row=2, column=0, columnspan=3, pady=10, sticky=N)

        self.frame_content = Frame(self.master)
        self.frame_content.configure(background="#787878")
        self.frame_content.columnconfigure(0, minsize=100)
        self.frame_content.columnconfigure(1, minsize=100)
        self.frame_content.columnconfigure(2, minsize=100)
        self.frame_content.columnconfigure(3, minsize=100)
        self.frame_content.columnconfigure(4, minsize=100)
        self.frame_content.columnconfigure(5, minsize=100)
        self.frame_content.columnconfigure(6, minsize=100)
        self.frame_content.columnconfigure(7, minsize=100)
        self.frame_content.columnconfigure(8, minsize=100)

        self.buttons = []


    def login(self):
        self.frame_login.destroy()
        self.lblLogo.destroy()

        self.frame_content.place(x=0, y=46, w=width, h=height)
        self.create_menu()
        

    def create_menu(self):

        self.buttons = []
        
        self.btn1 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn1["command"] = self.selectButton1
        self.btn1.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        self.btn2 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn2["command"] = self.selectButton2
        self.btn2.grid(row=1, column=0, sticky=W, pady=10, padx=10)
        
        self.btn3 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn3["command"] = self.selectButton3
        self.btn3.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        self.btn4 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn4["command"] = self.selectButton4
        self.btn4.grid(row=3, column=0, sticky=W, pady=10, padx=10)

        self.btn5 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn5["command"] = self.selectButton5
        self.btn5.grid(row=4, column=0, sticky=W, pady=10, padx=10)

        self.btn6 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn6["command"] = self.selectButton6
        self.btn6.grid(row=5, column=0, sticky=W, pady=10, padx=10)

        self.btn7 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn7["command"] = self.selectButton7
        self.btn7.grid(row=6, column=0, sticky=W, pady=10, padx=10)

        self.btn8 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn8["command"] = self.selectButton8
        self.btn8.grid(row=7, column=0, sticky=W, pady=10, padx=10)

        self.btn9 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn9["command"] = self.selectButton9
        self.btn9.grid(row=8, column=0, sticky=W, pady=10, padx=10)

        self.btn10 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn10["command"] = self.selectButton10
        self.btn10.grid(row=9, column=0, sticky=W, pady=10, padx=10)

        self.btn11 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn11["command"] = self.selectButton11
        self.btn11.grid(row=10, column=0, sticky=W, pady=10, padx=10)

        self.btn12 = Button(self.frame_content, text="FUNCTION",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn12["command"] = self.selectButton12
        self.btn12.grid(row=11, column=0, sticky=W, pady=10, padx=10)
      
        self.btn_sair = Button(self.frame_content, text="SAIR", width=20, bg="#780011", fg="#ffffff", font="Courier 12 bold")
        self.btn_sair["command"] = self.close
        self.btn_sair.grid(row=12, column=0, sticky=W, pady=10, padx=10)

        self.buttons = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6,
                        self.btn7, self.btn8, self.btn9, self.btn10, self.btn11, self.btn12]

        # animations
        self.labelTitle = Label(self.frame_content, text="")
        self.posyLabelTitle = -100

        self.posxAnimateClose1 = -int(width/2)
        self.posxAnimateClose2 = width

        self.frame1 = Frame(self.frame_content)
        self.frame1.configure(background="#000000")        

        self.frame2 = Frame(self.frame_content)
        self.frame2.configure(background="#000000")        


    def showTitle(self, message):
        self.labelTitle.place(x=0, y=-200)
        
        self.labelTitle = Label(self.frame_content, text=message.upper(), font="None 32 bold", bg="#787878")
        self.labelTitle.place(x = 250, y = self.posyLabelTitle)

        self.animateTitle()
        

    def animateTitle(self):
        if self.posyLabelTitle < 0:
            self.posyLabelTitle += 5
            self.labelTitle.place(x = 250, y = self.posyLabelTitle)
            self.labelTitle.after(10, self.animateTitle)
        else:
            self.posyLabelTitle = -50
            

    def selectButton1(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn1["bg"] = "#0275d8"
        self.showTitle("button 1 clicked")
        

    def selectButton2(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn2["bg"] = "#0275d8"
        self.showTitle("button 2 clicked")
        

    def selectButton3(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn3["bg"] = "#0275d8"
        self.showTitle("button 3 clicked")

    def selectButton4(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn4["bg"] = "#0275d8"
        self.showTitle("button 4 clicked")
        

    def selectButton5(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn5["bg"] = "#0275d8"
        self.showTitle("button 5 clicked")
        

    def selectButton6(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn6["bg"] = "#0275d8"
        self.showTitle("button 6 clicked")

    def selectButton7(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn7["bg"] = "#0275d8"
        self.showTitle("button 7 clicked")
        

    def selectButton8(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn8["bg"] = "#0275d8"
        self.showTitle("button 8 clicked")
        

    def selectButton9(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn9["bg"] = "#0275d8"
        self.showTitle("button 9 clicked")

    def selectButton10(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn10["bg"] = "#0275d8"
        self.showTitle("button 10 clicked")
        

    def selectButton11(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn11["bg"] = "#0275d8"
        self.showTitle("button 11 clicked")
        

    def selectButton12(self):
        for button in self.buttons:            
            button["bg"] = "#787878"
        self.btn12["bg"] = "#0275d8"
        self.showTitle("button 12 clicked")        


    def close(self):
        self.labelTitle.place(x=0, y=-200)
        
        self.frame1.place(x=self.posxAnimateClose1, y=0, w=width/2 + 20, h=height)
        self.frame2.place(x=self.posxAnimateClose2, y=0, w=width/2 + 20, h=height)        

        if self.posxAnimateClose1 < -20:
            self.posxAnimateClose1 += 20
            self.posxAnimateClose2 -= 20
    
            self.frame1.after(30, self.close)
        else:
            #root.destroy()
            pass
        
        
App(root)
root.geometry("{}x{}+0+0".format(width, height))
root.title("Interfaces Gráficas com Python")
root.mainloop()
