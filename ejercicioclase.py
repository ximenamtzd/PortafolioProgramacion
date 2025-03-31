#Fngeneral

def funciongeneral(a,b,c):
    discri=b**2-4*a*c

    if discri>0:
        raiz_discri=(discri)**(1/2)
        x1=(-b+raiz_discri)/(2*a)
        x2=(-b-raiz_discri)/(2*a)
        return x1, x2
    
    if discri ==0:
      x3=(-b)/(2*a)
      return x3
    
    if discri<0:
       d=(discri*0-1j)
       


    a=float(input("Ingrese el valor de a:"))
    b=float(input("Ingrese el valor de b:"))
    c=float(input("Ingrese el valor de c:"))
