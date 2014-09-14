def push_stack(stackArr,ele):
    stackArr.append(str(ele))

def pop_stack(stackArr):
    return stackArr.pop()


def isOperand(opr):
    if(not(isOperator(opr)) and (opr != "(") and (opr != ")")):
        return 1
    return 0

def isOperator(opr):
    if(opr == "+" or opr == "-" or opr == "*" or opr == "/" or opr == "^"):
        return 1
    return 0

def topStack(stackArr):
    return(stackArr[len(stackArr)-1])

def isEmpty(stackArr):
    if(len(stackArr) == 0):
        return 1
    return 0

def strToTokens(str):
    strArr = []
    strArr = str
    tempStr = ''
    tokens = []
    tokens_index = 0
    count = 0
    for x in strArr:
        count = count+1
        if(isOperand(x)):
            tempStr += x
        if(isOperator(x) or x == ")" or x == "("):
            if(tempStr != ""):
                tokens.append(tempStr)
                tokens_index = tokens_index+1
            tempStr = ''
            tokens.append(x)
            tokens_index = tokens_index+1
        if(count == len(strArr)):
            if(tempStr != ''):
                tokens.append(tempStr)
    return(tokens)

def prcd(opr):
    if(opr == "^"):return(5)
    if((opr == "*") or (opr == "/")):return(4)
    if((opr == "+") or (opr == "-")):return(3)
    if(opr == "("):return(2)
    if(opr == ")"):return(1)

def ip(infixStr, postfixStr = [],retType = 0):
    postfixStr = []
    stackArr = []
    postfixPtr = 0
    tempStr = infixStr
    infixStr = []
    infixStr = strToTokens(tempStr)
    for x in infixStr:
        if(isOperand(x)):
            postfixStr.append(x)
            postfixStr.append(',')
            postfixPtr = postfixPtr+1
        if(isOperator(x)):
            if(x != "^"):
                while((not(isEmpty(stackArr))) and (prcd(x) <= prcd(topStack(stackArr)))):
                    postfixStr.append(topStack(stackArr))
                    postfixStr.append(',')
                    pop_stack(stackArr)
                    postfixPtr = postfixPtr+1
            else:
                while((not(isEmpty(stackArr))) and (prcd(x) < prcd(topStack(stackArr)))):
                    postfixStr.append(topStack(stackArr))
                    postfixStr.append(',')
                    pop_stack(stackArr)
                    postfixPtr = postfixPtr+1
            push_stack(stackArr,x)
        if(x == "("):
                push_stack(stackArr,x)                
        if(x == ")"):
            while(topStack(stackArr) != "("):
                postfixStr.append(pop_stack(stackArr))
                postfixStr.append(',')
                postfixPtr = postfixPtr+1
            pop_stack(stackArr)
            
    while(not(isEmpty(stackArr))):
        if(topStack(stackArr) == "("):
            pop_stack(stackArr)
        else:
            postfixStr.append(pop_stack(stackArr))
            postfixStr.append(',')

    returnVal = ''
    for x in postfixStr:
        returnVal += x

    if(retType == 0):
        return(returnVal)
    else:
        return(postfixStr)

def eval1(postfix):
    exp=ip(infixStr)
    res_list=[]
    res=exp.split(',')
    for each in res:

        if each.isdigit(): #or each.isalpha():
            res_list.append(each)

        if each=='+':
              first=res_list.pop()
              second=res_list.pop()
              res_list.append(int(first)+int(second))
        elif each=='-':
              first=res_list.pop()
              second=res_list.pop()
              res_list.append(int(second)-int(first))
        elif each=='*':
              first=res_list.pop()
              second=res_list.pop()

              res_list.append(int(first)*int(second))
        elif each=='/':
              first=res_list.pop()
              second=res_list.pop()
              res_list.append(int(second)/int(first))
        elif each=='^':
            first=res_list.pop()
            second=res_list.pop()
            res_list.append(int(second)**int(first))
    if len(res_list)==1:
     print res_list.pop()


run = True

while run:
    print "Choose an option:"

    print "0: Evaluate"
    print "1: Exit"

    choice = raw_input()

    if choice == "1":
        print "Exit!"
        run = False
    elif choice == "0":
        infixStr="12+2^3+(2-3+(1-2))"
        print eval1(infixStr)
    else:
        print "Please choose a valid option."
        print "\n"
