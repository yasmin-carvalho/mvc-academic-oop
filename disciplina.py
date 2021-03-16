import tkinter as tk
from tkinter import messagebox

class Disciplina:

    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria

    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getCargaHoraria(self):
        return self.__cargaHoraria

class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Disciplina")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCodigo = tk.Frame(self)
        self.frameCargaHoraria = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameCargaHoraria.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCargaHoraria = tk.Label(self.frameCargaHoraria,text="Carga Horaria: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelCargaHoraria.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left") 
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left") 
        self.inputCargaHoraria = tk.Entry(self.frameCargaHoraria, width=20)
        self.inputCargaHoraria.pack(side="left") 

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

class LimiteMostraDisciplinas():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)

class CtrlDisciplina():       
    def __init__(self):
        self.listaDisciplinas = [
            Disciplina('COM220', 'Programação OO', 64),
            Disciplina('COM222', 'Programação Web', 64),
            Disciplina('COM111', 'Estruturas de Dados', 64)
        ]

    def getListaDisciplinas(self):
        return self.listaDisciplinas

    def getDisciplina(self, nome):
        discRet = None
        for disc in self.listaDisciplinas:
            if disc.getNome() == nome:
                discRet = disc
        return discRet

    def getListaNomeDisciplinas(self):
        listaNome = []
        for disc in self.listaDisciplinas:
            listaNome.append(disc.getNome())
        return listaNome

    def insereDisciplinas(self):
        self.limiteIns = LimiteInsereDisciplinas(self) 

    def mostraDisciplinas(self):
        texto = 'Código -- Nome\n'
        for disc in self.listaDisciplinas:
            texto += disc.getCodigo() + ' -- ' + disc.getNome() + '--' + str(disc.getCargaHoraria()) + '\n'
        self.limiteLista = LimiteMostraDisciplinas(texto)

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        cargaHoraria = int(self.limiteIns.inputCargaHoraria.get())
        disciplina = Disciplina(nroMatric, nome, cargaHoraria)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso!')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCargaHoraria.delete(0, len(self.limiteIns.inputCargaHoraria.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()