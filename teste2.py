from tkinter import *
from tkinter import messagebox as ms
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.messagebox import *
import sqlite3
			

# Criacao do banco de dados "teste2" com a tabela user caso nao exista!
with sqlite3.connect('teste2.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEXT NOT NULL,nome TEXt,email TEXt,cpf TEXt);')
db.commit()
db.close()

class main:
    def __init__(self,master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_nome = StringVar()
        self.n_email = StringVar()
        self.n_cpf = StringVar()
        
        self.widgets()

    #Funcao de Login
    def login(self):
    	
        with sqlite3.connect('teste2.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()


        if result: 
            self.logf.pack_forget()
            class Images(Frame):
                def __init__(self, root):
                    self.root = root
                    self.root.title('puthon-sqlite3-project')
                    self.root.geometry('1100x500+-10+10')
                    self.root.resizable(width=1, height=1)
                    self.root.configure(bg="#0B0B3B")
                    
                    files = "./imagens/fundo.jpg"

                    self.var = StringVar()
                    self.var.set(files.title())
                    self.nameLabel = Label(
                        self.root , textvariable=self.var, 
                        bd=2, fg='black', bg='white', 
                        font='helvetica, 15 bold', relief='raised', width=50)
                    self.nameLabel.place(x=350, y=1)

                    self.img1 = Image.open(files)
                    self.img1 =  self.img1.resize((300, 300), Image.ANTIALIAS)
                    self.img = ImageTk.PhotoImage(self.img1)
                    self.imageLabel = Label(self.root)
                    self.imageLabel.place(x=100, y=80)
                    self.imageLabel["compound"] = LEFT
                    self.imageLabel["image"] = self.img

                

                    self.img2 = Image.open(files)
                    self.img2 =  self.img2.resize((300, 300), Image.ANTIALIAS)
                    self.img2 = ImageTk.PhotoImage(self.img2)
                    self.imageLabel2 = Label(self.root)
                    self.imageLabel2.place(x=500, y=80)
                    self.imageLabel2["compound"] = LEFT
                    self.imageLabel2["image"] = self.img2

                    self.img3 = Image.open(files)
                    self.img3 =  self.img3.resize((300, 300), Image.ANTIALIAS)
                    self.img3 = ImageTk.PhotoImage(self.img3)
                    self.imageLabel3 = Label(self.root)
                    self.imageLabel3.place(x=900, y=80)
                    self.imageLabel3["compound"] = LEFT
                    self.imageLabel3["image"] = self.img3

                    self.img4 = Image.open(files)
                    self.img4 =  self.img4.resize((300, 300), Image.ANTIALIAS)
                    self.img4 = ImageTk.PhotoImage(self.img4)
                    self.imageLabel4 = Label(self.root)
                    self.imageLabel4.place(x=100, y=400)
                    self.imageLabel4["compound"] = LEFT
                    self.imageLabel4["image"] = self.img4

                    self.img5 = Image.open(files)
                    self.img5 =  self.img5.resize((300, 300), Image.ANTIALIAS)
                    self.img5 = ImageTk.PhotoImage(self.img5)
                    self.imageLabel5 = Label(self.root)
                    self.imageLabel5.place(x=500, y=400)
                    self.imageLabel5["compound"] = LEFT
                    self.imageLabel5["image"] = self.img5

                    self.img6 = Image.open(files)
                    self.img6 =  self.img6.resize((300, 300), Image.ANTIALIAS)
                    self.img6 = ImageTk.PhotoImage(self.img6)
                    self.imageLabel6 = Label(self.root)
                    self.imageLabel6.place(x=900, y=400)
                    self.imageLabel6["compound"] = LEFT
                    self.imageLabel6["image"] = self.img6

                    #  Logica que carrega as imagens de determinada pasta em um formato de grid!
                    def loadImages():
                        directory = filedialog.askdirectory()
                    
                        os.chdir(directory)
                        allImages = os.listdir()
                        allImages.reverse()
                        self.listImages = Listbox(self.root, bd=5, width=100, height=2,selectbackground='grey73')
                        self.listImages.place(x=0, y=900)
                        for image in allImages: 
                            pos = 0
                            if image.endswith(('png', 'jpg', 'jpeg', 'ico')):
                                self.listImages.insert(pos, image)
                                pos +=1
                        self.listImages.selection_set(0)
                        self.listImages.see(0)
                        self.listImages.activate(0)
                        self.listImages.selection_anchor(0)
                        image = self.listImages.curselection()
                        images = self.listImages.get(image[0])
                        self.img1 = Image.open(images)
                        self.img1 =  self.img1.resize((300, 300), Image.ANTIALIAS)
                        self.img = ImageTk.PhotoImage(self.img1,)
                        self.imageLabel = Label(self.root)
                        self.imageLabel.place(x=100, y=80)
                        self.imageLabel["compound"] = LEFT
                        self.imageLabel["image"] = self.img


                        for image in allImages: 
                            pos = 0
                            if image.endswith(('png', 'jpg', 'jpeg', 'ico')):
                                self.listImages.insert(pos, image)
                                pos +=1
                        self.listImages.selection_set(1)
                        self.listImages.see(0)
                        self.listImages.activate(0)
                        self.listImages.selection_anchor(0)
                        image = self.listImages.curselection()
                        images2 = self.listImages.get(image[0])
                        
                        self.img2 = Image.open(images2)
                        self.img2 =  self.img2.resize((300, 300), Image.ANTIALIAS)
                        self.img2 = ImageTk.PhotoImage(self.img2,)
                        self.imageLabel2 = Label(self.root)
                        self.imageLabel2.place(x=500, y=80)
                        self.imageLabel2["compound"] = LEFT
                        self.imageLabel2["image"] = self.img2

                        for image in allImages: 
                            pos = 0
                            if image.endswith(('png', 'jpg', 'jpeg', 'ico')):
                                self.listImages.insert(pos, image)
                                pos +=1
                        self.listImages.selection_set(2)
                        self.listImages.see(0)
                        self.listImages.activate(0)
                        self.listImages.selection_anchor(0)
                        image = self.listImages.curselection()
                        images3 = self.listImages.get(image[0])
                        
                        self.img3 = Image.open(images3)
                        self.img3 =  self.img3.resize((300, 300), Image.ANTIALIAS)
                        self.img3 = ImageTk.PhotoImage(self.img3,)
                        self.imageLabel3 = Label(self.root)
                        self.imageLabel3.place(x=900, y=80)
                        self.imageLabel3["compound"] = LEFT
                        self.imageLabel3["image"] = self.img3

                        for image in allImages:
                            pos = 0
                            if image.endswith(('png', 'jpg', 'jpeg', 'ico')):
                                self.listImages.insert(pos, image)
                                pos +=1
                        self.listImages.selection_set(3)
                        self.listImages.see(0)
                        self.listImages.activate(0)
                        self.listImages.selection_anchor(0)
                        image = self.listImages.curselection()
                        images4 = self.listImages.get(image[0])
                        
                        self.img4 = Image.open(images4)
                        self.img4 =  self.img4.resize((300, 300), Image.ANTIALIAS)
                        self.img4 = ImageTk.PhotoImage(self.img4,)
                        self.imageLabel4 = Label(self.root)
                        self.imageLabel4.place(x=100, y=400)
                        self.imageLabel4["compound"] = LEFT
                        self.imageLabel4["image"] = self.img4

                        for image in allImages: 
                            pos = 0
                            if image.endswith(('png', 'jpg', 'jpeg', 'ico')):
                                self.listImages.insert(pos, image)
                                pos +=1
                        self.listImages.selection_set(4)
                        self.listImages.see(0)
                        self.listImages.activate(0)
                        self.listImages.selection_anchor(0)
                        image = self.listImages.curselection()
                        images5 = self.listImages.get(image[0])
                        
                        self.img5 = Image.open(images5)
                        self.img5 =  self.img5.resize((300, 300), Image.ANTIALIAS)
                        self.img5 = ImageTk.PhotoImage(self.img5,)
                        self.imageLabel5 = Label(self.root)
                        self.imageLabel5.place(x=500, y=400)
                        self.imageLabel5["compound"] = LEFT
                        self.imageLabel5["image"] = self.img5

                        for image in allImages:
                            pos = 0
                            if image.endswith(('png', 'jpg', 'jpeg', 'ico')):
                                self.listImages.insert(pos, image)
                                pos +=1
                        self.listImages.selection_set(5)
                        self.listImages.see(0)
                        self.listImages.activate(0)
                        self.listImages.selection_anchor(0)
                        image = self.listImages.curselection()
                        images6 = self.listImages.get(image[0])
                        
                        self.img6 = Image.open(images6)
                        self.img6 =  self.img6.resize((300, 300), Image.ANTIALIAS)
                        self.img6 = ImageTk.PhotoImage(self.img6,)
                        self.imageLabel6 = Label(self.root)
                        self.imageLabel6.place(x=900, y=400)
                        self.imageLabel6["compound"] = LEFT
                        self.imageLabel6["image"] = self.img6

                        # Logica para avancar as imagens
                    def nextImage():
                        try:
                            next_one = self.listImages.curselection()
                            next_one = next_one[0]+1
                            image = self.listImages.get(next_one)
                            self.img1 = Image.open(image)
                            self.img1 =  self.img1.resize((300, 300), Image.ANTIALIAS)
                            self.img = ImageTk.PhotoImage(self.img1,)
                            self.imageLabel = Label(self.root)
                            self.imageLabel.place(x=100, y=80)
                            self.imageLabel["compound"] = LEFT
                            self.imageLabel["image"] = self.img
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]+1
                            image = self.listImages.get(next_one)
                            self.img2 = Image.open(image)
                            self.img2 =  self.img2.resize((300, 300), Image.ANTIALIAS)
                            self.img2 = ImageTk.PhotoImage(self.img2,)
                            self.imageLabel2 = Label(self.root)
                            self.imageLabel2.place(x=500, y=80)
                            self.imageLabel2["compound"] = LEFT
                            self.imageLabel2["image"] = self.img2
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]+1
                            image = self.listImages.get(next_one)
                            self.img3 = Image.open(image)
                            self.img3 =  self.img3.resize((300, 300), Image.ANTIALIAS)
                            self.img3 = ImageTk.PhotoImage(self.img3,)
                            self.imageLabel3 = Label(self.root)
                            self.imageLabel3.place(x=900, y=80)
                            self.imageLabel3["compound"] = LEFT
                            self.imageLabel3["image"] = self.img3
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]+1
                            image = self.listImages.get(next_one)
                            self.img4 = Image.open(image)
                            self.img4 =  self.img4.resize((300, 300), Image.ANTIALIAS)
                            self.img4 = ImageTk.PhotoImage(self.img4,)
                            self.imageLabel4 = Label(self.root)
                            self.imageLabel4.place(x=100, y=400)
                            self.imageLabel4["compound"] = LEFT
                            self.imageLabel4["image"] = self.img4
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]+1
                            image = self.listImages.get(next_one)
                            self.img5 = Image.open(image)
                            self.img5 =  self.img5.resize((300, 300), Image.ANTIALIAS)
                            self.img5 = ImageTk.PhotoImage(self.img5,)
                            self.imageLabel5 = Label(self.root)
                            self.imageLabel5.place(x=500, y=400)
                            self.imageLabel5["compound"] = LEFT
                            self.imageLabel5["image"] = self.img5
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]+1
                            image = self.listImages.get(next_one)
                            self.img6 = Image.open(image)
                            self.img6 =  self.img6.resize((300, 300), Image.ANTIALIAS)
                            self.img6 = ImageTk.PhotoImage(self.img6,)
                            self.imageLabel6 = Label(self.root)
                            self.imageLabel6.place(x=900, y=400)
                            self.imageLabel6["compound"] = LEFT
                            self.imageLabel6["image"] = self.img6
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)
                        except:
                            showerror("No Next Image", "Please press the Previous button")

                        #Logica para voltar as imagens
                    def previousImage():
                        try:
                            next_one = self.listImages.curselection()
                            next_one = next_one[0]-1
                            image = self.listImages.get(next_one)
                            self.img1 = Image.open(image)
                            self.img1 =  self.img1.resize((300, 300), Image.ANTIALIAS)
                            self.img = ImageTk.PhotoImage(self.img1,)
                            self.imageLabel = Label(self.root)
                            self.imageLabel.place(x=100, y=80)
                            self.imageLabel["compound"] = LEFT
                            self.imageLabel["image"] = self.img
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]-1
                            image = self.listImages.get(next_one)
                            self.img2 = Image.open(image)
                            self.img2 =  self.img2.resize((300, 300), Image.ANTIALIAS)
                            self.img2 = ImageTk.PhotoImage(self.img2,)
                            self.imageLabel2 = Label(self.root)
                            self.imageLabel2.place(x=500, y=80)
                            self.imageLabel2["compound"] = LEFT
                            self.imageLabel2["image"] = self.img2
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]-1
                            image = self.listImages.get(next_one)
                            self.img3 = Image.open(image)
                            self.img3 =  self.img3.resize((300, 300), Image.ANTIALIAS)
                            self.img3 = ImageTk.PhotoImage(self.img3,)
                            self.imageLabel3 = Label(self.root)
                            self.imageLabel3.place(x=900, y=80)
                            self.imageLabel3["compound"] = LEFT
                            self.imageLabel3["image"] = self.img
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]-1
                            image = self.listImages.get(next_one)
                            self.img4 = Image.open(image)
                            self.img4 =  self.img4.resize((300, 300), Image.ANTIALIAS)
                            self.img = ImageTk.PhotoImage(self.img4,)
                            self.imageLabel4 = Label(self.root)
                            self.imageLabel4.place(x=100, y=400)
                            self.imageLabel4["compound"] = LEFT
                            self.imageLabel4["image"] = self.img4
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]-1
                            image = self.listImages.get(next_one)
                            self.img5 = Image.open(image)
                            self.img5 =  self.img5.resize((300, 300), Image.ANTIALIAS)
                            self.img5 = ImageTk.PhotoImage(self.img5,)
                            self.imageLabel5 = Label(self.root)
                            self.imageLabel5.place(x=500, y=400)
                            self.imageLabel5["compound"] = LEFT
                            self.imageLabel5["image"] = self.img5
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)

                            next_one = self.listImages.curselection()
                            next_one = next_one[0]-1
                            image = self.listImages.get(next_one)
                            self.img6 = Image.open(image)
                            self.img6 =  self.img6.resize((300, 300), Image.ANTIALIAS)
                            self.img6 = ImageTk.PhotoImage(self.img6,)
                            self.imageLabel6 = Label(self.root)
                            self.imageLabel6.place(x=900, y=400) 
                            self.imageLabel6["compound"] = LEFT
                            self.imageLabel6["image"] = self.img6
                            self.listImages.select_clear(0, END)
                            self.listImages.activate(next_one)
                            self.listImages.selection_set(next_one, last=None)
                            self.var.set(image)
                        except:
                            showerror("Sem imagem anterior", "Prescione a tecla seguinte!")

                        # Chamando as funcoes criadas nos comandos dos buttons abaixo
                    self.button1 = Button(self.root,  text='<<', bd=5 ,bg='#8A0829', fg='black', border=0, font='helvetica, 10 bold', command=nextImage)
                    self.button1.place(x=50, y=300)
                    self.button2 = Button(self.root,  text='>>', bd=5 , bg='#8A0829', fg='black', border=0, font='helvetica, 10 bold', command=nextImage)
                    self.button2.place(x=1220, y=300)

                    self.root.bind('<Right>', lambda x: nextImage())
                    self.root.bind('<Left>', lambda x: nextImage())

                    
                    self.buttonBrowse = Button(self.root , text=u"\U0001F5C1 Buscar Imagens \U0001F5C1 ", bd=3, bg='#8A0829', fg='white', font='helvetica, 10 bold', command=loadImages)
                    self.buttonBrowse.place(x=4, y=1)

                    self.Exit = Button(self.root , text="Sair", bd=3, fg='white', width=10, bg='#8A0829', font='helvetica, 10',  command=self.root.destroy)
                    self.Exit.place(x=1200, y=1)

            def main2():
                
                ui = Images(root)
                

            if __name__ == "__main__":
                main2()


        else:
            ms.showerror('Oops!','Usuario nao encontrado!')
            
    def new_user(self):
    	#Estabelecendo conexao
        with sqlite3.connect('teste2.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT username FROM user WHERE username = ?')
        c.execute(find_user,[(self.n_username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Nome de usuário ja foi escolhido Tente um diferente.')
        else:
            ms.showinfo('Boa!','Conta Criada!')
            self.log()
        #Criar nova conta
        insert = 'INSERT INTO user(username,password,nome,email,cpf) VALUES(?,?,?,?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get()),(self.n_nome.get()),(self.n_email.get()),(self.n_cpf.get())])
        db.commit()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN!'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.n_nome.set('')
        self.n_email.set('')
        self.n_cpf.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Criar conta'
        self.crf.pack()
        
    
    def widgets(self):

        color='#0B0B3B'			

        self.head = Label(self.master,text = 'BEM VINDO!',bg='#8A0829',fg='white', font = ('',30),pady = 30, padx= 204)
        self.head.pack()
        self.logf = Frame(self.master,padx =150,bg=color,pady = 100)
        Label(self.logf,text = 'Usuario: ',  bg='#0B0B3B', fg='white', border=0, font = ('',20),pady=4,padx=4).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Senha: ',  bg='#0B0B3B', fg='white', border=0, font = ('',20),pady=4,padx=4).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 3 , font = ('',15),padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Criar Conta ',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()


        self.crf = Frame(self.master,padx =10,pady = 10)
        Label(self.crf,text = 'Usuario: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Senha: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Label(self.crf,text = 'Nome: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_nome,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(self.crf,text = 'Email: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_email,bd = 5,font = ('',15)).grid(row=3,column=1)
        Label(self.crf,text = 'CPF: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_cpf,bd = 5,font = ('',15)).grid(row=4,column=1)
        Button(self.crf,text = 'Criar Conta',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Ir para Login',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.log).grid(row=5,column=1)

if __name__ == '__main__':
    root = Tk()
    root.title('PYTHON-SQLITE3-PROJECT')
    main(root)
    root.mainloop()