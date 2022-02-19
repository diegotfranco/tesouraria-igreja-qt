from datetime import datetime
from sys import argv
from ctypes import windll
import sqlite3

from pdfcore import *
from qtcore import *
from ui_main import Ui_MainWindow
from ui_dialog import Ui_Dialog, Ui_Dialog_2

class Overlay(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Window, Qt.transparent)
        self.setPalette(palette)
              
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(0, 0, 0, 127)))
        painter.end()


class Dialog(QDialog):
    def __init__(self, parent) -> None:
        super(Dialog, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        

class Dialog2(QDialog):
    def __init__(self, parent) -> None:
        super(Dialog2, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui = Ui_Dialog_2()
        self.ui.setupUi(self)


#TODO dimunir o tamanho do scroll dentro da main
class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()


		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.popup = Overlay(self)
		self.popup.setMinimumWidth(1920)
		self.popup.setMinimumHeight(1080)
		self.popup.hide()

		self.ui.tableWidget_membros.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.ui.tableWidget_membros.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

		self.ui.tableWidget_historico.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

		self.ui.tableWidget_entrada.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		self.ui.tableWidget_entrada.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

		self.ui.tableWidget_saida.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.ui.tableWidget_saida.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

		self.ui.tableWidget_lista_entrada.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

		self.ui.tableWidget_lista_saida.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
		self.ui.tableWidget_lista_saida.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)


		self.atualizaSaldoAnterior()
		self.atualizaPorcentagemDizimo()
		self.atualizaPorcentagemOfertas()
		
		self.showMaximized()
		self.show()

		##########################################################################
		#SINAIS DE CONTROLE
		self.ui.lineEdit_data_nasc.installEventFilter(self)
		self.ui.lineEdit_data_ref.installEventFilter(self)
		self.ui.lineEdit_data_dep.installEventFilter(self)
		self.ui.lineEdit_data_saida.installEventFilter(self)
		self.ui.lineEdit_financ_data_inicio.installEventFilter(self)
		self.ui.lineEdit_financ_data_fim.installEventFilter(self)
		self.ui.lineEdit_data_nasc.textChanged.connect(self.formataData)
		self.ui.lineEdit_data_ref.textChanged.connect(self.formataData)
		self.ui.lineEdit_data_dep.textChanged.connect(self.formataData)
		self.ui.lineEdit_data_saida.textChanged.connect(self.formataData)
		self.ui.lineEdit_financ_data_inicio.textChanged.connect(self.formataData)
		self.ui.lineEdit_financ_data_fim.textChanged.connect(self.formataData)
		#---------------------------------------------------------------#
		self.ui.lineEdit_cep.textEdited.connect(self.formataCep)
		self.ui.lineEdit_celular.textEdited.connect(self.formataCelular)
		#---------------------------------------------------------------#
		self.ui.tableWidget_membros.itemChanged.connect(self.atualizaMembros)
		self.ui.tableWidget_membros.keyPressEvent = self.deletaLinha
		#---------------------------------------------------------------#
		self.ui.comboBox_lista_entrada.currentIndexChanged.connect(self.listaEntrada)
		#---------------------------------------------------------------#
		self.ui.tableWidget_lista_entrada.itemChanged.connect(self.atualizaEntrada)
		self.ui.tableWidget_lista_entrada.keyPressEvent = self.deletaLinha
		#---------------------------------------------------------------#
		self.ui.comboBox_lista_saida.currentIndexChanged.connect(self.listaSaida)
		#---------------------------------------------------------------#
		self.ui.tableWidget_lista_saida.itemChanged.connect(self.atualizaSaida)
		self.ui.tableWidget_lista_saida.keyPressEvent = self.deletaLinha

		##########################################################################
		#BOTAO ENTRAR
		self.ui.pushButton_entrar.clicked.connect(self.verificaCredenciais)
		self.ui.lineEdit_senha_login.setEchoMode(QLineEdit.Password)
	
		##########################################################################
		#PAGINAS
		self.ui.pushButton_home.clicked.connect(self.atualizaPorcentagemDizimo)
		self.ui.pushButton_home.clicked.connect(self.atualizaPorcentagemOfertas)
		self.ui.pushButton_home.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.home))

		self.ui.pushButton_cadastro.clicked.connect(self.limpaCampos)
		self.ui.pushButton_cadastro.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.cadastro))

		self.ui.pushButton_membros.clicked.connect(self.limpaCampos)
		self.ui.pushButton_membros.clicked.connect(self.carregaMembros)
		self.ui.pushButton_membros.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.membros))

		self.ui.tableWidget_membros.doubleClicked.connect(self.historicoMembro)

		self.ui.pushButton_entradas.clicked.connect(self.limpaCampos)
		self.ui.pushButton_entradas.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.entradas))

		self.ui.pushButton_saidas.clicked.connect(self.limpaCampos)
		self.ui.pushButton_saidas.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.saidas))

		self.ui.pushButton_financeiro.clicked.connect(self.limpaCampos)
		self.ui.pushButton_financeiro.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.financeiro))
		
		##########################################################################
		#ATUALIZA AUTOCOMPLETAR
		self.atualizaAutocompletarMembros()
		self.atualizaAutocompletarEnderecos()
		self.atualizaAutocompletarCampanhas()
		self.atualizaAutocompletarDestinos()

		################################################################
		#BOTAO SAIR
		self.ui.pushButton_sair.clicked.connect(lambda: self.ui.inicio.setCurrentWidget(self.ui.login))

		################################################################
		#BOTAO SALVAR CADASTRO
		self.ui.btn_salvar_cadastro.clicked.connect(self.salvaInformacoesCadastro)

		################################################################
		#BOTAO BUSCA MEMBRO
		self.ui.toolButton_busca_membro.clicked.connect(self.carregaMembros)

		################################################################
		#BOTAO SALVAR ENTRADAS
		self.ui.btn_salvar_entrada.clicked.connect(self.salvaInformacoesEntrada)

		################################################################
		#BOTAO LISTA ENTRADAS
		self.ui.btn_visualizar_entrada.clicked.connect(self.limpaCampos)
		self.ui.btn_visualizar_entrada.clicked.connect(self.listaEntrada)

		################################################################
		#BOTAO EXTRA_ENTRADA
		self.ui.btn_extra.clicked.connect(self.extraEntrada)

		################################################################
		#BOTAO SALVAR SAIDAS
		self.ui.btn_salvar_saida.clicked.connect(self.salvaInformacoesSaida)

		################################################################
		#BOTAO LISTA SAIDAS
		self.ui.btn_visualizar_saida.clicked.connect(self.limpaCampos)
		self.ui.btn_visualizar_saida.clicked.connect(self.listaSaida)

		################################################################
		#BOTAO BUSCAR FINANCEIRO
		self.ui.pushButton_buscar_financeiro.clicked.connect(self.buscaDadosFinanceiro)

		################################################################
		#BOTAO VOLTAR FINANCEIRO
		self.ui.btn_voltar_financeiro.clicked.connect(self.limpaCampos)
		self.ui.btn_voltar_financeiro.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.financeiro))

		################################################################
		#BOTAO EXPORTAR FINANCEIRO
		self.ui.btn_exportar_pdf.clicked.connect(self.geraPDF)

	def limpaCampos(self):

		if self.ui.pages.currentWidget().objectName() == 'home':
			return
	
		if self.ui.pages.currentWidget().objectName() == 'financeiro':
			self.ui.frame_48.setMaximumHeight(0)
			print('entrei financeiro')
		else:
			for i in self.ui.pages.currentWidget().findChildren(QLabel)[1:]:
				i.clear()

		for i in self.ui.pages.currentWidget().findChildren(QLineEdit):
			i.clear()

		for i in self.ui.pages.currentWidget().findChildren(QComboBox):
			i.setCurrentIndex(0)

	def formataNumeroEntrada(self, cadeia):
		try:

			float(cadeia)
			return cadeia
		except ValueError:

			try:

				temp = cadeia
				cadeia = cadeia[:-3].replace('.', '') + cadeia[-3:]
				cadeia = cadeia[:-3] + cadeia[-3:].replace(',', '.')
				float(cadeia)
				return cadeia
			except ValueError:

				cadeia = temp
				cadeia = cadeia[3:]
				cadeia = cadeia[:-3].replace('.', '') + cadeia[-3:]
				cadeia = cadeia[:-3] + cadeia[-3:].replace(',', '.')
				try:

					float(cadeia)
					return cadeia
				except ValueError:

					msg = Dialog2(self)
					#msg.setWindowTitle('Ops, algo deu errado!')
					msg.ui.label.setText('Não foi possivel fazer esta alteração!')
					msg.ui.label_2.setText('O número parece ser inválido.')
					self.popup.show()
					msg.exec()
					self.popup.hide()
							

	def formataNumeroSaida(self, cadeia):

		for i in range(len(cadeia)-6, 3, -3):
			cadeia = cadeia[:i]+'.'+cadeia[i:]

		cadeia = cadeia[:-3] + cadeia[-3:].replace('.', ',')
		return cadeia

	def formataDataEntrada(self, cadeia):
		try:

			if len(cadeia) != 10:
				raise ValueError

			temp = cadeia.split('/')
			if len(temp[0]) < 2:
				temp[0] = '0'*(2-len(temp[0]))+temp[0]
			if len(temp[1]) < 2:
				temp[1] = '0'*(2-len(temp[1]))+temp[1]

			cadeia = '-'.join(temp[::-1])
			datetime.strptime(cadeia, '%Y-%m-%d')
			return cadeia
		except ValueError:
			
			msg = Dialog2(self)
			#msg.setWindowTitle('Ops, algo deu errado!')
			msg.ui.label.setText('Não foi possivel fazer esta alteração!')
			msg.ui.label_2.setText('A data parece ser inválida.')
			self.popup.show()
			msg.exec()
			self.popup.hide()

	def atualizaSaldoAnterior(self):

		try:
			query = f"select * from caixa where data = date('now', 'start of month')"
			cursor.execute(query)
			caixaMes = cursor.fetchone()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		if not caixaMes:
			try:
				query = f'''SELECT 			sum(dizimo),
											sum(doacao_terenos),
											sum(doacao_missoes),
											sum(doacao_pam),
											sum(doacao_campanha) 
										FROM (
												SELECT	data_referencia,
														dizimo,
														doacao_terenos,
														doacao_missoes,
														doacao_pam,
														doacao_campanha

												FROM entradas
												WHERE data_referencia
												BETWEEN date('now', 'start of month') AND date('now', 'start of month', '+1 month', '-1 day')
											)
										WHERE (dizimo != '' OR dizimo > 0) and 
											(doacao_terenos != '' or doacao_terenos > 0) and
											(doacao_missoes != '' or doacao_missoes > 0) and
											(doacao_pam != '' or doacao_pam > 0) and
											(doacao_campanha != '' or doacao_campanha > 0)'''
				cursor.execute(query)
				entrada = cursor.fetchone()

				query = f"SELECT sum(valor) FROM saidas WHERE data BETWEEN date('now', 'start of month') AND date('now', 'start of month', '+1 month', '-1 day')"
				
				cursor.execute(query)
				saida = cursor.fetchone()

				query = f'''SELECT saldo_anterior, caixa_terenos, sum(doacao_terenos) FROM caixa, entradas  
							WHERE (entradas.data_referencia BETWEEN date('now', 'start of month') AND date('now', 'start of month', '+1 month', '-1 day'))
							 AND (caixa.data BETWEEN date('now', 'start of month') AND date('now', 'start of month', '+1 month', '-1 day'))'''
				
				cursor.execute(query)
				caixa = cursor.fetchone()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return
			
			try:
				query = f"INSERT INTO caixa VALUES (date('now', '+1 month','start of month'), {sum(entrada)-saida[0]+caixa[0]:.2f}, {caixa[1]+caixa[2]:.2f})"
				cursor.execute(query)
				banco.commit()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
			


	def salvarArquivo(self):
		resposta = QFileDialog.getSaveFileName(parent= self, caption='Salvar como', filter='Todos Arquivos (*.*) ;; Documento PDF (*.pdf)', selectedFilter='Documento PDF (*.pdf)')
		return resposta[0]

	def buscaDadosFinanceiro(self):
		
		data_inicio = self.ui.validaData.validate(self.ui.lineEdit_financ_data_inicio.text(), 0)
		data_fim = self.ui.validaData.validate(self.ui.lineEdit_financ_data_fim.text(), 0)

		tudoOK = True
		if data_inicio[1] == '':
			self.ui.label_aviso_financ_data_inicio.setText('Campo Obrigatório!')
			tudoOK = False
		elif data_inicio[0] != QValidator.Acceptable:
			self.ui.label_aviso_financ_data_inicio.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_financ_data_inicio.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_financ_data_inicio.setText('')
		
		if data_fim[1] == '':
			self.ui.label_aviso_financ_data_fim.setText('Campo Obrigatório!')
			tudoOK = False
		elif data_fim[0] != QValidator.Acceptable:
			self.ui.label_aviso_financ_data_fim.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_financ_data_fim.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_financ_data_fim.setText('')
		
		if not tudoOK:
			return
		tipo = self.ui.comboBox_financeiro.currentText()
		
		if tipo == 'Entrada':
			try:
				query = f'''SELECT data_referencia,
 										sum(dizimo),
 										sum(doacao_terenos),
 										sum(doacao_missoes),
 										sum(doacao_pam),
 										sum(doacao_campanha) 
 									FROM (
 											SELECT	data_referencia,
 													dizimo,
 													doacao_terenos,
 													doacao_missoes,
 													doacao_pam,
 													doacao_campanha

 											FROM entradas
											WHERE data_referencia
											BETWEEN '{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}'
 										)
 									WHERE (dizimo != '' OR dizimo > 0) and 
 										(doacao_terenos != '' or doacao_terenos > 0) and
 										(doacao_missoes != '' or doacao_missoes > 0) and
 										(doacao_pam != '' or doacao_pam > 0) and
 										(doacao_campanha != '' or doacao_campanha > 0)
 										
 									GROUP BY data_referencia'''
				cursor.execute(query)
				entradas = cursor.fetchall()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return
		
			self.ui.tableWidget_entrada.setRowCount(len(entradas))
			for row, entrada in enumerate(entradas):
				for col, dado in enumerate(entrada):
					if col == 0:
						self.ui.tableWidget_entrada.setItem(row, col, QTableWidgetItem('/'.join(dado.split('-')[::-1])))
						self.ui.tableWidget_entrada.item(row, col).setTextAlignment(Qt.AlignCenter)
					else:
						self.ui.tableWidget_entrada.setItem(row, col, QTableWidgetItem(self.formataNumeroSaida(f'R$ {dado:.2f}')))
						self.ui.tableWidget_entrada.item(row, col).setTextAlignment(Qt.AlignCenter)

			v = 0 
			for i in range(0, len(entradas)):
				v +=  float(self.formataNumeroEntrada(self.ui.tableWidget_entrada.item(i, 1).text()))
			self.ui.total_financeiro_saida_1.setText(self.formataNumeroSaida(f'R$ {v:.2f}'))
			
			v = 0 
			for i in range(0, len(entradas)):
				v +=  float(self.formataNumeroEntrada(self.ui.tableWidget_entrada.item(i, 2).text()))
			self.ui.total_financeiro_saida_2.setText(self.formataNumeroSaida(f'R$ {v:.2f}'))

			v = 0 
			for i in range(0, len(entradas)):
				v +=  float(self.formataNumeroEntrada(self.ui.tableWidget_entrada.item(i, 3).text()))
			self.ui.total_financeiro_saida_3.setText(self.formataNumeroSaida(f'R$ {v:.2f}'))

			v = 0 
			for i in range(0, len(entradas)):
				v +=  float(self.formataNumeroEntrada(self.ui.tableWidget_entrada.item(i, 4).text()))
			self.ui.total_financeiro_saida_4.setText(self.formataNumeroSaida(f'R$ {v:.2f}'))

			v = 0 
			for i in range(0, len(entradas)):
				v +=  float(self.formataNumeroEntrada(self.ui.tableWidget_entrada.item(i, 5).text()))
			self.ui.total_financeiro_saida_5.setText(self.formataNumeroSaida(f'R$ {v:.2f}'))
			self.ui.pagFinanceiro.setCurrentWidget(self.ui.tabela_entrada)

		elif tipo == 'Saída':
			try:
				query = f'''SELECT data, destino, valor FROM saidas WHERE data BETWEEN 
							'{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}' order by data'''
				
				cursor.execute(query)
				saidas = cursor.fetchall()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return

			self.ui.tableWidget_saida.setRowCount(len(saidas))
			for row, saida in enumerate(saidas):
				for col, dado in enumerate(saida):
					if col == 0:
						self.ui.tableWidget_saida.setItem(row, col, QTableWidgetItem('/'.join(dado.split('-')[::-1])))
						self.ui.tableWidget_saida.item(row, col).setTextAlignment(Qt.AlignCenter)
					elif col == 1:
						self.ui.tableWidget_saida.setItem(row, col, QTableWidgetItem(dado))
						self.ui.tableWidget_saida.item(row, col).setTextAlignment(Qt.AlignLeft)
					else:
						self.ui.tableWidget_saida.setItem(row, col, QTableWidgetItem(self.formataNumeroSaida(f'R$ {dado:.2f}')))
						self.ui.tableWidget_saida.item(row, col).setTextAlignment(Qt.AlignCenter)
			
			v = 0 
			for i in range(0, len(saidas)):
				v +=  float(self.formataNumeroEntrada(self.ui.tableWidget_saida.item(i, 2).text()))
			self.ui.total_financeiro_saida.setText(self.formataNumeroSaida(f'R$ {v:.2f}'))

			self.ui.pagFinanceiro.setCurrentWidget(self.ui.tabela_saida)
		
		elif tipo == 'Entrada/Saída':
			try:
				query = f'''SELECT data_referencia,
 										sum(dizimo),
 										sum(doacao_terenos),
 										sum(doacao_missoes),
 										sum(doacao_pam),
 										sum(doacao_campanha) 
 									FROM (
 											SELECT	data_referencia,
 													dizimo,
 													doacao_terenos,
 													doacao_missoes,
 													doacao_pam,
 													doacao_campanha

 											FROM entradas
											WHERE data_referencia
											BETWEEN '{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}'
 										)
 									WHERE (dizimo != '' OR dizimo > 0) and 
 										(doacao_terenos != '' or doacao_terenos > 0) and
 										(doacao_missoes != '' or doacao_missoes > 0) and
 										(doacao_pam != '' or doacao_pam > 0) and
 										(doacao_campanha != '' or doacao_campanha > 0)
 										
 									GROUP BY data_referencia'''
				cursor.execute(query)
				entradas = cursor.fetchall()

				query = f'''SELECT data, destino, valor FROM saidas WHERE data BETWEEN 
							'{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}' order by data'''
				
				cursor.execute(query)
				saidas = cursor.fetchall()

				query = f'''SELECT saldo_anterior, caixa_terenos, sum(doacao_terenos) FROM caixa, entradas  where (entradas.data_referencia BETWEEN 
							'{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}') AND
				 			(caixa.data BETWEEN '{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}')'''
				
				cursor.execute(query)
				caixa = cursor.fetchall()[0]
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return
				
			d = 0 
			for i in range(0, len(entradas)):
				d += entradas[i][1]
			self.ui.label_22.setText(self.formataNumeroSaida(f'R$ {d:.2f}'))
			
			t = 0 
			for i in range(0, len(entradas)):
				t += entradas[i][2]
			self.ui.label_24.setText(self.formataNumeroSaida(f'R$ {t:.2f}'))

			m = 0 
			for i in range(0, len(entradas)):
				m += entradas[i][3]
			self.ui.label_26.setText(self.formataNumeroSaida(f'R$ {m:.2f}'))

			p = 0 
			for i in range(0, len(entradas)):
				p += entradas[i][4]
			self.ui.label_28.setText(self.formataNumeroSaida(f'R$ {p:.2f}'))

			c = 0 
			for i in range(0, len(entradas)):
				c += entradas[i][5]
			self.ui.label_30.setText(self.formataNumeroSaida(f'R$ {c:.2f}'))
			
			total_entrada = d+t+m+p+c
			self.ui.label_46.setText(self.formataNumeroSaida(f'R$ {total_entrada:.2f}'))

			total_saida = 0 
			for i in range(0, len(saidas)):
				total_saida += saidas[i][2]

			self.ui.label_34.setText(self.formataNumeroSaida(f'R$ {total_saida:.2f}'))

			self.ui.label_36.setText(self.formataNumeroSaida(f'R$ {caixa[0]:.2f}'))

			self.ui.label_38.setText(self.formataNumeroSaida(f'R$ {total_entrada-total_saida+caixa[0]:.2f}'))

			self.ui.label_40.setText(self.formataNumeroSaida(f'R$ {total_entrada-total_saida+caixa[0]-caixa[1]-caixa[2]:.2f}'))

			self.ui.label_42.setText(self.formataNumeroSaida(f'R$ {caixa[1]+caixa[2]:.2f}'))

			self.ui.pagFinanceiro.setCurrentWidget(self.ui.tabela_entrada_saida)
		
		self.ui.frame_48.setMaximumHeight(16777215)

	def geraPDF(self):
		
		data_inicio = self.ui.validaData.validate(self.ui.lineEdit_financ_data_inicio.text(), 0)
		data_fim = self.ui.validaData.validate(self.ui.lineEdit_financ_data_fim.text(), 0)

		tudoOK = True
		if data_inicio[1] == '':
			self.ui.label_aviso_financ_data_inicio.setText('Campo Obrigatório!')
			tudoOK = False
		elif data_inicio[0] != QValidator.Acceptable:
			self.ui.label_aviso_financ_data_inicio.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_financ_data_inicio.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_financ_data_inicio.setText('')
		
		if data_fim[1] == '':
			self.ui.label_aviso_financ_data_fim.setText('Campo Obrigatório!')
			tudoOK = False
		elif data_fim[0] != QValidator.Acceptable:
			self.ui.label_aviso_financ_data_fim.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_financ_data_fim.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_financ_data_fim.setText('')
		
		if not tudoOK:
			return
		
		try:
			query = f'''SELECT data_referencia,
									sum(dizimo),
									sum(doacao_terenos),
									sum(doacao_missoes),
									sum(doacao_pam),
									sum(doacao_campanha) 
								FROM (
										SELECT	data_referencia,
												dizimo,
												doacao_terenos,
												doacao_missoes,
												doacao_pam,
												doacao_campanha

										FROM entradas
										WHERE data_referencia
										BETWEEN '{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}'
									)
								WHERE (dizimo != '' OR dizimo > 0) and 
									(doacao_terenos != '' or doacao_terenos > 0) and
									(doacao_missoes != '' or doacao_missoes > 0) and
									(doacao_pam != '' or doacao_pam > 0) and
									(doacao_campanha != '' or doacao_campanha > 0)
									
								GROUP BY data_referencia'''
			cursor.execute(query)
			entradas = cursor.fetchall()
			
			query = f'''SELECT data, destino, sum(valor) FROM saidas WHERE data BETWEEN 
							'{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}' group by destino order by data '''	
			cursor.execute(query)
			saidas = cursor.fetchall()

			query = f'''SELECT saldo_anterior, caixa_terenos, sum(doacao_terenos) FROM caixa, entradas  where (entradas.data_referencia BETWEEN 
						'{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}') AND
						(caixa.data BETWEEN '{"-".join(data_inicio[1].split("/")[::-1])}' AND '{"-".join(data_fim[1].split("/")[::-1])}')'''
			cursor.execute(query)
			caixa = cursor.fetchall()[0]
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		d = 0 
		for i in range(0, len(entradas)):
			d += entradas[i][1]
		t = 0 
		for i in range(0, len(entradas)):
			t += entradas[i][2]
		m = 0 
		for i in range(0, len(entradas)):
			m += entradas[i][3]
		p = 0 
		for i in range(0, len(entradas)):
			p += entradas[i][4]
		c = 0 
		for i in range(0, len(entradas)):
			c += entradas[i][5]
		total_entrada = d+t+m+p+c

		for row, entrada in enumerate(entradas):
			temp = []
			for col, dado in enumerate(entrada):
				if col == 0:
					temp.append('/'.join(dado.split('-')[::-1]))
				else:
					temp.append(self.formataNumeroSaida(f'R$ {dado:.2f}'))
			entradas.pop(row)
			entradas.insert(row, temp)
		
		entradas.insert(0, ['Data', 'Dízimo', 'Terenos', 'Missões', 'P.A.M', 'Campanha'])
		entradas.append(['Total', self.formataNumeroSaida(f'R$ {d:.2f}'), self.formataNumeroSaida(f'R$ {t:.2f}'),
							self.formataNumeroSaida(f'R$ {m:.2f}'), self.formataNumeroSaida(f'R$ {p:.2f}'), self.formataNumeroSaida(f'R$ {c:.2f}')])
		entradas.insert(-1, ['', '', '', '', '', ''])

		total_saida = 0 
		for i in range(0, len(saidas)):
			total_saida += saidas[i][2]

		for row, saida in enumerate(saidas):
			temp = []
			for col, dado in enumerate(saida):
				if col == 0:
					temp.append('/'.join(dado.split('-')[::-1]))
				elif col == 2:
					temp.append(self.formataNumeroSaida(f'R$ {dado:.2f}'))
				else:
					temp.append(dado)
			saidas.pop(row)
			saidas.insert(row, temp)

		saidas.insert(0, ['Data', 'Destino', 'Valor'])

		pdf = PDF('P', 'mm', 'A4')
		pdf.alias_nb_pages()
		pdf.set_auto_page_break(auto=True, margin=30)
		pdf.add_page()
		pdf.set_font('Times', size = 12)
		pdf.create_table(table_data=entradas, title=f'Total Entrada: R${total_entrada:.2f}', cell_width='even', align_header= 'L',
						 align_data= 'L', x_start='C', emphasize_data=['Data', 'Dízimo', 'Terenos', 'Missões', 'P.A.M', 'Campanha'], emphasize_style='B')
		pdf.ln(10)
		pdf.create_table(table_data=saidas, title=f'Total Saida: R${total_saida:.2f}', cell_width=[((pdf.w-25)/10)*2, ((pdf.w-25)/10)*6, ((pdf.w-25)/10)*2], align_header= 'L',
						 align_data='L', x_start='C', emphasize_data=['Data', 'Destino', 'Valor'], emphasize_style='B')
		pdf.ln(10)
		detalhamento = [['**Saldo Anterior**:', '',self.formataNumeroSaida(f"R$ {caixa[0]:.2f}")], ['**Saldo p/ o próx. mês**:', '', self.formataNumeroSaida(f"R$ {total_entrada-total_saida+caixa[0]:.2f}")],
		['**Caixa Igreja**:', '',self.formataNumeroSaida(f"R$ {total_entrada-total_saida+caixa[0]-caixa[1]-caixa[2]:.2f}")], ['**Caixa Terenos**:', '',self.formataNumeroSaida(f"R$ {caixa[1]+caixa[2]:.2f}")]]
		pdf.create_table(table_data=detalhamento, title='Detalhamento do Caixa', cell_width=[((pdf.w-25)/10)*3, ((pdf.w-25)/10)*5, ((pdf.w-25)/10)*2], align_data='L', x_start='C', header= True)
		pdf.ln(25)
		pdf.cell(105, 12,'          __________________________________')
		pdf.cell(80, 12,'__________________________________')
		pdf.output(self.salvarArquivo())


	def atualizaPorcentagemDizimo(self):

		query = ['select* from dizimos', 'select nome from membros']
		try:
			cursor.execute(query[0])
			contribuintes = cursor.fetchall()
			cursor.execute(query[1])
			membros = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return
		
		contribuintes = [membro for membro in contribuintes if membro in membros]
		self.ui.label_10.setText(f'{(len(contribuintes)/len(membros))*100:.1f}%'.replace('.', ','))

	def atualizaPorcentagemOfertas(self):

		query = ['select* from ofertas', 'select nome from membros']
		try:
			cursor.execute(query[0])
			contribuintes = cursor.fetchall()
			cursor.execute(query[1])
			membros = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return
		
		contribuintes = [membro for membro in contribuintes if membro in membros]
		self.ui.label_13.setText(f'{(len(contribuintes)/len(membros))*100:.1f}%'.replace('.', ','))


	def eventFilter(self, source, event):

		if event.type() == QEvent.KeyPress and source in [self.ui.lineEdit_data_nasc, self.ui.lineEdit_data_ref, self.ui.lineEdit_data_dep,
		 													self.ui.lineEdit_data_saida, self.ui.lineEdit_financ_data_inicio, self.ui.lineEdit_financ_data_fim]:
			if event.key() == Qt.Key_Backspace and not source.hasSelectedText():
				
				pos = source.cursorPosition()
				txt = source.text()

				if pos >= 2 and txt[source.cursorPosition()-2] == '/':
					source.setText(txt[0:pos-2] + txt[pos:])
					source.setCursorPosition(pos-2)
				elif pos >= 1 and txt[source.cursorPosition()-1] != '/':
					source.setText(txt[0:pos-1] + txt[pos:])
					source.setCursorPosition(pos-1)
				else:
					source.setCursorPosition(pos)	
				return True	
				
			if event.key() == Qt.Key_Delete and not source.hasSelectedText():

				pos = source.cursorPosition()
				txt = source.text()
				tam = len(txt)

				if pos < tam-1 and txt[pos+1] == '/':
					source.setText(txt[:pos] + txt[pos+2:])
					source.setCursorPosition(pos)
				elif pos < tam and txt[pos] != '/':
					source.setText(txt[:pos] + txt[pos+1:])
					source.setCursorPosition(pos)
				else:
					source.setCursorPosition(pos)
				return True	
		return False

	def formataData(self, txt):
		
		current_widget = self.ui.pages.focusWidget()
		#print(current_widget)
		if current_widget in [self.ui.lineEdit_data_nasc, self.ui.lineEdit_data_ref, self.ui.lineEdit_data_dep,
								self.ui.lineEdit_data_saida, self.ui.lineEdit_financ_data_inicio, self.ui.lineEdit_financ_data_fim]:
			tam = len(txt)
			contBarra = txt.count('/')
			
			if (tam - contBarra) - contBarra < 1:
				current_widget.setText(txt.replace('/', ''))
			elif tam == 2 and contBarra == 0:
				current_widget.setText(txt[:2]+'/')
			elif tam == 4 and contBarra == 1:
				txt = txt.replace('/', '')
				current_widget.setText(txt[:2]+'/'+txt[2:])
			elif tam == 5 and contBarra == 1:
				current_widget.setText(txt[:5]+'/')

	def formataCep(self, txt):
		
		current_widget = self.ui.lineEdit_cep

		tam = len(txt)
		contBarra = txt.count('-')

		if tam == 5 and contBarra == 0:
			current_widget.setText(txt[:5]+'-')
		elif tam == 6 and contBarra == 1:
			current_widget.setText(txt[:5])
	
	def formataCelular(self, txt):
		
		current_widget = self.ui.lineEdit_celular
		tam = len(txt)
		contBarra = txt.count('-')
		contEspaco = txt.count(' ')

		if tam == 2 and contEspaco == 0:
			current_widget.setText(txt[:2]+' ')
		elif tam == 3 and contEspaco == 1:
			current_widget.setText(txt[:2])
		elif tam == 8 and contBarra == 0:
			current_widget.setText(txt[:8]+'-')
		elif tam == 9 and txt.index('-') - txt.index(' ') == 6:
			current_widget.setText(txt[:8])

	def atualizaAutocompletarDestinos(self):

		try:
			self.destinos = QCompleter([x[0] for x in cursor.execute("select distinct destino from saidas")])
			self.destinos.setCaseSensitivity(Qt.CaseInsensitive)
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		self.ui.lineEdit_destino_saida.setCompleter(self.destinos)

	def atualizaAutocompletarEnderecos(self):

		try:
			self.endereco = QCompleter([x[0] for x in cursor.execute("select distinct endereco from membros")])
			self.endereco.setCaseSensitivity(Qt.CaseInsensitive)
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		self.ui.lineEdit_endereco.setCompleter(self.endereco)

	def atualizaAutocompletarMembros(self):

		try:
			self.membros = QCompleter([x[0] for x in cursor.execute("select nome from membros")])
			self.membros.setCaseSensitivity(Qt.CaseInsensitive)
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		self.ui.lineEdit_nome_cad.setCompleter(self.membros)
		self.ui.lineEdit_nome_entrada.setCompleter(self.membros)
		self.ui.lineEdit_busca_membro.setCompleter(self.membros)

	def atualizaAutocompletarCampanhas(self):

		try:
			self.campanhas = QCompleter([x[0] for x in cursor.execute("select* from campanhas")])
			self.campanhas.setCaseSensitivity(Qt.CaseInsensitive)
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		self.ui.lineEdit_campanha_nome_entrada.setCompleter(self.campanhas)

	def extraEntrada(self):

		altura = self.ui.extra_entrada.height()

		if altura == 0:
			novaAltura = 100
		else:
			novaAltura = 0
		
		self.animation = QPropertyAnimation(self.ui.extra_entrada, b"maximumHeight")
		self.animation.setDuration(500)
		self.animation.setStartValue(altura)
		self.animation.setEndValue(novaAltura)
		self.animation.setEasingCurve(QEasingCurve.InOutQuart)
		self.animation.start()

	def listaEntrada(self):

		self.ui.tableWidget_lista_entrada.blockSignals(True)
		self.ui.meio_lista_entrada_2.setMaximumHeight(0)

		op = self.ui.comboBox_lista_entrada.currentIndex()

		if op == 0:		
			query = 'select rowid, * from entradas order by rowid desc limit 25'
		else:
			query = '''select rowid, * from entradas where data_referencia between 
						date('now', 'start of month') AND date('now', 'start of month', '+1 month', '-1 day') order by data_referencia'''

		try:
			cursor.execute(query)
			entradas = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		self.ui.tableWidget_lista_entrada.setRowCount(len(entradas))

		for row, entrada in enumerate(entradas):
			for col, dado in enumerate(entrada):
				if col == 0:
					self.ui.tableWidget_lista_entrada.setItem(row, col, QTableWidgetItem(str(dado)))
				elif col == 1 or col == 8 or col == 10:
					self.ui.tableWidget_lista_entrada.setItem(row, col, QTableWidgetItem(dado))
				elif col == 2 or col == 3:
					self.ui.tableWidget_lista_entrada.setItem(row, col, QTableWidgetItem('/'.join(dado.split('-')[::-1])))
					self.ui.tableWidget_lista_entrada.item(row, col).setTextAlignment(Qt.AlignCenter)
				else:
					if dado == '':
						dado = 0
					self.ui.tableWidget_lista_entrada.setItem(row, col, QTableWidgetItem(self.formataNumeroSaida(f"R$ {dado:.2f}")))
					self.ui.tableWidget_lista_entrada.item(row, col).setTextAlignment(Qt.AlignCenter)
		self.ui.tableWidget_lista_entrada.setColumnHidden(0, True)

		if entradas:
			self.ui.meio_lista_entrada_2.setMaximumHeight(16777215)
		self.ui.tableWidget_lista_entrada.blockSignals(False)
		self.ui.pages.setCurrentWidget(self.ui.lista_entrada)

	def atualizaEntrada(self, item):

		match item.column():
			case 1:
				campo = item.text()
				query = f"update entradas set nome = '{campo}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
			case 2:
				campo = self.formataDataEntrada(item.text())
				query = f"update entradas set data_referencia = '{campo}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
			case 3:
				campo = self.formataDataEntrada(item.text())
				query = f"update entradas set data_deposito = '{campo}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
			case 4:
				campo = self.formataNumeroEntrada(item.text())
				query = f"update entradas set dizimo = '{float(campo)}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
			case 5:
				campo = self.formataNumeroEntrada(item.text())
				query = f"update entradas set doacao_terenos = '{float(campo)}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
			case 6:
				campo = self.formataNumeroEntrada(item.text())
				query = f"update entradas set doacao_missoes = '{float(campo)}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
			case 7:
				campo = self.formataNumeroEntrada(item.text())
				query = f"update entradas set doacao_pam = '{float(campo)}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
			case 8:
				campo = item.text()
				query = f"update entradas set campanha_nome = '{campo}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
			case 9:
				campo = self.formataNumeroEntrada(item.text())
				query = f"update entradas set doacao_campanha = '{float(campo)}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
			case 10:
				campo = item.text()
				query = f"update entradas set forma_pagamento = '{campo}' where rowid = {self.ui.tableWidget_lista_entrada.item(item.row(), 0).text()}"
		
		if not campo:
			msg = Dialog2(self)
			msg.ui.label.setText('Não foi possivel fazer esta alteração!')
			msg.ui.label_2.setText('O campo parece estar vazio.')
			self.popup.show()
			msg.exec()
			self.listaEntrada()
			self.popup.hide()
			return

		try:
			cursor.execute(query)
			banco.commit()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

	def carregaMembros(self):

		self.ui.tableWidget_membros.blockSignals(True)

		txt = self.ui.lineEdit_busca_membro.text()

		if txt == None:		
			query = 'select rowid, nome, celular, data_nascimento from membros order by nome asc'
		else:
			query = f'select rowid, nome, celular, data_nascimento from membros where nome like "%{txt}%" order by nome asc'

		try:
			cursor.execute(query)
			membros = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		self.ui.tableWidget_membros.setRowCount(len(membros))

		for row, membro in enumerate(membros):
			for col, dado in enumerate(membro):
				if col == 0:
					self.ui.tableWidget_membros.setItem(row, col, QTableWidgetItem(str(dado)))
				elif col == 1:
					self.ui.tableWidget_membros.setItem(row, col, QTableWidgetItem(dado))
				elif col == 2:
					self.ui.tableWidget_membros.setItem(row, col, QTableWidgetItem(dado))
					self.ui.tableWidget_membros.item(row, col).setTextAlignment(Qt.AlignCenter)
				else:
					self.ui.tableWidget_membros.setItem(row, col, QTableWidgetItem('/'.join(dado.split('-')[::-1])))
					self.ui.tableWidget_membros.item(row, col).setTextAlignment(Qt.AlignCenter)
		self.ui.tableWidget_membros.setColumnHidden(0, True)
		self.ui.tableWidget_membros.blockSignals(False)

	def atualizaMembros(self, item):

		match item.column():
			case 1:
				campo = item.text()
				query = f"update membros set nome = '{campo}' where rowid = '{self.ui.tableWidget_membros.item(item.row(), 0).text()}'"
			case 2:
				campo = item.text()
				query = f"update membros set celular = '{campo}' where rowid = '{self.ui.tableWidget_membros.item(item.row(), 0).text()}'"
			case 3:
				campo = self.formataDataEntrada(item.text())
				query = f"update membros set data_nascimento = '{campo}' where rowid = '{self.ui.tableWidget_membros.item(item.row(), 0).text()}'"
		
		if not campo:
			msg = Dialog2(self)
			msg.ui.label.setText('Não foi possivel fazer esta alteração!')
			msg.ui.label_2.setText('O campo parece estar vazio.')
			self.popup.show()
			msg.exec()
			self.carregaMembros()
			self.popup.hide()
			return
		
		try:
			cursor.execute(query)
			banco.commit()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

	def deletaLinha(self, event):

		if event.key() == Qt.Key_Delete:
			
			op = None

			if self.ui.pages.currentWidget().objectName() == 'membros':
				op = 0
				query = f'delete from membros where rowid = {self.ui.tableWidget_membros.item(self.ui.tableWidget_membros.currentRow(), 0).text()}'
			elif self.ui.pages.currentWidget().objectName() == 'lista_entrada':
				op = 1
				query = f'delete from entradas where rowid = {self.ui.tableWidget_lista_entrada.item(self.ui.tableWidget_lista_entrada.currentRow(), 0).text()}'
			elif self.ui.pages.currentWidget().objectName() == 'lista_saida':
				op = 2
				query = f'delete from saidas where rowid = {self.ui.tableWidget_lista_saida.item(self.ui.tableWidget_lista_saida.currentRow(), 0).text()}'
			
			msg = Dialog(self)
			#msg.setWindowTitle('Cuidado! Essa ação é irreversível!')
			msg.ui.label.setText('Você tem certeza')
			msg.ui.label_2.setText('que gostaria de excluir este item?')

			self.popup.show()
			if not msg.exec():
				self.popup.hide()
				return
			self.popup.hide()

			try:
				cursor.execute(query)
				banco.commit()
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
			
			if op == 0:
				self.ui.tableWidget_membros.removeRow(self.ui.tableWidget_membros.currentRow())
			elif op == 1:
				self.ui.tableWidget_lista_entrada.removeRow(self.ui.tableWidget_lista_entrada.currentRow())
			elif op == 2:
				self.ui.tableWidget_lista_saida.removeRow(self.ui.tableWidget_lista_saida.currentRow())
		
		return super().keyPressEvent(event)
		
		


	def historicoMembro(self):
		membro = self.ui.tableWidget_membros.item(self.ui.tableWidget_membros.selectedItems()[0].row(), 1).text()
		mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
		querys = [f'select * from total_janeiro where nome = "{membro}"',
				  f'select * from total_fevereiro where nome = "{membro}"',
				  f'select * from total_marco where nome = "{membro}"',
				  f'select * from total_abril where nome = "{membro}"',
				  f'select * from total_maio where nome = "{membro}"',
				  f'select * from total_junho where nome = "{membro}"',
				  f'select * from total_julho where nome = "{membro}"',
				  f'select * from total_agosto where nome = "{membro}"',
				  f'select * from total_setembro where nome = "{membro}"',
				  f'select * from total_outubro where nome = "{membro}"',
				  f'select * from total_novembro where nome = "{membro}"',
				  f'select * from total_dezembro where nome = "{membro}"']

		self.ui.tableWidget_historico.setRowCount(12)
		for row, query in enumerate(querys):	
			try:
				cursor.execute(query)
				doacoes = cursor.fetchall()
				if doacoes:
					doacoes = doacoes.pop()
				else:
					doacoes = [membro, 0.0, 0.0, 0.0, 0.0, 0.0]
			except sqlite3.Error as erro:
				print('Erro com o banco de dados: ', erro)
				return

			self.ui.tableWidget_historico.setItem(row, 0, QTableWidgetItem(mes[row]))
			for col, doacao in enumerate(doacoes[1:]):
				self.ui.tableWidget_historico.setItem(row, col+1, QTableWidgetItem(self.formataNumeroSaida(f"R$ {doacao:.2f}")))
				self.ui.tableWidget_historico.item(row, col+1).setTextAlignment(Qt.AlignCenter)

		self.ui.label_hist_nome_membro.setText(membro)
		self.ui.pages.setCurrentWidget(self.ui.hist_membros)

	def listaSaida(self):

		self.ui.tableWidget_lista_saida.blockSignals(True)
		self.ui.meio_lista_saida_2.setMaximumHeight(0)

		op = self.ui.comboBox_lista_saida.currentIndex()

		if op == 0:
			query = 'select rowid, data, destino, valor from saidas order by rowid desc limit 25'
		else:
			query = '''select rowid, data, destino, valor from saidas where data between 
						date('now', 'start of month') AND date('now', 'start of month', '+1 month', '-1 day') order by data'''

		try:
			cursor.execute(query)
			saidas = cursor.fetchall()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		self.ui.tableWidget_lista_saida.setRowCount(len(saidas))

		for row, saida in enumerate(saidas):
			for col, dado in enumerate(saida):
				if col == 0:
					self.ui.tableWidget_lista_saida.setItem(row, col, QTableWidgetItem(str(dado)))
				elif col == 1:
					self.ui.tableWidget_lista_saida.setItem(row, col, QTableWidgetItem('/'.join(dado.split('-')[::-1])))
					self.ui.tableWidget_lista_saida.item(row, col).setTextAlignment(Qt.AlignCenter)
				elif col == 2:
					self.ui.tableWidget_lista_saida.setItem(row, col, QTableWidgetItem(dado))
				else:
					if dado == '':
						dado = 0
					self.ui.tableWidget_lista_saida.setItem(row, col, QTableWidgetItem(self.formataNumeroSaida(f"R$ {dado:.2f}")))
					self.ui.tableWidget_lista_saida.item(row, col).setTextAlignment(Qt.AlignCenter)
		self.ui.tableWidget_lista_saida.setColumnHidden(0, True)
		
		if saidas:
			self.ui.meio_lista_saida_2.setMaximumHeight(16777215)
		self.ui.tableWidget_lista_saida.blockSignals(False)
		self.ui.pages.setCurrentWidget(self.ui.lista_saida)

	def atualizaSaida(self, item):

		match item.column():
			case 1:
				campo = self.formataDataEntrada(item.text())
				query = f"update saidas set data = '{campo}' where rowid = {self.ui.tableWidget_lista_saida.item(item.row(), 0).text()}"
			case 2:
				campo = item.text()
				query = f"update saidas set destino = '{campo}' where rowid = {self.ui.tableWidget_lista_saida.item(item.row(), 0).text()}"
			case 3:
				campo = self.formataNumeroEntrada(item.text())
				query = f"update saidas set valor = '{float(campo)}' where rowid = {self.ui.tableWidget_lista_saida.item(item.row(), 0).text()}"
		
		if not campo:
			msg = Dialog2(self)
			msg.ui.label.setText('Não foi possivel fazer esta alteração!')
			msg.ui.label_2.setText('O campo parece estar vazio.')
			self.popup.show()
			msg.exec()
			self.listaSaida()
			self.popup.hide()
			return

		try:
			cursor.execute(query)
			banco.commit()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

	def salvaInformacoesCadastro(self):

		nome = self.ui.validaNome.validate(self.ui.lineEdit_nome_cad.text(), 0)
		data = self.ui.validaData.validate(self.ui.lineEdit_data_nasc.text(), 0)
		endereco = self.ui.validaTexto.validate(self.ui.lineEdit_endereco.text(), 0)
		numero = self.ui.validaInteiro.validate(self.ui.lineEdit_numero.text(), 0)
		complemento = self.ui.validaTexto.validate(self.ui.lineEdit_complemento.text(), 0)
		bairro = self.ui.validaTexto.validate(self.ui.lineEdit_bairro.text(), 0)
		uf = self.ui.comboBox_uf.currentText()
		cidade = self.ui.validaTexto.validate(self.ui.lineEdit_cidade.text(), 0)
		cep = self.ui.validaCep.validate(self.ui.lineEdit_cep.text(), 0)
		email = self.ui.validaEmail.validate(self.ui.lineEdit_email_cadastro.text(), 0)
		celular = self.ui.validaTelefone.validate(self.ui.lineEdit_celular.text(), 0)
		diretoria = self.ui.comboBox_privilegios.currentText()

		tudoOK = True
		if nome[1] == '':
			self.ui.label_aviso_nome_cad.setText('Campo Obrigatório!')
			tudoOK = False
		elif nome[0] != QValidator.Acceptable:
			self.ui.label_aviso_nome_cad.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_nome_cad.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_nome_cad.setText('')

		if endereco[1] != '' and endereco[0] != QValidator.Acceptable:
			self.ui.label_aviso_cidade.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_endereco.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_endereco.setText('')

		if numero[1] != '' and numero[0] != QValidator.Acceptable:
			self.ui.label_aviso_numero.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_numero.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_numero.setText('')
		
		if complemento[1] != '' and complemento[0] != QValidator.Acceptable:
			self.ui.label_aviso_complemento.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_complemento.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_complemento.setText('')
		
		if bairro[1] != '' and bairro[0] != QValidator.Acceptable:
			self.ui.label_aviso_bairro.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_bairro.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_bairro.setText('')
		
		if cidade[1] != '' and cidade[0] != QValidator.Acceptable:
			self.ui.label_aviso_cidade.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_cidade.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_cidade.setText('')
		
		if cep[1] != '' and cep[0] != QValidator.Acceptable:
			self.ui.label_aviso_cep.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_cep.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_cep.setText('')
		
		if email[1] != '' and email[0] != QValidator.Acceptable:
			self.ui.label_aviso_email_cadastro.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_email_cadastro.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_email_cadastro.setText('')
		
		if celular[1] == '':
			self.ui.label_aviso_celular.setText('Campo Obrigatório!')
			tudoOK = False
		elif celular[0] != QValidator.Acceptable:
			self.ui.label_aviso_celular.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_celular.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_celular.setText('')
		
		if data[1] == '':
			self.ui.label_aviso_data_nasc.setText('Campo Obrigatório!')
			tudoOK = False
		elif data[0] != QValidator.Acceptable:
			self.ui.label_aviso_data_nasc.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_data_nasc.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_data_nasc.setText('')
		
		if not tudoOK:
			return

		args = (nome[1], '-'.join(data[1].split('/')[::-1]), endereco[1].lower(), numero[1], complemento[1].lower(), bairro[1].lower(), uf.upper(), cidade[1].lower(), cep[1], email[1].lower(), celular[1], diretoria)

		try:
			cursor.execute('INSERT INTO membros VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', args)
			banco.commit()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return
		
		msg = Dialog2(self)
		#msg.setWindowTitle('Ação concluída!')
		msg.ui.label.setText('Cadastro efetuado com sucesso.')
		self.popup.show()
		msg.exec()
		self.popup.hide()

		self.atualizaAutocompletarMembros()		
		self.limpaCampos()
	
	def salvaInformacoesEntrada(self):

		nome = self.ui.validaNome.validate(self.ui.lineEdit_nome_entrada.text(), 0)
		data_ref = self.ui.validaData.validate(self.ui.lineEdit_data_ref.text(), 0)
		data_dep = self.ui.validaData.validate(self.ui.lineEdit_data_dep.text(), 0)
		dizimo = self.ui.validaValor.validate(self.ui.lineEdit_dizimo_entrada.text(), 0)
		terenos = self.ui.validaValor.validate(self.ui.lineEdit_terenos_entrada.text(), 0)
		missoes = self.ui.validaValor.validate(self.ui.lineEdit_missoes_entrada.text(), 0)
		pam = self.ui.validaValor.validate(self.ui.lineEdit_pam_entrada.text(), 0)
		tipo = self.ui.comboBox_tipo_entrada.currentText()
		campanha = self.ui.validaTexto.validate(self.ui.lineEdit_campanha_nome_entrada.text(), 0)
		valor = self.ui.validaValor.validate(self.ui.lineEdit_campanha_valor_entrada.text(), 0)

		tudoOK = True
		if nome[1] == '':
			nome2 = 'Anônimo'
		elif nome[0] != QValidator.Acceptable:
			self.ui.label_aviso_nome_entrada.setText('Campo preenchido incorretamente!')
			tudoOK = False;
		else:
			nome2 = nome[1]
			self.ui.label_aviso_nome_entrada.setText('')
		
		if dizimo[1] != '' and dizimo[0] != QValidator.Acceptable:
			self.ui.label_aviso_dizimo_entrada.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_valor_saida.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_dizimo_entrada.setText('')
		
		if terenos[1] != '' and terenos[0] != QValidator.Acceptable:
			self.ui.label_aviso_terenos_entrada.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_terenos_entrada.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_terenos_entrada.setText('')
		
		if missoes[1] != '' and missoes[0] != QValidator.Acceptable:
			self.ui.label_aviso_missoes_entrada.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_missoes_entrada.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_missoes_entrada.setText('')

		if pam[1] != '' and pam[0] != QValidator.Acceptable:
			self.ui.label_aviso_pam_entrada.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_pam_entrada.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_pam_entrada.setText('')

		if campanha[1] == '' and valor [1] != '':
			self.ui.label_aviso_campanha_nome_entrada.setText('Campo Obrigatório!')
			tudoOK = False
		elif campanha[1] != '' and campanha[0] != QValidator.Acceptable:
			self.ui.label_aviso_campanha_nome_entrada.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_campanha_nome_entrada.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_campanha_nome_entrada.setText('')

		if valor[1] == '' and campanha [1] != '':
			self.ui.label_aviso_campanha_valor_entrada.setText('Campo Obrigatório!')
			tudoOK = False
		elif valor[1] != '' and valor[0] != QValidator.Acceptable:
			self.ui.label_aviso_campanha_valor_entrada.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_campanha_valor_entrada.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_campanha_valor_entrada.setText('')
		
		if data_ref[1] == '':
			self.ui.label_aviso_data_ref_entrada.setText('Campo Obrigatório!')
			tudoOK = False
		elif data_ref[0] != QValidator.Acceptable:
			self.ui.label_aviso_data_ref_entrada.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_data_ref.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_data_ref_entrada.setText('')
		
		if data_dep[1] == '' and self.ui.comboBox_tipo_entrada.currentIndex() != 1:
			self.ui.label_aviso_data_dep_entrada.setText('Campo Obrigatório!')
			tudoOK = False
		elif data_dep[1] != '' and data_dep[0] != QValidator.Acceptable:
			self.ui.label_aviso_data_dep_entrada.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_data_dep.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_data_dep_entrada.setText('')

		if dizimo[1] == '' and terenos[1] == '' and missoes[1] == '' and pam[1] == '' and valor[1] == '':
			self.ui.label_aviso_dizimo_entrada.setText('Preencha um dos campos!')
			self.ui.label_aviso_terenos_entrada.setText('Preencha um dos campos!')
			self.ui.label_aviso_missoes_entrada.setText('Preencha um dos campos!')
			self.ui.label_aviso_pam_entrada.setText('Preencha um dos campos!')
			self.ui.label_aviso_campanha_valor_entrada.setText('Preencha um dos campos!')
			tudoOK = False

		if not tudoOK:
			return

		args = (nome2, '-'.join(data_ref[1].split('/')[::-1]), '-'.join(data_dep[1].split('/')[::-1]), dizimo[1].replace(',', '.'),
				terenos[1].replace(',', '.'), missoes[1].replace(',', '.'), pam[1].replace(',', '.'), campanha[1].lower(), valor[1].replace(',', '.'), tipo)
		
		try:
			cursor.execute('INSERT INTO entradas VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', args)
			banco.commit()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return
		
		msg = Dialog2(self)
		#msg.setWindowTitle('Ação concluída!')
		msg.ui.label.setText('Entrada salva com sucesso.')

		self.popup.show()
		msg.exec()
		self.popup.hide()

		self.atualizaAutocompletarCampanhas()
		self.limpaCampos()
		
	def salvaInformacoesSaida(self):

		destino = self.ui.validaTexto.validate(self.ui.lineEdit_destino_saida.text(), 0)
		data = self.ui.validaData.validate(self.ui.lineEdit_data_saida.text(), 0)
		valor = self.ui.validaValor.validate(self.ui.lineEdit_valor_saida.text(), 0)
		
		tudoOK = True
		if destino[1] == '':
			self.ui.label_aviso_destino_saida.setText('Campo Obrigatório!')
			tudoOK = False
		elif destino[0] != QValidator.Acceptable:
			self.ui.label_aviso_destino_saida.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_destino_saida.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_destino_saida.setText('')
		
		if valor[1] == '':
			self.ui.label_aviso_valor_saida.setText('Campo Obrigatório!')
			tudoOK = False
		elif valor[0] != QValidator.Acceptable:
			self.ui.label_aviso_valor_saida.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_valor_saida.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_valor_saida.setText('')
		
		if data[1] == '':
			self.ui.label_aviso_data_ref_saida.setText('Campo Obrigatório!')
			tudoOK = False
		elif data[0] != QValidator.Acceptable:
			self.ui.label_aviso_data_ref_saida.setText('Campo preenchido incorretamente!')
			self.ui.lineEdit_data_saida.setText('')
			tudoOK = False
		else:
			self.ui.label_aviso_data_ref_saida.setText('')
			
		if not tudoOK:
			return

		args = (destino[1].lower(), valor[1].replace(',', '.'), '-'.join(data[1].split('/')[::-1]))

		try:
			cursor.execute('INSERT INTO saidas VALUES (?, ?, ?)', args)
			banco.commit()
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return

		msg = Dialog2(self)
		#msg.setWindowTitle('Ação concluída!')
		msg.ui.label.setText('Saída salva com sucesso.')
		self.popup.show()
		msg.exec()
		self.popup.hide()

		self.atualizaAutocompletarDestinos()
		self.limpaCampos()
		
	def deslogar(self):

		self.hide()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()

	def verificaCredenciais(self):

		nome = self.ui.lineEdit_email_login.text()
		senha = self.ui.lineEdit_senha_login.text()
		if len(nome) == 0 or len(senha) == 0:
			self.ui.label_avisos.setText('Por favor, preencha todos os campos!')
			return

		self.ui.lineEdit_email_login.setText('')
		self.ui.lineEdit_senha_login.setText('')			
		try:
			usuarios = cursor.execute('SELECT email, senha FROM usuarios')	
		except sqlite3.Error as erro:
			print('Erro com o banco de dados: ', erro)
			return
		for linha in usuarios:
			if linha[0] == nome and linha[1] == senha:
				self.ui.label_avisos.setText('')
				self.ui.inicio.setCurrentWidget(self.ui.main)
				return
			self.ui.label_avisos.setText('Usuário/senha inválidos!')



if __name__ == '__main__':

	myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
	windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	try:
		banco = sqlite3.connect('db\ibanje.db')
		cursor = banco.cursor()
	except sqlite3.Error as erro:
		print('Erro com o banco de dados: ', erro)

	app = QApplication(argv)
	app.setWindowIcon(QIcon('icons\church_black_48dp.svg'))

	window = MainWindow()
	app.exec()
	
	banco.close()
	

