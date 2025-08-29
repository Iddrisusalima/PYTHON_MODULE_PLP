# Activity 1: Smartphone Class with Inheritance

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
    
    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}... 📞")
    
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"Battery charged to {self.battery}% 🔋")
    
    def phone_info(self):
        print(f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%")

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu_power):
        super().__init__(brand, model, storage, battery)
        self.gpu_power = gpu_power
    
    def play_game(self, game):
        if self.battery > 20:
            print(f"Playing {game} 🎮 with {self.gpu_power} GPU power!")
            self.battery -= 20
        else:
            print("Battery too low to play games! ⚠️")

# ---------- TEST OBJECTS ----------
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 80)
phone1.phone_info()
phone1.make_call("123-456-7890")
phone1.charge(15)

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 512, 50, "Ultra RTX")
gaming_phone.phone_info()
gaming_phone.play_game("PUBG")
gaming_phone.charge(30)

# ---------------- Activity 2 ----------------
# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bike(Vehicle):
    def move(self):
        print("Cycling 🚴")

# ---------- TEST OBJECTS ----------
vehicles = [Car(), Plane(), Bike()]

for v in vehicles:
    v.move()
