def alumno(nombre, ciudad="Río Cuarto", **kwargs):
    print(f"El alumno {nombre} es de {ciudad}")
    if kwargs != {}:
        print("Otra data:")
        for k, v in kwargs.items():
            print(f"{k}: {v}")

alumno("Juan", "San Basilio")
alumno("Pipo")
alumno("Anita", "Jovita", Observaciones="abanderada")