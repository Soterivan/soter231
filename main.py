class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50  # 0 - ситий, 100 - дуже голодний
        self.energy = 50  # 0 - втомлений, 100 - повний сил
        self.happiness = 50  # 0 - сумний, 100 - дуже щасливий

    def feed(self):
        if self.hunger > 10:
            self.hunger -= 10
            self.happiness += 5
            print(f"{self.name} смачно поїв!")
        else:
            print(f"{self.name} не голодний.")

    def play(self):
        if self.energy > 10:
            self.happiness += 10
            self.energy -= 10
            self.hunger += 5
            print(f"{self.name} грається і веселий!")
        else:
            print(f"{self.name} занадто втомлений, щоб гратися.")

    def sleep(self):
        if self.energy < 90:
            self.energy += 20
            self.hunger += 10
            print(f"{self.name} добре виспався.")
        else:
            print(f"{self.name} не хоче спати зараз.")

    def status(self):
        print(f"Статус {self.name}:")
        print(f"  Голод: {self.hunger}/100")
        print(f"  Енергія: {self.energy}/100")
        print(f"  Щастя: {self.happiness}/100")
        if self.hunger >= 80:
            print(f"{self.name} дуже голодний!")
        if self.energy <= 20:
            print(f"{self.name} дуже втомлений!")
        if self.happiness <= 20:
            print(f"{self.name} сумний.")


# Приклад використання
my_pet = Pet(name="Бобик", species="собака")

my_pet.status()
my_pet.feed()
my_pet.play()
my_pet.sleep()
my_pet.status()
