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
        self.lblLin.grid(row=0, column=1)

        self.txtLin = Label(self.master, text=r"linkedin.com/in/nathanbahia", bg=self.BG, fg="#ffffff", font="Courier 12 bold").grid(row=0, column=2)

        self.imgGit = PhotoImage(file="images/github.png")
        self.lblGit = Label(self.master, image=self.imgGit, bg= self.BG)
        self.lblGit.image = self.imgGit
        self.lblGit.grid(row=0, column=3)

        self.txtGit = Label(self.master, text=r"github.com/nathanbahia", bg=self.BG, fg="#ffffff", font="Courier 12 bold").grid(row=0, column=4)

        self.imgIns = PhotoImage(file="images/instagram.png")
        self.lblIns = Label(self.master, image=self.imgIns, bg= self.BG)
        self.lblIns.image = self.imgIns
        self.lblIns.grid(row=0, column=5)

        self.txtIns = Label(self.master, text=r"instagram.com/noobpythonbr", bg=self.BG, fg="#ffffff", font="Courier 12 bold").grid(row=0, column=6)

        self.imgLogo = PhotoImage(file="images/login_screen_logo.png")
        self.lblLogo = Label(self.master, image=self.imgLogo, bg= self.BG)
        self.lblLogo.image = self.imgLogo
        self.lblLogo.grid(row=1, column=0, columnspan=9, pady=30)        
                
        self.frame_login = Frame(self.master, highlightbackground="#000000", highlightthickness=3)        
        self.frame_login.columnconfigure(0, minsize=10)
        self.frame_login.columnconfigure(1, minsize=200)
        self.frame_login.columnconfigure(2, minsize=10)
        self.frame_login.configure(background="#787878")
        self.frame_login.grid(row=2, column=0, columnspan=9, pady=4, padx=20)        
        
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

    def create_menu(self):
        self.btn_folha = Button(self.frame_content, text="FOLHA",width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn_folha["command"] = self.folha
        self.btn_folha.grid(row=0, column=0, sticky=W, pady=10, padx=10)
        
        self.btn_despesas = Button(self.frame_content, text="DESPESAS", width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn_despesas.grid(row=1, column=0, pady=10, sticky=W, padx=10)
        
        self.btn_projetos = Button(self.frame_content, text="PROJETOS", width=20, bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.btn_projetos.grid(row=2, column=0, sticky=W, pady=10, padx=10)

        self.btn_sair = Button(self.frame_content, text="SAIR", width=20, bg="#780011", fg="#ffffff", font="Courier 12 bold")
        self.btn_sair["command"] = root.destroy
        self.btn_sair.grid(row=3, column=0, sticky=W, pady=10, padx=10)


    def login(self):
        self.frame_login.destroy()
        self.lblLogo.destroy()

        self.frame_content.place(x=0, y=46, w=width, h=height)
        self.create_menu()
        
        
    def folha(self):
        self.lblMes = Label(self.frame_content, text="Selecione um mês:", bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.lblMes.grid(row=0, column=2)
                                    
        var = StringVar()
        meses = ["Janeiro","Fevereiro","Marco","Abril","Maio"]
        self.selecionaMes = OptionMenu(self.frame_content, var, *meses)
        self.selecionaMes["width"] = 7
        self.selecionaMes.grid(row=0, column=3)

        self.lblAno = Label(self.frame_content, text="Selecione um ano:", bg="#787878", fg="#ffffff", font="Courier 12 bold")
        self.lblAno.grid(row=0, column=4)
                                    
        var = StringVar()
        anos = [2015,2016,2017,2018,2019,2020]
        self.selecionaAno = OptionMenu(self.frame_content, var, *anos)
        self.selecionaAno["width"] = 7
        self.selecionaAno.grid(row=0, column=5)        

        self.btnBusca = Button(self.frame_content, text="BUSCAR").grid(row=0, column=6)

        

App(root)
root.geometry("{}x{}+0+0".format(width, height))
root.title("Interfaces Gráficas com Python")
root.mainloop()
