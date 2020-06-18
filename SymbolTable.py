symbolTable = []
INT = 'int'
FLOAT = 'float'
BOOL = 'boolean'
TYPE = 'type'
UNDEFINED = 'undefined'
PARAMS = 'params'
BINDABLE = 'bindable'
CONSTANTE = 'constante'
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

Number = [INT, FLOAT]
primitivos = [BYTE, SHORT, INT, LONG, UNDEFINED, BOOL]

def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope
    print(symbolTable)

def endScope():     
    global symbolTable     
    symbolTable = symbolTable[0:-1]
    print(symbolTable)

def addVar(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type}
    print(symbolTable)

def addVal(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: CONSTANTE, TYPE : type}
    print(symbolTable)

def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE : returnType}
    print(symbolTable)

def getBindable(bindableName):     
    global symbolTable     
    for i in reversed(range(len(symbolTable))):         
        if (bindableName in symbolTable[i].keys()):             
            return symbolTable[i][bindableName]     
    return None

