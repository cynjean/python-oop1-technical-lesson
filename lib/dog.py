# Dog model goes here
# Build the class 
class Dog:
    #Initialize Instance Properties
    def __init__(self, name, breed, age, last_checkup = None):
        self.name = name #Instance property
        self.breed = breed #Instance property
        self.age = age #Instance property
        self.last_checkup = last_checkup #Instance property for the last checkup date. If the user puts nothing in for last_checkup, it will default to None. 

    #Create instance methods 
    def checkup(self, date):
        print(f"Checking up with {self.name} on {date}")
        self.last_checkup = date

    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age}")

    # Getters and setters
    # fido.age
    def get_age(self):
        return self._age 

    # fido.age = 10
    def set_age(self, value):
        if type(value) is int and 0 <= value:
            self._age = value
        else:
            print("Not valid age")

    age = property(get_age, set_age)
    
# Create and use instances of the class
# Create dogs
fido = Dog("Fido","Golden Retriever", 3, "05/22/2022")
clifford = Dog(
    name = "Clifford",
    age = 2, 
    breed = "Big Red"
)

# Use the instances
# print(fido.age) # 3
# fido.birthday_celebration()
# print(fido.age) # 4
# print(clifford.last_checkup) # None
# clifford.checkup("03/02/2024")
# print(clifford.last_checkup) # 03/02/2024

# Test instance properties 
#balto = Dog("Balto", "Husky", "Not an age") # Output: Not a valid age, not a integer
#steele = Dog("Steele", "Husky", -10) # Output: Not a valid age, not more than 0

    