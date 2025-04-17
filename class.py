
class Superhero:
    def __init__(self, name, power, city):  
        self.__name = name
        self.__power = power
        self.__city = city

    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__power

    def get_city(self):
        return self.__city

    def set_power(self, power):
        self.__power = power

    def set_city(self, city):
        self.__city = city

    def show_info(self):
        print(f"{self.__name} protects {self.__city} with the power of {self.__power}.")

    def fight_crime(self):
        print(f"{self.__name} uses {self.__power} to fight crime in {self.__city}!")

class Speedster(Superhero):
    def __init__(self, name, city, speed_level):
        super().__init__(name, "Super Speed", city)
        self.__speed_level = speed_level

    def get_speed_level(self):
        return self.__speed_level

    def set_speed_level(self, level):
        self.__speed_level = level

    def fight_crime(self):  
        print(f"{self.get_name()} dashes through {self.get_city()} at speed level {self.__speed_level} to stop villains in a flash!")

hero = Superhero("Night Flame", "Fire Manipulation", "Nairobi")
hero.show_info()
hero.fight_crime()

print("")

flash = Speedster("Velocity", "Mombasa", 8)
flash.show_info()
flash.fight_crime()
