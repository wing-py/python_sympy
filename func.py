from sympy import *
a,b,c,d=symbols("a b c d")
def bo(x):
    if x==True:
        return 1
    else:
        return 0
def pinglian():
    s=0
    while True:
        x=str(input())
        if x=="finish":
            if s==0:
                return "have exit"
            else:
                return 1/s
        else:
            x=float(x)
            s+=(1/x)
def totable(expr,n):
    expr=simplify(expr)#expr为字符串
    for i in range(2):    
        expr1=expr.subs(a,i)
        if n==1:
            print(i,expr1)
            continue
        for j in range(2):
            expr2=expr1.subs(b,j)
            if n==2:
                print(i,j,expr2)
                continue
            for k in range(2):
                expr3=expr2.subs(c,k)
                if n==3:
                    print(i,j,k,expr3)
                    continue
                for m in range(2):
                    expr4=expr3.subs(d,m)
                    if n==4:
                        print(i,j,k,m,bo(expr4))
                

       
    
    
