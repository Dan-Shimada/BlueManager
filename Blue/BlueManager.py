from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL import ImageTk, Image
import os.path
import os
from locale import setlocale, LC_NUMERIC

setlocale(LC_NUMERIC, 'pt_BR')

root = Tk()
codmat_var = StringVar()
horario_var = StringVar()
cursomat_var = StringVar()
situacao_var = StringVar()
status_pag_var = StringVar()
forma_pag_var = StringVar()
path = 'C:\\BlueManager\\Blue\\dist\\Dados'

class Options:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title('Blue')

        self.main_fr = Frame(self.raiz)
        self.main_fr.grid(row=0, column=0)

        image = Image.open("Logo.png")
        photo = ImageTk.PhotoImage(image)

        logo_lbl = Label(self.main_fr, image=photo)
        logo_lbl.image = photo
        logo_lbl.grid(row=0, column=0)

        self.planilhaAluno = Button(self.main_fr, bg='#015DA8', fg='#FFFFFF', pady=20, command=self.cabecalho_aluno,
                                    text='Criar planilha Aluno')
        self.planilhaAluno.grid(row=1, column=0, sticky='EW', columnspan=2)

        self.planilhaMatricula = Button(self.main_fr, bg='#015DA8', fg='#FFFFFF', pady=20,
                                        command=self.cabecalho_matricula, text='Criar planilha Matrícula')
        self.planilhaMatricula.grid(row=2, column=0, sticky='EW', columnspan=2)

        self.planilhaEscola = Button(self.main_fr, bg='#015DA8', fg='#FFFFFF', pady=20, command=self.cabecalho_escola,
                                     text='Criar planilha Escola')
        self.planilhaEscola.grid(row=3, column=0, sticky='EW', columnspan=2)

        self.planilhaFinanca = Button(self.main_fr, bg='#015DA8', fg='#FFFFFF', pady=20, command=self.cabecalho_financa,
                                      text='Criar planilha Financa')
        self.planilhaFinanca.grid(row=4, column=0, sticky='EW', columnspan=2)

        if os.path.isfile('{}\\Alunos.csv'.format(path)) and os.path.isfile('{}\\Alunos.csv'.format(path)) and os.path.isfile(
                '{}\\Cursos_Alunos.csv'.format(path)) and os.path.isfile('{}\\Escola.csv'.format(path)) and os.path.isfile('{}\\Financa.csv'.format(path)):
            self.planilhaAluno['state'] = DISABLED
            self.planilhaMatricula['state'] = DISABLED
            self.planilhaEscola['state'] = DISABLED
            self.planilhaFinanca['state'] = DISABLED
        else:
            self.planilhaAluno['state'] = NORMAL
            self.planilhaMatricula['state'] = NORMAL
            self.planilhaEscola['state'] = NORMAL
            self.planilhaFinanca['state'] = NORMAL

        self.cadastrarAlunos = Button(self.main_fr, bg='#015DA8', fg='#FFFFFF', pady=20, command=self.cadastrar_dados,
                                      text='Cadastrar dados')
        self.cadastrarAlunos.grid(row=5, column=0, sticky='EW', columnspan=2)

        self.alterarDados = Button(self.main_fr, bg='#015DA8', fg='#FFFFFF', pady=20, command=self.alterarDados,
                                   text='Alterar Dados')
        self.alterarDados.grid(row=6, column=0, sticky='EW', columnspan=2)

        self.excluirAluno = Button(self.main_fr,bg='#015DA8', fg='#FFFFFF', pady=20, command=self.excluirAluno,
                                   text='Excluir Aluno')
        self.excluirAluno.grid(row=7, column=0, sticky='EW', columnspan=2)

        self.close = Button(self.main_fr, bg='#E53737', fg='#FFFFFF', pady=20, command=self.fechar, text='Fechar')
        self.close.grid(row=8, column=0, sticky='EW', columnspan=2)

    def fechar(self):
        self.raiz.destroy()

    def cabecalho_aluno(self):
        lista_id_aluno = []
        lista_nome = []
        lista_nome_completo = []
        lista_endereco = []
        lista_numero = []
        lista_cidade = []
        lista_estado = []
        lista_data_Nascimento = []
        lista_nome_Responsavel = []

        cabecalho_Alunos = {
            'id': lista_id_aluno,
            'Nome': lista_nome,
            'Nome_completo': lista_nome_completo,
            'Endereco': lista_endereco,
            'Numero': lista_numero,
            'Cidade': lista_cidade,
            'Estado': lista_estado,
            'Data_Nascimento': lista_data_Nascimento,
            'Nome_Responsavel': lista_nome_Responsavel,
        }
        df_cabecalho_Alunos = pd.DataFrame(cabecalho_Alunos)
        df_cabecalho_Alunos.to_csv('{}\\Alunos.csv'.format(path), header=True, index=False,
                                   sep=';')

        self.planilhaAluno['state'] = DISABLED
        self.planilhaAluno['text'] = 'Planilha Aluno criado'

    def cabecalho_matricula(self):
        lista_Cod = []
        lista_Cursos = []
        lista_Horario = []
        lista_id_Aluno = []
        lista_P1 = []
        lista_P2 = []
        lista_P3 = []
        lista_P4 = []
        lista_Media = []
        lista_Situacao = []

        cabecalho_Curso_Alunos = {
            'Cod': lista_Cod,
            'Cursos': lista_Cursos,
            'Horario': lista_Horario,
            'id': lista_id_Aluno,
            'P1': lista_P1,
            'P2': lista_P2,
            'P3': lista_P3,
            'P4': lista_P4,
            'Media': lista_Media,
            'Situacao': lista_Situacao,
        }
        df_cabecalho_Cursos_Alunos = pd.DataFrame(cabecalho_Curso_Alunos)
        df_cabecalho_Cursos_Alunos.to_csv('{}\\Cursos_Alunos.csv'.format(path), header=True,
                                          index=False, sep=';')

        self.planilhaMatricula['state'] = DISABLED
        self.planilhaMatricula['text'] = 'Planilha Matricula Criada'

    def cabecalho_escola(self):
        lista_escolas = []
        lista_id_escola = []

        cabecalho_escola = {
            'ID_escola': lista_id_escola,
            'Escola': lista_escolas
        }

        df_cabecalho_escola = pd.DataFrame(cabecalho_escola)
        df_cabecalho_escola.to_csv('{}\\Escola.csv'.format(path), header=True, index=False,
                                   sep=';')

        self.planilhaEscola['state'] = DISABLED
        self.planilhaEscola['text'] = 'Planilha Escola Criada'

    def cabecalho_financa(self):
        lista_id_financa = []
        lista_formaPag = []
        lista_statusPag = []
        lista_vencimento = []
        lista_parcela = []

        cabecalho_financa = {
            'id': lista_id_financa,
            'FormaPagamento': lista_formaPag,
            'StatusPagamento': lista_statusPag,
            'DiaVencimento': lista_vencimento,
            'Parcela': lista_parcela
        }

        df_cabecalho_financas = pd.DataFrame(cabecalho_financa)
        df_cabecalho_financas.to_csv('{}\\Financa.csv'.format(path), header=True, index=False,
                                     sep=';')

        self.planilhaFinanca['state'] = DISABLED
        self.planilhaFinanca['text'] = 'Planilha Financa Criada'

    def cadastrar_dados(self):
        df_alunos = pd.read_csv('{}\\Alunos.csv'.format(path), sep=None, engine='python')

        self.cadastro_fr = Frame(self.main_fr, width=10, padx=20)
        self.cadastro_fr.grid(row=2, column=2, rowspan=5, sticky='NS')

        self.IDAlunolbl_lbl = Label(self.cadastro_fr, text='ID')
        self.IDAlunolbl_lbl.grid(row=0, column=0)
        self.IDAluno_ent = Entry(self.cadastro_fr, width=3)
        self.IDAluno_ent.insert(0,len(df_alunos.index) + 1)
        self.IDAluno_ent.grid(row=0, column=1, sticky='W')

        self.NomeAluno_lbl = Label(self.cadastro_fr, text='Primeiro    \nNome  ')
        self.NomeAluno_lbl.grid(row=0, column=2)
        self.NomeAluno_ent = Entry(self.cadastro_fr, width=10)
        self.NomeAluno_ent.grid(row=0, column=3)

        self.NomeCompleto_lbl = Label(self.cadastro_fr, text='Nome Completo  ')
        self.NomeCompleto_lbl.grid(row=0, column=4)
        self.NomeCompleto_ent = Entry(self.cadastro_fr, width=25)
        self.NomeCompleto_ent.grid(row=0, column=5, columnspan=3, sticky='EW')

        self.DataNascimento_lbl = Label(self.cadastro_fr, text='Data de\nNascimento')
        self.DataNascimento_lbl.grid(row=1, column=0)
        self.DataNascimento_ent = Entry(self.cadastro_fr, width=10)
        self.DataNascimento_ent.grid(row=1, column=1, sticky='EW')

        self.Endereco_lbl = Label(self.cadastro_fr, text='Endereco')
        self.Endereco_lbl.grid(row=1, column=2)
        self.Endereco_ent = Entry(self.cadastro_fr, width=35)
        self.Endereco_ent.grid(row=1, column=3, sticky='EW', columnspan=3)

        self.NumeroEndereco_lbl = Label(self.cadastro_fr, text='Nº   ')
        self.NumeroEndereco_lbl.grid(row=2, column=0, sticky='E')
        self.NumeroEndereco_ent = Entry(self.cadastro_fr, width=4)
        self.NumeroEndereco_ent.grid(row=2, column=1, sticky='W')

        self.Cidade_lbl = Label(self.cadastro_fr, text='Cidade')
        self.Cidade_lbl.grid(row=2, column=2)
        self.Cidade_ent = Entry(self.cadastro_fr)
        self.Cidade_ent.grid(row=2, column=3)

        self.Estado_lbl = Label(self.cadastro_fr, text='Estado  \n(SSP)  ')
        self.Estado_lbl.grid(row=2, column=4, sticky='E')
        self.Estado_ent = Entry(self.cadastro_fr, width=2)
        self.Estado_ent.grid(row=2, column=5, sticky='W')

        self.NomeResponsavel_lbl = Label(self.cadastro_fr, text='Responsavel')
        self.NomeResponsavel_lbl.grid(row=3, column=0)
        self.NomeResponsavel_ent = Entry(self.cadastro_fr, width=25)
        self.NomeResponsavel_ent.grid(row=3, column=1, columnspan=3, sticky='EW')

        self.CadastroAluno_btn = Button(self.cadastro_fr, width=15, command=self.CadastrarAluno, text='Salvar')
        self.CadastroAluno_btn.grid(row=4, column=4, pady=3, padx=10)

        self.PlanilhaMatricula_btn = Button(self.cadastro_fr, width=15, command=self.FormularioMatricula,
                                            text='Proximo')
        self.PlanilhaMatricula_btn.grid(row=4, column=5, pady=3, padx=10)

        self.alterarDados_fr.grid_forget()

    def FormularioMatricula(self):
        self.cadastro_fr.grid_forget()

        self.matricula_fr = Frame(self.main_fr, width=10, padx=20)
        self.matricula_fr.grid(row=2, column=2, rowspan=5, sticky='NS')

        self.id_aluno_mat_lbl = Label(self.matricula_fr, text='ID')
        self.id_aluno_mat_lbl.grid(row=0, column=0)
        self.id_aluno_mat_ent = Entry(self.matricula_fr, width=3)
        self.id_aluno_mat_ent.insert(0, self.IDAluno_ent.get())
        self.id_aluno_mat_ent.grid(row=0, column=1, sticky='W')

        self.cod_mat_lbl = Label(self.matricula_fr, text='Codigo')
        self.cod_mat_lbl.grid(row=0, column=2, sticky='E')
        self.cod_mat_cbbox = ttk.Combobox(self.matricula_fr, textvariable=codmat_var,
                                          values=('curso01', 'curso02', 'curso03'))
        self.cod_mat_cbbox.state(['readonly'])
        self.cod_mat_cbbox.current(0)
        self.cod_mat_cbbox.grid(row=0, column=3)

        self.curso_mat_lbl = Label(self.matricula_fr, text='Nivel  ')
        self.curso_mat_lbl.grid(row=0, column=4, sticky='E')
        self.curso_mat_cbbox = ttk.Combobox(self.matricula_fr, textvariable=cursomat_var,
                                            values=('Iniciante', 'Intermediario', 'Avancado'))
        self.curso_mat_cbbox.state(['readonly'])
        self.curso_mat_cbbox.current(0)
        self.curso_mat_cbbox.grid(row=0, column=5)

        self.horario_mat_lbl = Label(self.matricula_fr, text='Periodo')
        self.horario_mat_lbl.grid(row=1, column=0, sticky='E')
        self.horario_mat_cbbox = ttk.Combobox(self.matricula_fr, textvariable=horario_var,
                                              values=('Manha', 'Tarde', 'Noite'))
        self.horario_mat_cbbox.state(['readonly'])
        self.horario_mat_cbbox.current(0)
        self.horario_mat_cbbox.grid(row=1, column=1)

        self.p1_mat_lbl = Label(self.matricula_fr, text='P1  ')
        self.p1_mat_lbl.grid(row=2, column=0, sticky='E')
        self.p1_mat_ent = Entry(self.matricula_fr, width=5)
        self.p1_mat_ent.grid(row=2, column=1, sticky='W')

        self.p2_mat_lbl = Label(self.matricula_fr, text='P2  ')
        self.p2_mat_lbl.grid(row=2, column=2, sticky='E')
        self.p2_mat_ent = Entry(self.matricula_fr, width=5)
        self.p2_mat_ent.grid(row=2, column=3, sticky='W')

        self.p3_mat_lbl = Label(self.matricula_fr, text='P3  ')
        self.p3_mat_lbl.grid(row=3, column=0, sticky='E')
        self.p3_mat_ent = Entry(self.matricula_fr, width=5)
        self.p3_mat_ent.grid(row=3, column=1, sticky='W')

        self.p4_mat_lbl = Label(self.matricula_fr, text='P4  ')
        self.p4_mat_lbl.grid(row=3, column=2, sticky='E')
        self.p4_mat_ent = Entry(self.matricula_fr, width=5)
        self.p4_mat_ent.grid(row=3, column=3, sticky='W')

        self.media_mat_lbl = Label(self.matricula_fr, text='Media  ')
        self.media_mat_lbl.grid(row=4, column=0)
        self.media_mat_ent = Entry(self.matricula_fr, width=5)
        self.media_mat_ent.grid(row=4, column=1, sticky='W')

        self.situacao_mat_lbl = Label(self.matricula_fr, text='Situacao  ')
        self.situacao_mat_lbl.grid(row=4, column=2, sticky='E')
        self.situacao_mat_cbbox = ttk.Combobox(self.matricula_fr, textvariable=situacao_var,
                                               values=('Aprovado', 'Reprovado'))
        self.situacao_mat_cbbox.state(['readonly'])
        self.situacao_mat_cbbox.current(0)
        self.situacao_mat_cbbox.grid(row=4, column=3)

        self.CadastrarMatricula_btn = Button(self.matricula_fr, width=15, command=self.CadastrarMatricula,
                                             text='Salvar')
        self.CadastrarMatricula_btn.grid(row=5, column=4, pady=3, padx=10)

        self.PlanilhaFormulario_btn = Button(self.matricula_fr, width=15, command=self.FormularioEscola, text='Proximo')
        self.PlanilhaFormulario_btn.grid(row=5, column=5, pady=3, padx=10)

    def FormularioEscola(self):
        self.matricula_fr.grid_forget()

        self.escola_fr = Frame(self.main_fr, width=10, padx=20)
        self.escola_fr.grid(row=2, column=2, rowspan=5, sticky='NS')

        self.id_escola_lbl = Label(self.escola_fr, text='ID')
        self.id_escola_lbl.grid(row=0, column=0)
        self.id_escola_ent = Entry(self.escola_fr, width=3)
        self.id_escola_ent.insert(0, self.IDAluno_ent.get())
        self.id_escola_ent.grid(row=0, column=1, sticky='W')

        self.nome_escola_lbl = Label(self.escola_fr, text='Escola')
        self.nome_escola_lbl.grid(row=1, column=0)
        self.nome_escola_ent = Entry(self.escola_fr)
        self.nome_escola_ent.grid(row=1, column=1, sticky='EW')

        self.CadastrarEscola_btn = Button(self.escola_fr, width=15, command=self.CadastrarEscola, text='Salvar')
        self.CadastrarEscola_btn.grid(row=5, column=4, pady=3, padx=10)

        self.PlanilhaFinanca_btn = Button(self.escola_fr, width=15, command=self.FormularioFinanca, text='Proximo')
        self.PlanilhaFinanca_btn.grid(row=5, column=5, pady=3, padx=10)

    def FormularioFinanca(self):
        self.escola_fr.grid_forget()

        self.financa_fr = Frame(self.main_fr, width=10, padx=20)
        self.financa_fr.grid(row=2, column=2, rowspan=5, sticky='NS')

        self.id_financa_lbl = Label(self.financa_fr, text='ID')
        self.id_financa_lbl.grid(row=0, column=0, sticky='E')
        self.id_financa_ent = Entry(self.financa_fr, width=3)
        self.id_financa_ent.insert(0, self.IDAluno_ent.get())
        self.id_financa_ent.grid(row=0, column=1, sticky='W')

        self.forma_pag_lbl = Label(self.financa_fr, text='Forma de\nPagamento')
        self.forma_pag_lbl.grid(row=0, column=2, sticky='E')
        self.forma_pag_cbbox = ttk.Combobox(self.financa_fr, textvariable=forma_pag_var, values=(
        'Banco do Brasil', 'Bradesco', 'Itau', 'Santander', 'Sicredi', 'Transferencia'))
        self.forma_pag_cbbox.state(['readonly'])
        self.forma_pag_cbbox.current(0)
        self.forma_pag_cbbox.grid(row=0, column=3, sticky='W')

        self.dia_venc_lbl = Label(self.financa_fr, text='Vencimento')
        self.dia_venc_lbl.grid(row=1, column=0)
        self.dia_venc_ent = Entry(self.financa_fr, width=15)
        self.dia_venc_ent.grid(row=1, column=1, sticky='W')

        self.parcela_lbl = Label(self.financa_fr, text='Valor da\nParcela')
        self.parcela_lbl.grid(row=1, column=2, sticky='E')
        self.parcela_ent = Entry(self.financa_fr, width=15)
        self.parcela_ent.grid(row=1, column=3, sticky='W')

        self.status_pag_lbl = Label(self.financa_fr, text='Status do\nPagamento  ')
        self.status_pag_lbl.grid(row=2, column=0)
        self.status_pag_cbbox = ttk.Combobox(self.financa_fr, textvariable=status_pag_var, values=('Pago', 'Em Debito'))
        self.status_pag_cbbox.state(['readonly'])
        self.status_pag_cbbox.current(0)
        self.status_pag_cbbox.grid(row=2, column=1, sticky='W')

        self.CadastrarFinanca_btn = Button(self.financa_fr, width=15, command=self.CadastrarFinanca, text='Salvar')
        self.CadastrarFinanca_btn.grid(row=3, column=2, pady=3, padx=10)

        self.FimCadastro_btn = Button(self.financa_fr, width=15, command=self.FinalizarCadastro, text='Finalizar')
        self.FimCadastro_btn.grid(row=3, column=3, pady=3, padx=10)

    def FinalizarCadastro(self):
        self.financa_fr.grid_forget()

    def CadastrarAluno(self):
        self.CadastroAluno_btn['text'] = 'Salvo'

        lista_id_aluno_aux = []
        lista_nome_aux = []
        lista_nome_completo_aux = []
        lista_endereco_aux = []
        lista_numero_aux = []
        lista_cidade_aux = []
        lista_estado_aux = []
        lista_data_Nascimento_aux = []
        lista_nome_Responsavel_aux = []

        #
        lista_id_aluno_aux.append(self.IDAluno_ent.get())
        lista_nome_completo_aux.append(self.NomeCompleto_ent.get())
        lista_nome_aux.append(self.NomeAluno_ent.get())
        lista_data_Nascimento_aux.append(self.DataNascimento_ent.get())
        lista_endereco_aux.append(self.Endereco_ent.get())
        lista_numero_aux.append(self.NumeroEndereco_ent.get())
        lista_cidade_aux.append(self.Cidade_ent.get())
        lista_estado_aux.append(self.Estado_ent.get())
        lista_nome_Responsavel_aux.append(self.NomeResponsavel_ent.get())

        aluno = {
            'id': lista_id_aluno_aux,
            'Nome': lista_nome_aux,
            'Nome_completo': lista_nome_completo_aux,
            'Endereco': lista_endereco_aux,
            'Numero': lista_numero_aux,
            'Cidade': lista_cidade_aux,
            'Estado': lista_estado_aux,
            'Data_Nascimento': lista_data_Nascimento_aux,
            'Nome_Responsavel': lista_nome_Responsavel_aux
        }

        df = pd.DataFrame(aluno)
        df.to_csv('{}\\Alunos.csv'.format(path), header=False, index=False, sep=';', mode='a',
                  decimal=',')

    def CadastrarMatricula(self):
        self.CadastrarMatricula_btn['text'] = 'Salvo'

        lista_Cod_aux = []
        lista_Cursos_aux = []
        lista_Horario_aux = []
        lista_id_Aluno_aux = []
        lista_P1_aux = []
        lista_P2_aux = []
        lista_P3_aux = []
        lista_P4_aux = []
        lista_Media_aux = []
        lista_Situacao_aux = []

        if codmat_var.get() == 'curso01':
            lista_Cod_aux.append(self.cod_mat_cbbox['values'][0])
        elif codmat_var.get() == 'curso02':
            lista_Cod_aux.append(self.cod_mat_cbbox['values'][1])
        elif codmat_var.get() == 'curso03':
            lista_Cod_aux.append(self.cod_mat_cbbox['values'][2])

        if cursomat_var.get == None:
            pass
        elif cursomat_var.get() == 'Iniciante':
            lista_Cursos_aux.append(self.curso_mat_cbbox['values'][0])
        elif cursomat_var.get() == 'Intermediario':
            lista_Cursos_aux.append(self.curso_mat_cbbox['values'][1])
        elif cursomat_var.get() == 'Avancado':
            lista_Cursos_aux.append(self.curso_mat_cbbox['values'][2])

        if horario_var.get() == None:
            pass
        elif horario_var.get() == 'Manha':
            lista_Horario_aux.append(self.horario_mat_cbbox['values'][0])
        elif horario_var.get() == 'Tarde':
            lista_Horario_aux.append(self.horario_mat_cbbox['values'][1])
        elif horario_var.get() == 'Noite':
            lista_Horario_aux.append(self.horario_mat_cbbox['values'][2])

        lista_id_Aluno_aux.append(self.id_aluno_mat_ent.get())
        lista_P1_aux.append(self.p1_mat_ent.get())
        lista_P2_aux.append(self.p2_mat_ent.get())
        lista_P3_aux.append(self.p3_mat_ent.get())
        lista_P4_aux.append(self.p4_mat_ent.get())
        lista_Media_aux.append(self.media_mat_ent.get())

        if situacao_var.get() == 'Aprovado':
            lista_Situacao_aux.append(self.situacao_mat_cbbox['values'][0])
        elif situacao_var.get() == 'Reprovado':
            lista_Situacao_aux.append(self.situacao_mat_cbbox['values'][1])

        Matricula = {
            'Cod': lista_Cod_aux,
            'Cursos': lista_Cursos_aux,
            'Horario': lista_Horario_aux,
            'id_Aluno': lista_id_Aluno_aux,
            'P1': lista_P1_aux,
            'P2': lista_P2_aux,
            'P3': lista_P3_aux,
            'P4': lista_P4_aux,
            'Media': lista_Media_aux,
            'Situacao': lista_Situacao_aux
        }

        df = pd.DataFrame(Matricula)
        df.to_csv('{}\\Cursos_Alunos.csv'.format(path), header=False, index=False, sep=';',
                  mode='a', decimal=',')

    def CadastrarEscola(self):
        self.CadastrarEscola_btn['text'] = 'Salvo'

        lista_escola_aux = []
        lista_id_escola_aux = []

        lista_id_escola_aux.append(self.id_escola_ent.get())
        lista_escola_aux.append(self.nome_escola_ent.get())

        Escola = {
            'ID_escola': lista_id_escola_aux,
            'Escola': lista_escola_aux
        }

        df = pd.DataFrame(Escola)
        df.to_csv('{}\\Escola.csv'.format(path), header=False, index=False, sep=';', mode='a', decimal=',')

    def CadastrarFinanca(self):
        self.CadastrarFinanca_btn['text'] = 'Salvo'

        lista_id_financa_aux = []
        lista_formaPag_aux = []
        lista_statusPag_aux = []
        lista_vencimento_aux = []
        lista_parcela_aux = []

        lista_id_financa_aux.append(self.id_financa_ent.get())

        if forma_pag_var.get() == 'Banco do Brasil':
            lista_formaPag_aux.append(self.forma_pag_cbbox['values'][0])
        elif forma_pag_var.get() == 'Bradesco':
            lista_formaPag_aux.append(self.forma_pag_cbbox['values'][1])
        elif forma_pag_var.get() == 'Itau':
            lista_formaPag_aux.append(self.forma_pag_cbbox['values'][2])
        elif forma_pag_var.get() == 'Santander':
            lista_formaPag_aux.append(self.forma_pag_cbbox['values'][3])
        elif forma_pag_var.get() == 'Sicredi':
            lista_formaPag_aux.append(self.forma_pag_cbbox['values'][4])
        elif forma_pag_var.get() == 'Transferencia':
            lista_formaPag_aux.append(self.forma_pag_cbbox['values'][5])

        if status_pag_var.get() == 'Pago':
            lista_statusPag_aux.append(self.status_pag_cbbox['values'][0])
        elif status_pag_var.get() == 'Em Debito':
            lista_statusPag_aux.append(self.status_pag_cbbox['values'][1])

        lista_vencimento_aux.append(self.dia_venc_ent.get())
        lista_parcela_aux.append(self.parcela_ent.get())

        Financa = {
            'ID_financa': lista_id_financa_aux,
            'FormaPagamento': lista_formaPag_aux,
            'StatusPagamento': lista_statusPag_aux,
            'DiaVencimento': lista_vencimento_aux,
            'Parcela': lista_parcela_aux
        }

        df = pd.DataFrame(Financa)
        df.to_csv('{}\\Financa.csv'.format(path), header=False, index=False, sep=';', mode='a', decimal=',')

    def alterarDados(self):
        self.alterarDados_fr = Frame(self.main_fr, width=10, padx=20)
        self.alterarDados_fr.grid(row=1, column=2, rowspan=6, sticky='NS')

        self.pesquisa_ent = Entry(self.alterarDados_fr)
        self.pesquisa_ent.insert(0, 'ID')
        self.pesquisa_ent.grid(row=0, column=0, pady=5, padx=10)

        self.pesquisa_btn = Button(self.alterarDados_fr, text='Pesquisar', command=self.pesquisaAluno)
        self.pesquisa_btn.grid(row=0, column=1, pady=5, padx=10)

        self.listarAlunos_btn = Button(self.alterarDados_fr, text='Listar Alunos', command=self.listarAlunos)
        self.listarAlunos_btn.grid(row=0, column=2, pady=5, padx=10)

        self.alunosEmDebito_btn = Button(self.alterarDados_fr, text='Listar Debitos', command=self.listarDebito)
        self.alunosEmDebito_btn.grid(row=0, column=3, pady=5, padx=10)

        self.cadastro_fr.grid_forget()

    def listarAlunos(self):
        listar_dados = Toplevel(root)
        listar_dados.iconbitmap('Logo_BlueB.ico')
        ListarDados(listar_dados)
        listar_dados.mainloop()

    def listarDebito(self):
        listar_debito = Toplevel(root)
        listar_debito.iconbitmap('Logo_BlueB.ico')
        ListarDebito(listar_debito)
        listar_debito.mainloop()

    def pesquisaAluno(self):
        df_matricula = pd.read_csv('{}\\Cursos_Alunos.csv'.format(path), sep=None, engine='python')
        df_financa = pd.read_csv('{}\\Financa.csv'.format(path), sep=None, engine='python')

        self.p1Atual_lbl = Label(self.alterarDados_fr, text='P1 atual: ')
        self.p1Atual_lbl.grid(row=2, column=0, sticky='W')
        self.p1Atual_lbl2 = Label(self.alterarDados_fr, text=df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P1'], bg='white')
        self.p1Atual_lbl2.grid(row=2, column=0)

        self.atualiza1_btn = Button(self.alterarDados_fr, text='Atualizar', command=self.atualizaP1)
        self.atualiza1_btn.grid(row=2, column=0, sticky='E')

        self.p2Atual_lbl = Label(self.alterarDados_fr, text='P2 atual: ')
        self.p2Atual_lbl.grid(row=3, column=0, sticky='W')
        self.p2Atual_lbl2 = Label(self.alterarDados_fr, text=df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P2'], bg='white')
        self.p2Atual_lbl2.grid(row=3, column=0)

        self.atualiza2_btn = Button(self.alterarDados_fr, text='Atualizar', command=self.atualizaP2)
        self.atualiza2_btn.grid(row=3, column=0, sticky='E')

        self.p3Atual_lbl = Label(self.alterarDados_fr, text='P3 atual: ')
        self.p3Atual_lbl.grid(row=4, column=0, sticky='W')
        self.p3Atual_lbl2 = Label(self.alterarDados_fr, text=df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P3'], bg='white')
        self.p3Atual_lbl2.grid(row=4, column=0)

        self.atualiza3_btn = Button(self.alterarDados_fr, text='Atualizar', command=self.atualizaP3)
        self.atualiza3_btn.grid(row=4, column=0, sticky='E')

        self.p4Atual_lbl = Label(self.alterarDados_fr, text='P4 atual: ')
        self.p4Atual_lbl.grid(row=5, column=0, sticky='W')
        self.p4Atual_lbl2 = Label(self.alterarDados_fr, text=df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P4'], bg='white')
        self.p4Atual_lbl2.grid(row=5, column=0)

        self.atualiza4_btn = Button(self.alterarDados_fr, text='Atualizar', command=self.atualizaP4)
        self.atualiza4_btn.grid(row=5, column=0, sticky='E')

        self.StatusPagAtual_lbl = Label(self.alterarDados_fr, text='Pagamento:  ')
        self.StatusPagAtual_lbl.grid(row=2, column=3, sticky='W')
        self.StatusPagAtual_lbl2 = Label(self.alterarDados_fr, text=df_financa.loc[int(self.pesquisa_ent.get()) - 1, 'StatusPagamento'], bg='white')
        self.StatusPagAtual_lbl2.grid(row=2, column=4, sticky='E')

        self.atualizaPagAtual_btn = Button(self.alterarDados_fr, text='Atualizar', command=self.atualizaPag)
        self.atualizaPagAtual_btn.grid(row=2, column=5)

    def atualizaP1(self):
        self.p1Novo_lbl = Label(self.alterarDados_fr, text='P1 novo')
        self.p1Novo_lbl.grid(row=2, column=1)
        self.p1Novo_ent = Entry(self.alterarDados_fr, width=4)
        self.p1Novo_ent.grid(row=2, column=2, sticky='W')

        self.salvarNovoP1_btn = Button(self.alterarDados_fr, text='Salvar', command=self.salvarNovoDadoP1, width=7)
        self.salvarNovoP1_btn.grid(row=2, column=2, sticky='E')

    def atualizaP2(self):
        self.p2Novo_lbl = Label(self.alterarDados_fr, text='P2 novo')
        self.p2Novo_lbl.grid(row=3, column=1)
        self.p2Novo_ent = Entry(self.alterarDados_fr, width=4)
        self.p2Novo_ent.grid(row=3, column=2, sticky='W')

        self.salvarNovoP2_btn = Button(self.alterarDados_fr, text='Salvar', command=self.salvarNovoDadoP2, width=7)
        self.salvarNovoP2_btn.grid(row=3, column=2, sticky='E')

    def atualizaP3(self):
        self.p3Novo_lbl = Label(self.alterarDados_fr, text='P3 novo')
        self.p3Novo_lbl.grid(row=4, column=1)
        self.p3Novo_ent = Entry(self.alterarDados_fr, width=4)
        self.p3Novo_ent.grid(row=4, column=2, sticky='W')

        self.salvarNovoP3_btn = Button(self.alterarDados_fr, text='Salvar', command=self.salvarNovoDadoP3, width=7)
        self.salvarNovoP3_btn.grid(row=4, column=2, sticky='E')

    def atualizaP4(self):
        self.p4Novo_lbl = Label(self.alterarDados_fr, text='P4 novo')
        self.p4Novo_lbl.grid(row=5, column=1)
        self.p4Novo_ent = Entry(self.alterarDados_fr, width=4)
        self.p4Novo_ent.grid(row=5, column=2, sticky='W')

        self.salvarNovoP4_btn = Button(self.alterarDados_fr, text='Salvar', command=self.salvarNovoDadoP4, width=7)
        self.salvarNovoP4_btn.grid(row=5, column=2, sticky='E')

    def atualizaPag(self):
        self.statusPagNovo_lbl = Label(self.alterarDados_fr, text='Novo Pagamento')
        self.statusPagNovo_lbl.grid(row=3, column=3)
        self.statusPagNovo_ent = Entry(self.alterarDados_fr, width=10)
        self.statusPagNovo_ent.grid(row=3, column=4)

        self.salvarPagNovo_btn = Button(self.alterarDados_fr, text='Salvar', command=self.salvarPagNovo, width=7)
        self.salvarPagNovo_btn.grid(row=3, column=5)

    def salvarNovoDadoP1(self):
        self.salvarNovoP1_btn['text'] = 'Salvo'

        df_matricula = pd.read_csv('{}\\Cursos_Alunos.csv'.format(path), sep=None, engine='python')
        df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P1'] = self.p1Novo_ent.get()

        p1 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P1'].replace(',', '.'))
        p2 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P2'].replace(',', '.'))
        p3 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P3'].replace(',', '.'))
        p4 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P4'].replace(',', '.'))

        media = (p1 + p2 + p3 + p4) / 4
        df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Media'] = str(round(media,2)).replace('.',',')

        if media >= 7:
            df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Situacao'] = 'Aprovado'
        elif media < 7:
            df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Situacao'] = 'Reprovado'

        df_matricula.to_csv('{}\\Cursos_Alunos.csv'.format(path), sep=';', index=False, decimal=',')

        self.p1Novo_lbl.grid_forget()
        self.p1Novo_ent.grid_forget()
        self.salvarNovoP1_btn.grid_forget()

    def salvarNovoDadoP2(self):
        self.salvarNovoP2_btn['text'] = 'Salvo'

        df_matricula = pd.read_csv('{}\\Cursos_Alunos.csv'.format(path), sep=None, engine='python')
        df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P2'] = self.p2Novo_ent.get()

        p1 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P1'].replace(',', '.'))
        p2 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P2'].replace(',', '.'))
        p3 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P3'].replace(',', '.'))
        p4 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P4'].replace(',', '.'))

        media = (p1 + p2 + p3 + p4) / 4
        df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Media'] = str(round(media,2)).replace('.',',')

        if media >= 7:
            df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Situacao'] = 'Aprovado'
        elif media < 7:
            df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Situacao'] = 'Reprovado'

        df_matricula.to_csv('{}\\Cursos_Alunos.csv'.format(path), sep=';', index=False, decimal=',')

        self.p2Novo_lbl.grid_forget()
        self.p2Novo_ent.grid_forget()
        self.salvarNovoP2_btn.grid_forget()

    def salvarNovoDadoP3(self):
        self.salvarNovoP3_btn['text'] = 'Salvo'

        df_matricula = pd.read_csv('{}\\Cursos_Alunos.csv'.format(path), sep=None, engine='python')
        df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P3'] = self.p3Novo_ent.get()

        p1 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P1'].replace(',', '.'))
        p2 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P2'].replace(',', '.'))
        p3 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P3'].replace(',', '.'))
        p4 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P4'].replace(',', '.'))

        media = (p1 + p2 + p3 + p4) / 4
        df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Media'] = str(round(media,2)).replace('.',',')

        if media >= 7:
            df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Situacao'] = 'Aprovado'
        elif media < 7:
            df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Situacao'] = 'Reprovado'

        df_matricula.to_csv('{}\\Cursos_Alunos.csv'.format(path), sep=';', index=False, decimal=',')

        self.p3Novo_lbl.grid_forget()
        self.p3Novo_ent.grid_forget()
        self.salvarNovoP3_btn.grid_forget()

    def salvarNovoDadoP4(self):
        self.salvarNovoP4_btn['text'] = 'Salvo'

        df_matricula = pd.read_csv('{}\\Cursos_Alunos.csv'.format(path), sep=None, engine='python')
        df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P4'] = self.p4Novo_ent.get()

        p1 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P1'].replace(',', '.'))
        p2 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P2'].replace(',', '.'))
        p3 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P3'].replace(',', '.'))
        p4 = float(df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'P4'].replace(',', '.'))

        media = (p1 + p2 + p3 + p4) / 4
        df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Media'] = str(round(media,2)).replace('.',',')

        if media >= 7:
            df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Situacao'] = 'Aprovado'
        elif media < 7:
            df_matricula.loc[int(self.pesquisa_ent.get()) - 1, 'Situacao'] = 'Reprovado'

        df_matricula.to_csv('{}\\Cursos_Alunos.csv'.format(path), sep=';', index=False, decimal=',')

        self.p4Novo_lbl.grid_forget()
        self.p4Novo_ent.grid_forget()
        self.salvarNovoP4_btn.grid_forget()

    def salvarPagNovo(self):
        self.salvarPagNovo_btn['text'] = 'Salvo'

        df_financa = pd.read_csv('{}\\Financa.csv'.format(path), sep=None, engine='python')
        df_financa.loc[int(self.pesquisa_ent.get()) - 1, 'StatusPagamento'] = self.statusPagNovo_ent.get()
        df_financa.to_csv('{}\\Financa.csv'.format(path), sep=';', index=False, decimal=',')

        self.statusPagNovo_lbl.grid_forget()
        self.statusPagNovo_ent.grid_forget()
        self.salvarPagNovo_btn.grid_forget()

    def excluirAluno(self):
        self.excluirAluno_fr = Frame(self.main_fr, width=10, padx=20)
        self.excluirAluno_fr.grid(row=1, column=2, rowspan=6, sticky='NS')

        self.pesquisa2_ent = Entry(self.excluirAluno_fr)
        self.pesquisa2_ent.insert(0, 'ID')
        self.pesquisa2_ent.grid(row=0, column=0, pady=5, padx=10)

        self.pesquisa2_btn = Button(self.excluirAluno_fr, text='Deletar', command=self.DeletarAluno)
        self.pesquisa2_btn.grid(row=0, column=1, pady=5, padx=10)

        self.listarAlunos2_btn = Button(self.excluirAluno_fr, text='Listar Alunos', command=self.listarAlunos)
        self.listarAlunos2_btn.grid(row=0, column=2, pady=5, padx=10)

    def DeletarAluno(self):
        lista_del_index = []

        df_alunos = pd.read_csv('{}\\Alunos.csv'.format(path), sep=None, engine='python')
        df_matricula = pd.read_csv('{}\\Cursos_Alunos.csv'.format(path), sep=None, engine='python')
        df_escola = pd.read_csv('{}\\Escola.csv'.format(path), sep=None, engine='python')
        df_financa = pd.read_csv('{}\\Financa.csv'.format(path), sep=None, engine='python')

        lista_del_index.append(int(self.pesquisa2_ent.get()) - 1)

        # Remove a foto
        os.unlink('C:\\BlueManager\\Blue\\dist\\foto_aluno\\{}.jpeg'.format(df_alunos.loc[int(self.pesquisa2_ent.get()) - 1, 'Nome']))

        self.confirmaExclusao = Label(self.excluirAluno_fr, text='O aluno {} foi excluido'.format(df_alunos.loc[int(self.pesquisa2_ent.get()) - 1, 'Nome_completo']))
        self.confirmaExclusao.grid(row=1, column=0)

        # Dropa a linha desejada
        df_alunos.drop(lista_del_index[0], inplace=True)
        df_matricula.drop(lista_del_index[0], inplace=True)
        df_escola.drop(lista_del_index[0], inplace=True)
        df_financa.drop(lista_del_index[0], inplace=True)

        # Reseta index das planilhas
        df_alunos.reset_index(drop=True, inplace=True)
        df_matricula.reset_index(drop=True, inplace=True)
        df_escola.reset_index(drop=True, inplace=True)
        df_financa.reset_index(drop=True, inplace=True)

        df_alunos.to_csv('{}\\Alunos.csv'.format(path), sep=';', index=False, decimal=',')
        df_matricula.to_csv('{}\\Cursos_Alunos.csv'.format(path), sep=';', index=False, decimal=',')
        df_escola.to_csv('{}\\Escola.csv'.format(path), sep=';', index=False, decimal=',')
        df_financa.to_csv('{}\\Financa.csv'.format(path), sep=';', index=False, decimal=',')

        self.excluirAluno_fr.grid_forget()

class ListarDados():
    def __init__(self, exibir):
        self.exibir = exibir
        self.exibir.title('Listar Dados')

        self.listarDados_fr = Frame(self.exibir)
        self.listarDados_fr.grid(row=0, column=0, rowspan=4, columnspan=2)

        df_alunos = pd.read_csv('{}\\Alunos.csv'.format(path), sep=None, engine='python')
        df_matricula = pd.read_csv('{}\\Cursos_Alunos.csv'.format(path), sep=None, engine='python')

        lista_merge = pd.merge(df_alunos.iloc[:, [0, 2]], df_matricula.iloc[:, [3, 4, 5, 6, 7, 8, 9]], how='left',
                               on='id')

        self.exibeLista_lbl = Label(self.listarDados_fr, text=lista_merge)
        self.exibeLista_lbl.grid(row=1, column=1)

        self.ok_btn = Button(self.listarDados_fr, text='Ok', width=15, command=self.fecharLista)
        self.ok_btn.grid(row=3, column=1)

    def fecharLista(self):
        self.exibir.destroy()

class ListarDebito():
    def __init__(self, exibirDebito):
        self.exibirDebito = exibirDebito
        self.exibirDebito.title('Listar Debitos')

        self.listarDebito_fr = Frame(self.exibirDebito)
        self.listarDebito_fr.grid(row=0, column=0, rowspan=4, columnspan=2)

        df_alunos = pd.read_csv('{}\\Alunos.csv'.format(path), sep=None, engine='python')
        df_financa = pd.read_csv('{}\\Financa.csv'.format(path), sep=None, engine='python')

        df_listaDebito = pd.merge(df_alunos.iloc[:, [0, 2]], df_financa.iloc[:, [0, 1, 2, 3, 4]], how='left', on='id')

        self.exibeListaDebito_lbl = Label(self.listarDebito_fr, text=df_listaDebito)
        self.exibeListaDebito_lbl.grid(row=1, column=1)

        self.ok_btn = Button(self.listarDebito_fr, text='Ok', width=15, command=self.fecharListaDebito)
        self.ok_btn.grid(row=3, column=1)

    def fecharListaDebito(self):
        self.exibirDebito.destroy()

def main():
    Options(root)
    root.geometry('1024x620+400+200')
    root.iconbitmap('Logo_BlueB.ico')
    root.mainloop()

if __name__ == '__main__':
    main()

