from dataclasses import dataclass, field

@dataclass
class Persona:
    nombre: str
    edad: int


@dataclass
class Profesor(Persona):
    materia: str


profe = Profesor("Pablo", 44, "Matemática")
print(profe)

import datetime
now = datetime.datetime.now()
print(now.__str__()) # 2022-09-12 15:53:05.952940
print(now.__repr__()) # 'datetime.datetime(2020, 12, 27, 22, 28, 0, 324317)'


@dataclass
class Country:
     name: str
     population: int
     continent: str = field(repr=False) # omits the field
     official_lang: str

smallestEurope = Country("Monaco", 37623, "Europe", "French")

print(smallestEurope)

# Country(name='Monaco', population=37623, official_lang='French') 

@dataclass
class Country:
     name: str
     population: int  
     continent: str
     official_lang: str = field(init=False, repr=False) #Do not pass in this attribute in the constructor argument  


smallestEurope = Country("Monaco", 37623, "Europe")

print(smallestEurope)

@dataclass
class Country:
     name: str
     population: int  
     continent: str
     #official_lang: str = field(default="English") # If you ommit value, English will be used
     official_language: str = "English"


smallestEurope = Country("Monaco", 37623, "Europe") #Omitted, so English is used

print(smallestEurope)


