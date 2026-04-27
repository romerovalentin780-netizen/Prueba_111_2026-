edad_minima = 19

edad= int(input("colocar edad: "))
categoria= input("colocar categoria: A, B, C, D: ")
                       #or #and    
if edad >= edad_minima and (categoria == "D" or categoria == "d"):
    print("cheto mal")
else:
    print("Vo no pode")