
a = 2
b = 8
c = 3


delta = b**2 - 4*a*c


if delta > 0:

    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("O primeiro zero da função quadrática é:", x1)
    print("O segundo zero da função quadrática é:", x2)
elif delta == 0:
   
    x = -b / (2*a)
    print("A única raiz da função quadrática é:", x)
else:
 
    print("A equação quadrática não possui raízes reais.")

