import ply.yacc as yacc
import ply.lex as lex

from lex import tokens

import sys
import os.path

import string

class AnalisadorSintatico():
    def __init__(self):

        self.arquivo_entrada = "ProgramaKotlin_entrada.txt" #L�xico
        self.arquivo_saida = "ProgramaKotlin_saida.txt"		#Sint�tico

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

    def next_token (self):
        self.i += 1
        self.linha_atual = self.tokens[self.i] [self.tokens[self.i].find('\n'|';')+2: -1]
    def conteudo_token(self):
        return self.tokens[self.i][ : self.tokens[self.i].find('->')]

#Iniciar(kotlinFile -> (functionDeclaration* EOF)) 
    def start(self):
        if("Erro Lexico" in self.tokens[self.i]):
            self.i +=1
        self.FunctionDeclaration()
        if(self.tem_erro_sintatico):
            print("Verifique os erros sintaticos e tente compilar novamente")
            self.arquivo_saida.write("Verifique os erros sintaticos e tente compilar novamente\n")
        else:
            if("$" in self.tokens[self.i]):
                print("Cadeia de tokens na analise sintatica reconhecida com sucesso")
                self.arquivo_saida.write("Cadeia de tokens reconhecida com sucesso\n")
            else:
                print("Fim de Programa Nao Encontrado!")
                self.arquivo_saida.write("Fim de Programa Nao Encontrado!")
        self.arquivo_saida.close()
    def FunctionDeclaration (self):
        if("Erro Lexico" in self.tokens[self.i]):
            self.i += 1
        if('NUMER' in self.tokens[self.i]):
            self.next_token()
        if('PLUS' in self.tokens[self.i]):
            self.next_token()
        if('MINUS' in self.tokens[self.i]):
            self.next_token()
        if('MULT' in self.tokens[self.i]):
            self.next_token() 
        if('DIVIDE' in self.tokens[self.i]):
            self.next_token() 
        if('LPAREN' in self.tokens[self.i]):
            self.next_token() 
        if('RPAREN' in self.tokens[self.i]):
            self.next_token() 
        if('IF' in self.tokens[self.i]):
            self.next_token() 
        if('IMPORT' in self.tokens[self.i]):
            self.next_token() 
        if('NULLABLE' in self.tokens[self.i]):
            self.next_token() 
        if('VAR' in self.tokens[self.i]):
            self.next_token() 
        if('VAL' in self.tokens[self.i]):
            self.next_token() 
        if('FUN' in self.tokens[self.i]):
            self.next_token() 
        if('STRING' in self.tokens[self.i]):
            self.next_token() 
        if('ARRAY' in self.tokens[self.i]):
            self.next_token() 
        if('OBJECT' in self.tokens[self.i]):
            self.next_token() 
        if('THIS' in self.tokens[self.i]):
            self.next_token() 
        if('CHAR' in self.tokens[self.i]):
            self.next_token() 
        if('WHILE' in self.tokens[self.i]):
            self.next_token() 
        if('NULL' in self.tokens[self.i]):
            self.next_token() 
        if('WHEN' in self.tokens[self.i]):
            self.next_token() 
        if('FLOAT' in self.tokens[self.i]):
            self.next_token() 
        if('RETURN' in self.tokens[self.i]):
            self.next_token() 
        if('CONST' in self.tokens[self.i]):
            self.next_token() 
        if('OPERATOR' in self.tokens[self.i]):
            self.next_token() 
        if('INT' in self.tokens[self.i]):
            self.next_token() 
        if('CLASS' in self.tokens[self.i]):
            self.next_token() 
        if('CONSTRUCTOR' in self.tokens[self.i]):
            self.next_token() 
        if('DOUBLE' in self.tokens[self.i]):
            self.next_token() 
        if('SMARTCAST' in self.tokens[self.i]):
            self.next_token() 
        if('BOOLEAN' in self.tokens[self.i]):
            self.next_token() 
        if('FUNCTION' in self.tokens[self.i]):
            self.next_token() 
        if('FOR' in self.tokens[self.i]):
            self.next_token() 
        if('FALSE' in self.tokens[self.i]):
            self.next_token() 
        if('MOD' in self.tokens[self.i]):
            self.next_token() 
        if('PLUSPLUS' in self.tokens[self.i]):
            self.next_token()
        if('DECREMENTO' in self.tokens[self.i]):
            self.next_token()
        if('ATRIBUICAO' in self.tokens[self.i]):
            self.next_token()
        if('IGUALDADE' in self.tokens[self.i]):
            self.next_token()
        if('DIFERENTE' in self.tokens[self.i]):
            self.next_token()
        if('NOT' in self.tokens[self.i]):
            self.next_token()
        if('MENORIGUAL' in self.tokens[self.i]):
            self.next_token()
        if('MAIORIGUAL' in self.tokens[self.i]):
            self.next_token()
        if('MAIOR' in self.tokens[self.i]):
            self.next_token()
        if('MENOR' in self.tokens[self.i]):
            self.next_token()
        if('AND' in self.tokens[self.i]):
            self.next_token()
        if('OR' in self.tokens[self.i]):
            self.next_token()
        if('LCHAVE' in self.tokens[self.i]):
            self.next_token()
        if('RCHAVE' in self.tokens[self.i]):
            self.next_token()
        if('TRUE'in self.tokens[self.i]):
            self.next_token()
        if('ELSE' in self.tokens[self.i]):
            self.next_token()
        if('IDENT' in self.tokens[self.i]):
            self.next_token()
        if('DEDENT' in self.tokens[self.i]):
            self.next_token()
        else:
            print("Erro sintatico na linha: " +self.linha_atual+"\n")