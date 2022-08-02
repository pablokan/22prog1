from input_choice import inputChoice
from input_menu import inputMenu

pais = inputChoice("Argentina/Namibia/Irlanda", "Elija un país")
print(f"El país elegido fue {pais}")
print("====================================")
pais = inputMenu("Argentina/Namibia/Irlanda", "Elija un país")
print(f"El país elegido fue {pais}")


