operators=['+', '-', '*', '/', '(', ')', '^']
priority={'+':1, '-':1, '*':2, '/':2, '^':3} 
stack=[]
postfix='' 
infix=input('Enter infix expression: ')    
for i in infix:
    if i not in operators:
        postfix+=i
    elif i=='(':
        stack.append('(')
    elif i==')':
        while stack and stack[-1]!= '(':
            postfix+=stack.pop()
        stack.pop()
    else:     
        while stack and stack[-1]!='(' and priority[i]<=priority[stack[-1]]:
            postfix+=stack.pop()
        stack.append(i)
while stack:
    postfix+=stack.pop()
print('Postfix expression: ',postfix)
