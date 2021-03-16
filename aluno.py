import tkinter as tk
from tkinter import messagebox

class Aluno():

    def __init__(self, nroMatric, nome):
        self.__nroMatric = nroMatric
        self.__nome = nome

    def getNroMatric(self):
        return self.__nroMatric
    
    def getNome(self):
        return self.__nome

class LimiteInsereAluno(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Aluno")
        self.controle = controle

        self.frameNroMatric = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroMatric.pack()
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNroMatric = tk.Label(self.frameNroMatric,text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNroMatric.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputNroMatric = tk.Entry(self.frameNroMatric, width=20)
        self.inputNroMatric.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraAlunos():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

class CtrlAluno():       
    def __init__(self):
        self.listaAlunos = [
            Aluno('1001', 'Lana Ramos'),
            Aluno('1002', 'Ariana Souza'),
            Aluno('1003', 'Patrick Silva'),
            Aluno('1004', 'Mateus Paiva')
        ]

    def getAluno(self, nome):
        alunoRet = None
        for aluno in self.listaAlunos:
            if aluno.getNroMatric() == nome:
                alunoRet = aluno
        return alunoRet

    def getListaNome(self):
        listaNome = []
        for est in self.listaAlunos:
            listaNome.append(est.getNome())
        return listaNome

    def insereAlunos(self):
        self.limiteIns = LimiteInsereAluno(self) 

    def mostraAlunos(self):
        str = 'Nro Matric. -- Nome\n'
        for est in self.listaAlunos:
            str += est.getNroMatric() + ' -- ' + est.getNome() + '\n'       
        self.limiteLista = LimiteMostraAlunos(str)

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNroMatric.get()
        nome = self.limiteIns.inputNome.get()
        aluno = Aluno(nroMatric, nome)
        self.listaAlunos.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNroMatric.delete(0, len(self.limiteIns.inputNroMatric.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    
