from dataclasses import dataclass, field

@dataclass(order=True)
class Country:
    sort_index: int = field(init=False)
    name: str
    population: int = field(repr=True)
    continent: str 
    official_lang: str = field(default="English")
     

    def __post_init__(self):
        self.sort_index = self.population

smallestEurope = Country("Monaco", 37623, "Europe")
smallestAsia= Country("Maldives", 552595, "Asia")
smallestAfrica= Country("Gambia", 2521126, "Africa") 

print(smallestAsia < smallestAfrica) # True
print(smallestAsia > smallestAfrica) # False
print(max(smallestAfrica, smallestAsia, smallestEurope))