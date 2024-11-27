# Base Class: smartPhone
class smartPhone:
    def __init__(self, name, processor, batteryHealth, secret_identity):
        self.name = name
        self.processor = processor
        self.batteryHealth = batteryHealth
        self.__secret_identity = secret_identity  # Encapsulated attribute

    def use_processor(self):
        print(f"{self.name} uses {self.processor} with a battey level of {self.batteryHealth}!")

    def reveal_identity(self):
        print(f"{self.name}'s secret identity is {self.__secret_identity}.")

# Subclass: flagShip (inherits from smartPhone)
class flagShip(smartPhone):
    def __init__(self, name, processor, batteryHealth, secret_identity, model):
        super().__init__(name, processor, batteryHealth, secret_identity)
        self.model = model

    def use_processor(self):
        print(f"{self.name} uses {self.processor} while clocking at {self.model} Mhz!")

# Subclass: baseModel (inherits from smartPhone)
class baseModel(smartPhone):
    def __init__(self, name, processor, batteryHealth, secret_identity, gpu):
        super().__init__(name, processor, batteryHealth, secret_identity)
        self.gpu = gpu

    def use_processor(self):
        print(f"{self.name} uses {self.processor} with a dual graphics card of {self.gpu}!")

# Example Usage
hero1 = flagShip("Alienware", "core i9", 80, "Dell", 300)
hero2 = baseModel("Omen", "ryzen 9", 70, "Lara Night", "nvidia")

hero1.use_processor()
hero2.use_processor()

hero1.reveal_identity()
