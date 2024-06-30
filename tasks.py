import math
def answer(a,b,c):
    print("equation is:"+a+"x^2+"+b+"x+"+c)
    def root(a,b,c):
        a= float(a)
        b= float(b)
        c= float(c)
        delta= (b**2)-4*a*c
        if delta>0:
            root1=(-b+math.sqrt(delta))/2*a
            root2=(-b-math.sqrt(delta))/2*a
        if delta==0:
            root1=-b/2*a
        if delta<0: #for complex roots
            root1=complex(-b/2*a,math.sqrt(abs(delta))/2*a)
            root2=complex(-b/2*a,-math.sqrt(abs(delta))/2*a)
        print("roots: "+str(root1)+" and "+str(root2))
    root(a,b,c)    
a=input("enter a: ")
b=input("enter b: ")
c=input("enter c: ")
answer(a,b,c)
