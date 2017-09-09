def balance(num):
    l=list(num)
    stack=[]
    for x in l:
        if (x=='{') or (x=='[') or (x=='('):
            stack.append(x)
        else:
            if stack[-1]!=x:
                return False
            else:
                stack=stack[:-1]
    if stack==[]:
        return True
            