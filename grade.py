import tkinter as tk
from tkinter import messagebox
import disciplina as dis

class Grade():

    def __init__(self, ano, listaDisciplinas):
        self.__ano = ano
        self.__listaDisciplinas = listaDisciplinas

    def getAno(self):
        return self.__ano
    
    def getListaDisciplinas(self):
        return self.__listaDisciplinas

class LimiteInsereGrade(tk.Toplevel):
    def __init__(self, controle, listaDisciplinas):

        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Grade")
        self.controle = controle

        self.frameAno_Curso = tk.Frame(self)
        self.frameDisc = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameAno_Curso.pack()
        self.frameDisc.pack()
        self.frameButton.pack()
        
        self.labelAno = tk.Label(self.frameAno_Curso,text="Ano/Curso: ")
        self.labelListaDisciplinas = tk.Label(self.frameDisc,text="Lista de Disciplinas: ")
        self.labelAno.pack(side="left")
        self.labelListaDisciplinas.pack(side="left") 

        self.inputAno_Curso = tk.Entry(self.frameAno_Curso, width=20)
        self.inputAno_Curso.pack(side="left")

        self.listdisciplinas = tk.Listbox(self.frameDisc)
        self.listdisciplinas.pack(side="left")
        for i in listaDisciplinas:
            self.listdisciplinas.insert(tk.END, i)
        
        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Disciplina: ")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereDisciplina)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Grade")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaGrade)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraGrade():
    def __init__(self, str):
        messagebox.showinfo('Lista de Grades', str)

class CtrlGrade():
    def __init__(self, controlePrincipal):
        self.controlePrincipal = controlePrincipal
        self.listaGrade = []
        self.listaNomeDisc = []
        self.listaDisciplinas = []
    
    def insereGrade(self):
        self.listaDisciplinas = []
        self.listaNomeDisc = self.controlePrincipal.ctrlDisciplina.getListaNomeDisciplinas()
        self.limiteInsere = LimiteInsereGrade(self, self.listaNomeDisc)

    def mostraGrade(self):
        palavra = ''
        for grade in self.listaGrade:
            palavra += '\nAno/Curso: '+grade.getAno() 
            palavra += '\nLista de Disciplinas: \n'
            for disc in grade.getListaDisciplinas():
                palavra += 'Código: {} -- Nome: {} -- Carga Horária: {}\n'.format(disc.getCodigo(), disc.getNome(), disc.getCargaHoraria())
            palavra += '----------------------\n'
            
        self.limiteMostra = LimiteMostraGrade(palavra)
        
    def insereDisciplina(self, event):
        disciplinaSelecionada = self.limiteInsere.listdisciplinas.get(tk.ACTIVE)
        disc = self.controlePrincipal.ctrlDisciplina.getDisciplina(disciplinaSelecionada)
        self.listaDisciplinas.append(disc)
        self.limiteInsere.mostraJanela('Sucesso', 'Disciplina inserida na grade com sucesso!')
        self.limiteInsere.listdisciplinas.delete(tk.ACTIVE)
    
    def criaGrade(self, event):
        AnoCurso = self.limiteInsere.inputAno_Curso.get() 
        grade = Grade(AnoCurso, self.listaDisciplinas)
        self.listaGrade.append(grade)
        self.limiteInsere.mostraJanela('Sucesso', 'Grade cadastrada com sucesso!')
        self.limiteInsere.destroy()
    
    def getGrade(self):
        listaCurso = []
        for i in self.listaGrade:
            listaCurso.append(i.getAno())
        return listaCurso
    
    def getGradeSelecao(self, ano_Curso):
        ano_CursoRet = None
        for grade in self.listaGrade:
            if grade.getAno() == ano_Curso:
                ano_CursoRet = grade
                break
        return ano_CursoRet

    

    



        