# Preguntar nombre, carrera en la que se inscribe y ciudad donde vive
# un ingresante al Instituto. Los estudiantes de la carrera de
# Electromecánica y que no viven en Río Cuarto tendrán un
# 15% de descuento en la cuota que es de $4500.
# Mostrar nombre, ciudad, carrera y monto final de la cuota.

nombre = input("Nombre: ")
carrera = input("Carrera: ")
ciudad = input("Ciudad: ")

cuota = 7000
if carrera == "Electromecánica" and ciudad != "Río Cuarto":
    cuota = cuota * 0.85

print(nombre, "paga una cuota de", cuota, "pesos")
