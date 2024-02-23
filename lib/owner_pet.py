class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        if pet_type not in self.PET_TYPES:
            raise Exception("You have to pick the correct PET_TYPE")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self.owner_pets = []

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("The argument must be of type Pet")
        pet.owner = self
        self.owner_pets.append(pet)

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets

