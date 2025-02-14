#problema 10


#Leer, escribir y modificar un archivo de texto

#Abrir un archivo en modo lectura

path = "C:/Users/ximem/OneDrive/Desktop/"
name = "miarchivo"
ext= "txt"

with open(path+name+ "." +ext, "r", encoding="utf8") as miarchivo:
    for line in miarchivo.readlines():
        # line.replace("\n", "")
         #print (line, end="", sep="")
         print(line)


#with open(path+name+ "." +ext, "a", encoding="utf8") as miarchivo:
 #   print("Prueba 2.1", file=miarchivo)

#with open(path+name+ "." +ext, "r", encoding="utf8") as miarchivo:
 #   for line in miarchivo.readlines():
  #       line.replace("\n", "")
   #      print (line, end="", sep="")
    #     print(line)