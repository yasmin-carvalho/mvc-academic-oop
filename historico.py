import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import aluno as alu
import curso as curs
import grade as grad

class Historico():
    def __init__(self, aluno, listaDisciplinas, ano, semestre, nota):
        self.__aluno = aluno
        self.__listaDisciplinas = listaDisciplinas
        self.__ano = ano
        self.__semestre = semestre
        self.__nota = nota

    def getAluno(self):
        return self.__aluno
    
    def getListaDisciplinas(self):
        return self.__listaDisciplinas

    def getAno(self):
        return self.__ano
    
    def getSemestre(self):
        return self.__semestre
    
    def getNota(self):
        return self.__nota

class LimiteInsereHistorico(tk.Toplevel):
    def __init__(self, controle, alunos, disciplinas):
        tk.Toplevel.__init__(self)
        self.geometry('500x400')
        self.title("Disciplina")
        self.controle = controle

        self.frameNota = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameSemestre = tk.Frame(self)
        self.frameAluno = tk.Frame(self)
        self.frameListaDisc = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNota.pack()
        self.frameAno.pack()
        self.frameSemestre.pack()
        self.frameAluno.pack()
        self.frameListaDisc.pack()
        self.frameButton.pack()

        self.labelNota = tk.Label(self.frameNota, text='Nota: ')
        self.labelNota.pack(side='left')
        self.inputNota = tk.Entry(self.frameNota, width=5)
        self.inputNota.pack(side='left')

        self.labelAno = tk.Label(self.frameAno, text='Ano: ')
        self.labelAno.pack(side='left')
        self.inputAno = tk.Entry(self.frameAno, width=6)
        self.inputAno.pack(side='left')

        self.labelAluno = tk.Label(self.frameAluno, text='Aluno: ')
        self.labelAluno.pack(side='left')
        self.escolhaAluno = tk.StringVar()
        self.comboboxAluno = ttk.Combobox(self.frameAluno, width=30, textvariable=self.escolhaAluno)
        self.comboboxAluno.pack(side='left')
        self.comboboxAluno['values'] = alunos

        self.labelSemestre = tk.Label(self.frameSemestre, text='Semestre: ')
        self.labelSemestre.pack(side='left')
        self.comboboxSemestre = ttk.Combobox(self.frameSemestre, width=3, values=['1', '2'])
        self.comboboxSemestre.pack(side='left')

        self.labelDisciplinas = tk.Label(self.frameListaDisc, text='Selecione as disciplinas: ')
        self.labelDisciplinas.pack(side='left')
        self.listDisciplina = tk.Listbox(self.frameListaDisc)
        self.listDisciplina.pack(side='left')
        for disc in disciplinas:
            self.listDisciplina.insert(tk.END, disc.getNome())

        self.buttonInsereHistorico = tk.Button(self.frameButton, text='Inserir disciplina')
        self.buttonInsereHistorico.pack(side='left')
        self.buttonInsereHistorico.bind('<Button>', controle.insereDisciplina)

        self.buttonCria = tk.Button(self.frameButton, text='Criar Histórico')
        self.buttonCria.pack(side='left')
        self.buttonCria.bind('<Button>', controle.criaHistorico)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraHistorico():
    def __init__(self, texto):
        messagebox.showinfo('Lista de Historicos', texto)

class CtrlHistorico():
    def __init__(self, controlePrincipal):
        self.controlePrincipal = controlePrincipal
        self.listaHistorico = []
        self.listaDisciplinasHistorico = []
        self.listaNotaDisciplina = []
        self.listaNota = []
    
    def insereHistorico(self):
        listaNomeDeAlunos = self.controlePrincipal.ctrlAluno.getListaNome()
        listaDeDisciplina = self.controlePrincipal.ctrlDisciplina.listaDisciplinas
        self.limiteInsere = LimiteInsereHistorico(self, listaNomeDeAlunos, listaDeDisciplina)

    def mostraHistorico(self):
        texto = '**************---- EMITIR HISTÓRICO ----**************\n'
        for i in self.listaHistorico:
            texto += '\nAluno: {} \nMatricula: {} \nAno: {} \nSemestre: {}\n'.format(i.getAluno().getNome(), i.getAluno().getNroMatric(), i.getAno(), i.getSemestre())
            for disc, nota in self.listaDisciplinasHistorico:
                if nota>=6 :
                    texto += 'Cod: {} -- Nome: {} -- CH: {} -- Nota: {} - Aprovado\n'.format(disc.getCodigo(), disc.getNome(), disc.getCargaHoraria(), nota)
                else:
                    texto += 'Cod: {} -- Nome: {} -- CH: {} -- Nota: {} - Reprovado\n'.format(disc.getCodigo(), disc.getNome(), disc.getCargaHoraria(), nota)
        texto += '\n------------------------------------------'
        self.limiteMostra = LimiteMostraHistorico(texto)

    def insereDisciplina(self, event):
        nota = float(self.limiteInsere.inputNota.get())
        disciplinaSelecionada = self.limiteInsere.listDisciplina.get(tk.ACTIVE)
        disc = self.controlePrincipal.ctrlDisciplina.getDisciplina(disciplinaSelecionada)
        self.listaDisciplinasHistorico.append((disc, nota))
        self.listaNotaDisciplina.append(nota)
        self.limiteInsere.mostraJanela('Sucesso', 'Disciplina e nota inseridas')
        self.limiteInsere.listDisciplina.delete(tk.ACTIVE)
        self.limiteInsere.inputNota.delete(0, len(self.limiteInsere.inputNota.get()))

    def criaHistorico(self, event):
        nomeAluno = self.limiteInsere.escolhaAluno.get()
        aluno = self.controlePrincipal.ctrlAluno.getAluno(nomeAluno)
        ano = self.limiteInsere.inputAno.get()
        semestre = self.limiteInsere.comboboxSemestre.get()
        historico = Historico(aluno, self.listaDisciplinasHistorico, ano, semestre, self.listaNotaDisciplina)
        self.listaHistorico.append(historico)
        self.limiteInsere.mostraJanela('Sucesso', 'Historico criado')
        self.limiteInsere.destroy()
