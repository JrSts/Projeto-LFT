symbolTable = []
INT = 'int'
FLOAT = 'float'
BOOL = 'boolean'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'function'
VARIABLE = 'variable'
SCOPE = 'scope'
FOR = 'for'
IF = 'if'
WHILE ='while'
VAR = 'var'
VAL = 'val'
FUN = 'fun'
NULL = 'null'
RETURN = 'return'
FALSE = 'false'
TRUE = 'true'
ELSE = 'else'
CONTINUE = 'continue'
DO = 'do'
IN = 'in'
IS = 'is'
BREAK = 'break'
NOT_IN = 'not_in'
NOT_IS = 'not_is'
AS = 'as'
DOUBLE = 'double'
LONG ='long'
STRING = 'string'
BYTE = 'byte'
SHORT = 'short'
PRINT = 'print'
PRINTLN = 'println'
SIM = 'sim'
NAO = 'nao'
USANDO ='use'
Number = [INT, FLOAT]
primitivos = [BYTE,SHORT,INT,LONG]

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope

def endScope():
    global symbolTable
    dictionarylist = []
    for x in symbolTable[-1]:
        if(type(symbolTable[-1][x]) == type({})):
            if (symbolTable[-1][x][USANDO] == NAO):
                dictionarylist.append(x)
    symbolTable = symbolTable[0:-1]
    return dictionarylist

def addVar(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type}

def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE : returnType}

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            symbolTable[i][bindableName][USANDO] = SIM
            return symbolTable[i][bindableName]
    return None