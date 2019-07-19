from dataclasses import dataclass
@dataclass
class Pet:
    name: str
    age: int

print(Pet('Patch', 5))
print(Pet(5, 'Patch'))
