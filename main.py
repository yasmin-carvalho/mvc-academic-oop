import tkinter as tk
from tkinter import messagebox
import aluno as alu
import curso as curs
import disciplina as dis
import grade as grad
import historico as hist

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('500x400')
        self.menubar = tk.Menu(self.root)        
        self.alunoMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.disciplinaMenu = tk.Menu(self.menubar)
        self.gradeMenu = tk.Menu(self.menubar)  
        self.historicoMenu = tk.Menu(self.menubar)   

        self.alunoMenu.add_command(label="Insere", command=self.controle.insereAlunos)
        self.alunoMenu.add_command(label="Mostra", command=self.controle.mostraAlunos)
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)

        self.cursoMenu.add_command(label="Insere", command=self.controle.insereCursos)
        self.cursoMenu.add_command(label="Mostra", command=self.controle.mostraCursos)
        self.menubar.add_cascade(label="Curso", menu=self.cursoMenu)

        self.disciplinaMenu.add_command(label="Insere", command=self.controle.insereDisciplinas)
        self.disciplinaMenu.add_command(label="Mostra", command=self.controle.mostraDisciplinas)    
        self.menubar.add_cascade(label="Disciplina", menu=self.disciplinaMenu)

        self.gradeMenu.add_command(label="Insere", command=self.controle.insereGrade)
        self.gradeMenu.add_command(label="Mostra", command=self.controle.mostraGrade)                     
        self.menubar.add_cascade(label="Grade", menu=self.gradeMenu)      
        
        self.historicoMenu.add_command(label="Insere", command=self.controle.insereHistorico)
        self.historicoMenu.add_command(label="Mostra", command=self.controle.mostraHistorico)                     
        self.menubar.add_cascade(label="Historico", menu=self.historicoMenu)    
  

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlAluno = alu.CtrlAluno()
        self.ctrlCurso = curs.CtrlCurso(self)
        self.ctrlDisciplina = dis.CtrlDisciplina()
        self.ctrlGrade = grad.CtrlGrade(self)
        self.ctrlHistorico = hist.CtrlHistorico(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Sistema Acadêmico Yasmin")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereAlunos(self):
        self.ctrlAluno.insereAlunos()

    def mostraAlunos(self):
        self.ctrlAluno.mostraAlunos()
    
    def insereCursos(self):
        self.ctrlCurso.insereCursos()

    def mostraCursos(self):
        self.ctrlCurso.mostraCursos()
    
    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()
     
    def insereGrade(self):
        self.ctrlGrade.insereGrade()

    def mostraGrade(self):
        self.ctrlGrade.mostraGrade()
    
    def insereHistorico(self):
        self.ctrlHistorico.insereHistorico()

    def mostraHistorico(self):
        self.ctrlHistorico.mostraHistorico()
    

if __name__ == '__main__':
    c = ControlePrincipal()