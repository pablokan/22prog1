a = open("nuevos_nombres.txt", "w", encoding="utf-8") # abre el archivo en modo escritura
print(f"Posición del puntero: {a.tell()}") 
a.write("Iñaki\n") # escribe en el archivo
a.close() # cierra el archivo

a = open("nuevos_nombres.txt", "a", encoding="utf-8")
print(f"Posición del puntero: {a.tell()}") 
a.write("María\n")
a.writelines(["Juan\n", "Pedro\n"])
a.close()




