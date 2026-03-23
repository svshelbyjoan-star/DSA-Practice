def evaluvate_postfix(expression):
    stack=[]
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b=stack.pop()
            a=stack.pop()

            if token=='+':
                stack.append(a+b)
            elif token=='-':
                stack.append(a-b)
            elif token=='*':
                stack.append(a*b)
            elif token=='/':
                stack.append(a//b)


            elif token=='and':
                stack.append(a and b)
            elif token=='or':
                stack.append(a or b)



            elif token=='>':
                stack.append(a>b)
            elif token=='<':
                stack.append(a<b)
            elif token =='==':
                stack.append(a==b)
            elif token=='>=':
                stack.append(a>=b)
            elif token=='<=':
                stack.append(a<=b)

                
    return stack.pop()
expr = "2 3 and"
print("Postfix Result:", evaluvate_postfix(expr))

