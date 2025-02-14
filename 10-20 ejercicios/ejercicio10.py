#Leer, escribir y modificar un archivo de texto
path = "C:/Users/ximem/OneDrive/Desktop/"
name = "miarchivo"
ext= "txt" 


   
#Modificar el archivo
with open(path+name+ "." +ext, "w", encoding="utf8") as miarchivo:
    print("Prueba 5, prueba 9", file=miarchivo)
   

#Agregar
with open(path+name+ "." +ext, "a", encoding="utf8") as miarchivo:
    print("Prueba 6", file=miarchivo)   
    

#leer 
with open(path+name+ "." +ext, "r", encoding="utf8") as miarchivo:
    for line in miarchivo.readlines():
         line.replace("\n", "")
         print (line, end="", )
         

