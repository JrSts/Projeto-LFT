import ply.yacc as yacc
import ply.lex as lex

from ExpressionLanguageLex import tokens
from ConcretaClass import  *

import sys
import os.path

import string

class AnalisadorSintatico():
	def __init__(self):
    
    self.arquivo_entrada = "ProgramaKotlin_entrada.txt" #Léxico
    self.arquivo_saida = "ProgramaKotlin_saida.txt"		#Sintático

	self.tem_erro_sintatico = False

	self.arquivo_saida = open(self.arquivo_saida, 'w')
    # Verifica se o arquivo de entrada existe no diretorio em questao
    if not os.path.exists(self.arquivo_entrada):
		print("Arquivo de entrada inexistente")
		self.arquivo_saida.write("Arquivo de entrada inexistente")
		return
	
	self.arquivo = open(self.arquivo_entrada, 'r')
    self.tokens = self.arquivo.readlines()
    self.arquivo.close()
    self.i = 0
    self.j = 0
    self.linha_atual = ""

	
	'''
	# Definindo tabela de simbolos analise semantica
    self.registro_tab = {}
    self.constantes_tab = {}
    self.variaveis_globais_tab = {}
    self.funcoes_tab = {}
    self.algoritmo_tab = {}
	'''

	def next_token(self):
    self.i += 1
    self.linha_atual = self.tokens[self.i] [self.tokens[self.i].find('\n'|';')]

  def conteudo_token(self):
    return self.tokens[self.i][ : self.tokens[self.i].find('->')]

	