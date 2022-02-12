data = open("input.txt", "r")
dataNew = open("output3.txt", "w")
dataNewBuffer = list()
dataNew2 = open("target.txt", "w")
dataL=list()
for line in data:
    dataL.append(line)

def MOT(token):
    Table = {'ADD': '01', 'SUB': '02','MULT': '03', 'MOVER': '04','MOVEM': '05',
            'BC': '07', 'DIV': '06', 'COMP':'08', 'PRINT':'09', 'READ':'10'}
    for i in Table:
        if (token == i):
            return Table[token]
            break
    else:
        return -1

def Declarative(token):
    Table = {'DC': '01', 'DS': '02'}
    for i in Table:
        if (token == i):
            return Table[token]
            break
    else:
        return -1

def Register(token):
    Table = {'AREG': '01', 'BREG': '02','CREG': '03', 'DREG': '04'}
    for i in Table:
        if (token == i):
            return Table[token]
            break
    else:
        return -1

def POT(token):
    Table = {'START':'01', 'END':'02', 'LTORG': '05', 'ORIGIN': '03', 'EQU': '04'}
    if token in Table:
        return Table[token]
    else:
        return -1

symNo=0
symTable=dict()
symTable["No."] = []
symTable["Address"] = []
symTable["Symbol"] = []
def symbolTable(symNo, Address, Symbol):
    symTable["No."].append(symNo)
    symTable["Address"].append(Address)
    symTable["Symbol"].append(Symbol)

def checkS(word, word2):
    if word in symTable["Symbol"][::] and word2 == "DS":
        return 1
    # elif word in sTable["symbol"][::]:
    #     dataNew.write("(")
    #     dataNew.write("S")
    #     dataNew.write(",")
    #     dataNew.write(str(sT["symbol"].index(word)))
    #     dataNew.write(")")
    #     dataNew.write("\n")
    #     return 0
    else:
        return 0

def checkS2(word, word2):           #!!FOR DC!!
    if word in symTable["Symbol"][::] and word2 == "DC":
        return 1
    # elif word in sTable["symbol"][::]:
    #     dataNew.write("(")
    #     dataNew.write("S")
    #     dataNew.write(",")
    #     dataNew.write(str(sT["symbol"].index(word)))
    #     dataNew.write(")")
    #     dataNew.write("\n")
    #     return 0
    else:
        return 0


def checkIndex(dC):  # return  index of symbol
    for i in range(len(symTable["Symbol"])):
        if dC == symTable["Symbol"][i]:
            return i

def allocateAddressSymbol(n,Address,constant):
    symTable["Address"][n] = Address
    constant=constant[:-1]
    dataNew.write(" -"+"    "+" -"+"    "+constant)
    
    # return Address

lNo=0
lTable = dict()
lTable["No."] = []
lTable["Address"] = []
lTable["Literal"] = []
def literalTable(lNo, Address, Literal):
    lTable["No."].append(lNo)
    lTable["Address"].append(Address)
    lTable["Literal"].append(Literal)

def checkLiteralInLTable(token):
    if token in lTable["Literal"][::]:
        return 1
    else:
        return 0

poolTable = dict()
poolTabNo=0
poolTable["No."] = []

TableInc = dict()
TableInc["LC No"] = []
TableInc["Inst"] = []
def TII(LCNo, Inst):
    TableInc["LC No"].append(LCNo)
    TableInc["Inst"].append(Inst)

def checkTII(word):
    if word in TableInc["LC No"][::]:
        return 1
    # elif word in sTable["symbol"][::]:
    #     dataNew.write("(")
    #     dataNew.write("S")
    #     dataNew.write(",")
    #     dataNew.write(str(sT["symbol"].index(word)))
    #     dataNew.write(")")
    #     dataNew.write("\n")
    #     return 0
    else:
        return 0

def callLTORG(Address,poolTabNo):
    poolTable["No."].append(poolTabNo+1)
    firstcall=0
    i=0
    for i in range(poolTabNo, len(lTable["Literal"])):
        lTable["Address"][i] = Address
        if(firstcall):
            dataNew.write("\n")
            dataNew.write(Address)
            dataNew.write("    ")
        dataNew.write(" -"+"    "+" -"+"    ")
        dataNew.write(lTable["Literal"][i][2:-1])
        firstcall=1
        Address=str(int(Address)+1)
    return i + 1, Address

def ExecuteTII():
    dataNew.close()
    #print("Here")
    dataNEW=open("output3.txt", "r")
    for line in dataNEW:
        dataNewBuffer.append(line)
        #print(line,end="")

    print("\n")
    for line in dataNewBuffer:
        if (checkTII(line.split(" ")[0])):
            if(TableInc["Inst"][TableInc["LC No"].index(line.split(" ")[0])][0]!="="):
                line=line[:-1]+symTable["Address"][symTable["Symbol"].index(TableInc["Inst"][TableInc["LC No"].index(line.split(" ")[0])])]+"\n"
                dataNew2.write(line)
            else:
                line=line[:-1]+lTable["Address"][lTable["Literal"].index(TableInc["Inst"][TableInc["LC No"].index(line.split(" ")[0])])]+"\n"
                dataNew2.write(line)
            #line=line[:-1]+"Here\n"
            #dataNew2.write(line)
            #line=line+TableInc[line.split(" ")[0]]
        else:
            dataNew2.write(line)
    #print("Here")

def main():
    locationCounter=' - '
    initiateLoc=0
    EQUFlag=False
    LTORGFlag=False
    for line in dataL:
        dataNew.write("\n")
        dataNew.write(locationCounter+"    ")
        if(locationCounter!=' - '):
            locationCounter=str(int(locationCounter)+1)

        for token in line.split():
            if(POT(token)!=-1):
                if(POT(token)=='01'):
                    initiateLoc=1
                    dataNew.write(POT(token)+"    ")
                elif(POT(token)=='05'):
                    global poolTabNo
                    #print(locationCounter)
                    poolTabNo,locationCounter=callLTORG(str(int(locationCounter)-1),poolTabNo)
                    #dataNew.write(POT(token)+"    ")
                    LTORGFlag=True
                elif(POT(token)=='04'):
                    dataNew.write("No Code Generated")
                    continue
                elif(POT(token)=='03'):
                    dataNew.write("No Code Generated")
                    locationCounter=str(line.split(' ')[1])[:-1]
                    # initiateLoc=1
                    continue
                elif(POT(token)=='02'):
                    locationCounter=str(int(locationCounter)-1)
                    callLTORG(locationCounter,poolTabNo)
                    poolTable["No."].pop()
                    ExecuteTII()
            
            elif(token.isdigit()):
                if(initiateLoc):
                    locationCounter=token
                    dataNew.write(str(locationCounter)+"    ")
                    initiateLoc=0
                
                
            elif(MOT(token)!=-1):
                if(MOT(token)=="09"):
                    dataNew.write(MOT(token)+"    "+" -"+"    ")
                else:
                    dataNew.write(MOT(token)+"    ")
            
            elif(Register(token)!=-1):
                dataNew.write(Register(token)+"    ")
            
            elif(Declarative(token)!=-1):
                continue

            else:
                if (checkS(token, line.split(" ")[1])):  # Check similar copies of symbol
                    allocateAddressSymbol(checkIndex(token),str(int(locationCounter)-1),line.split(' ')[2])
                elif (checkS2(token, line.split(" ")[1])):  # Check similar copies of symbol
                    allocateAddressSymbol(checkIndex(token),str(int(locationCounter)-1),line.split(' ')[2])
                    #print(str(line.split(' ')[2]))
                    #dataNew.write("Here")
                elif (line.split(" ")[1]=='EQU'):
                    if(not EQUFlag):
                        EQUFlag=True
                        global symNo
                        # print("Here")
                        symbolTable(symNo+1," - ",line.split(" ")[0])
                        symTable["Address"][symTable['Symbol'].index(line.split(' ')[0])]=symTable['Address'][symTable['Symbol'].index(str(line.split(' ')[2])[:-1])]
                    
                else:
                    if(token[-1]==':'):
                        symNo=symNo+1
                        symbolTable(symNo,str(int(locationCounter)-1),token)
                    else:
                        TII(str(int(locationCounter)-1),token)
                        if(token[0]=='='):
                            if(checkLiteralInLTable(token)):
                                continue
                            else:
                                global lNo
                                lNo=lNo+1
                                literalTable(lNo,'-',token)
                                if(LTORGFlag):
                                    poolTable["No."].append(lNo)
                        else:
                            symNo=symNo+1
                            symbolTable(symNo,'-',token)
        
        
        EQUFlag=False


main()
dataNew2.write("\n\n\n")

import pandas as pd

dataNew2.write("Table of Incomplete Instructions\n")  # Print TII
tii = pd.DataFrame(TableInc)
tii = tii.to_string(index=False)
dataNew2.write(str(tii))
dataNew2.write("\n\n\n")

dataNew2.write("Literal Table\n")  # Print Literal Table
ltable = pd.DataFrame(lTable)
ltable = ltable.to_string(index=False)
dataNew2.write(str(ltable))
dataNew2.write("\n\n\n")

dataNew2.write("Symbol Table\n")  # Print Symbol Table
symtable = pd.DataFrame(symTable)
symtable = symtable.to_string(index=False)
dataNew2.write(str(symtable))
dataNew2.write("\n\n\n")

dataNew2.write("Pool Table\n")  # Print Pool Table
pt = pd.DataFrame(poolTable)
pt = pt.to_string(index=False)
# print(lt)
dataNew2.write(str(pt))

"""

A DS 3
LABEL EQU A
ORIGIN 500
L1 MULT CREG ='7'
B DC 10
MOVEM CREG ='7'
D DC 8
END

"""