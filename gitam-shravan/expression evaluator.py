
import time
import re
import keyword
from cStringIO import StringIO
from tokenize import generate_tokens
variables=[]
values=[]
key_words=keyword.kwlist


def regex():
    global simple_assi
    global numeric_assi
    global vari
    global num
    global parallel_assi
    global compound_assi

    op=r"[+|*|/|-]"
    v_n=r"([a-zA-Z]+|[0-9]*.[0-9]+|[0-9]+)"
    v_n_may=r"([a-zA-Z]+[0-9]*.[0-9]+|[0-9]+)*"
    mb=r"([+|*|/|-]([a-zA-Z]+|[0-9]*.[0-9]+|[0-9]+))*"
    br1=r"("+op+"[(]"+v_n+mb+"[)])*"
    br=r"([(]"+v_n+mb+br1+mb+"[)])*"
    op_br_may=r"("+op+br+")*"
    m=r"^[a-zA-Z]+[=]"+v_n_may+mb+op_br_may+mb+op_br_may+mb+"$"
    compound_assi=re.compile(m)
    simple_assi=re.compile(r"^[a-zA-Z]+[+|-|*|/]?=[a-zA-Z]+$")
    numeric_assi=re.compile(r"^[a-zA-Z]+[+|-|*|/]?=[+|-]?([0-9]*\.[0-9]+|[0-9]+)$")
    vari=re.compile(r"^[+-]?[a-zA-Z]+$")
    num=re.compile(r"^[+-]?([0-9]*.[0-9]+|[0-9]+)$")
    parallel_assi=re.compile(r"^[a-zA-Z]+(,[a-zA-Z]+)+=([0-9]*.[0-9]+|[0-9]+)(,[0-9]*.[0-9]+|,[0-9]+)+$")

def store(key,val):
    try:
        index=variables.index(key)
    except ValueError:
        variables.append(key)
        values.append(val)
    else:
        values[index]=val


def display():
    length=len(variables)
    i=0
    while i<length:
        print variables[i],"--->>",values[i]
        i+=1

def calculate(tokens):
    while '**' in tokens:
        index=tokens[::-1].index("**")
        tokens[index+1]=tokens[index-1]**tokens[index+1]
        del tokens[index-1:index+1]
    while '*' in tokens or '/' in tokens:
        if '*' in tokens:
            index1=tokens.index("*")
        else:
            index1=1000
        if '/' in tokens:
            index2=tokens.index("/")
        else:
            index2=1000
        print tokens
        print index1
        print index2
        if index1<index2:
            tokens[index1+1]=tokens[index1-1]*tokens[index1+1]
            del tokens[index1-1:index1+1]
        else:
            tokens[index2+1]=tokens[index2-1]/tokens[index2+1]
            del tokens[index2-1:index2+1]
    while '+' in tokens or '-' in tokens:
        if '+' in tokens:
            index1=tokens.index("+")
        else:
            index1=1000
        if '-' in tokens:
            index2=tokens.index("-")
        else:
            index2=1000
        if index1==0:
            return(tokens[1])
        if index2==0:
            return(tokens[1]*-1)
        if index1<index2:
            print tokens
            tokens[index1+1]=tokens[index1-1]+tokens[index1+1]
            del tokens[index1-1:index1+1]
        else:
            tokens[index2+1]=tokens[index2-1]-tokens[index2+1]
            del tokens[index2-1:index2+1]
    return tokens[0]

def assignment(tokens):
    operators=['**','*','/','+','-','=']
    paranthesis=['(',')']
    i=0
    length=len(tokens)
    while i<length:
        try:
            if '.' in tokens[i]:
                tokens[i]=float(tokens[i])
                i+=1
                continue
            if re.match("^[0-9]+$",tokens[i]):
                tokens[i]=int(tokens[i])
                i+=1
                continue
            if tokens[i] not in operators and tokens[i] not in paranthesis:
                tokens[i]=values[variables.index(tokens[i])]
        except ValueError:
            print "Unassigned variable "+tokens[i]
            return 'n'
        i+=1

    while '(' in tokens:
        try:
            index_right=tokens.index(')')
            index_left=tokens[::-1].index('(')
            index_left=len(tokens)-index_left
            print index_left
            print index_right
            val=calculate(tokens[index_left:index_right])
            tokens[index_right]=val
            del tokens[index_left-1:index_right]
            #print tokens

        except Exception:
            return calculate(tokens)
    return calculate(tokens)


def evaluate(expr):

    STRING = 1
    tokens=list(token[STRING] for token
         in generate_tokens(StringIO(expr).readline)
         if token[STRING])
    #print tokens
    if '=' in tokens:
        index_equals=tokens.index('=')
        if index_equals==1:
            val=assignment(tokens[2:])
            if val!='n':
                try:
                    index=variables.index(tokens[0])
                    values[index]=val
                except Exception:
                    variables.append(tokens[0])
                    values.append(val)
        else:
            i=0
            while i<variables.index(tokens[0]):
                values[variables.index(tokens[i])]=calculate(tokens[1])
    elif tokens[1] in ['+=','-=','*=','/=']:
        val=assignment(tokens[2:])
        if val!='n':
            try:
                if tokens[1]=='+=':
                    val+=values[variables.index(tokens[0])]
                if tokens[1]=='-=':
                    val-=values[variables.index(tokens[0])]
                if tokens[1]=='*=':
                    val*=values[variables.index(tokens[0])]
                if tokens[1]=='/=':
                    val/=values[variables.index(tokens[0])]
            except Exception:
                print "Unassigned variable "+tokens[0]
            try:
                index=variables.index(tokens[0])
                values[index]=val
            except Exception:
                variables.append(tokens[0])
                values.append(val)

    else:
        print assignment(tokens)
    display()




def validity(expr):

    if simple_assi.search(expr) or compound_assi.search(expr) or numeric_assi.search(expr) or vari.search(expr) or parallel_assi.search(expr) :
        return 1
    else:
        return -1


def readexper():
    regex()
    while True:
        expr=raw_input("Enter Input")
        if expr in key_words:
            print "It is a keyword"
            continue
        start=time.clock()
        #valid=validity(expr)
        valid=1
        if valid==1:
            expr=expr.replace(" ","")
            evaluate(expr)
        else:
            print "Invalid expression"
        print time.clock()-start
readexper()
