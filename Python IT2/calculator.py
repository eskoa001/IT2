import re #regex pakken er nødvendig for re.split()
import operator #operator pakken hjelper med string to operator

#kan ikke neste parentes 

#legge til - tall

ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv,} #definer regneoperasjonene til tekst

def operator_sum(n1, oper, n2): #tar regneoperasjon og to tall som input og returner summen gitt regneoperasjon
    n1, n2 = float(n1), float(n2)
    return ops[oper](n1, n2) 

def clear_parentes(splitInput): #regner innholdet i parentser og fjerner dem
    for x in splitInput:   
        if '(' in splitInput:  
            startPos = splitInput.index('(')
            endPos = splitInput.index(')')
            temp = splitInput[startPos+1:endPos]
            tempSum = calculate(temp, stage2)
            del splitInput[startPos+1:endPos+1]
            splitInput[startPos] = tempSum[0]
    return splitInput

def exponential(splitInput): #regner ut ** operasjonene
    for x in splitInput:   
        if '^' in splitInput:
            pos = splitInput.index('^')
            tempsum = float(splitInput[pos-1])**float(splitInput[pos+1])
            del splitInput[pos-1]
            del splitInput[pos] #korrigert pga. del
            splitInput[pos-1] = tempsum
    return splitInput


def calculate(splitInput, stage2):  #calculate funksjonen skal kalkulere verdien av den splittede stringen ved hjelp av rekursjon og string manipulasjon
    i = 0 #iterator
    for x in splitInput: #legg til ^ og () 
        if x == '*' or x == '/' or  x == '+' and stage2 == True or x == '-' and stage2 == True: 
            tempsum = operator_sum(splitInput[i-1], x, splitInput[i+1])
            del splitInput[i-1]
            del splitInput[i] #korrigert pga. del
            splitInput[i-1] = tempsum #korrigert pga. 2 del
            calculate(splitInput, stage2)
        i += 1
        if i == len(splitInput)-1 and stage2 == False:
            stage2 = True
            calculate(splitInput, stage2)
    return splitInput

while(True):
    stage2 = False #regnerekkefølge + dette må fikses

    CalculatorInput = input("Calculator input: ") 

    CalculatorInput = CalculatorInput.replace("**", "^")  #erstatter '**' med ^ slik at jeg kan regne med potenser (grunnet string split)
    splitInput = re.split('([^0-9.])', CalculatorInput) #bruker string split med regex, som splitter alt innenfor regex verdien og beholder 'dividerne'

    while("" in splitInput):
        splitInput.remove("") 
        
    while(' ' in splitInput):
        splitInput.remove(' ')
    
    splitInput = clear_parentes(splitInput)

    stage2 = False #vet ikke om denne har noe å si men nå er den hvertfall her

    splitInput = exponential(splitInput)

    print(calculate(splitInput, stage2)[0])




