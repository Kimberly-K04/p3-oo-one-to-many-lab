class Owner:
    all = []

    def __init__(self, name):
        self.name = name
        Owner.all.append(self)

    def pets(self):
        """Return a list of Pet instances that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to the pet."""
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """Return this owner's pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type

        self.owner = None
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an Owner instance")
            owner.add_pet(self)  # link pet to owner properly

        Pet.all.append(self)
                                        