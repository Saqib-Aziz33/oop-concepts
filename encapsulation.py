# Encapsulation is the bundling of data (attributes) and methods (functions) within a class,
# restricting access to some components to control interactions.
# A class is an example of encapsulation as it encapsulates all the data that is member functions,
# variables, etc.

# Types of Encapsulation:
# Public Members: Accessible from anywhere.
# Protected Members: Accessible within the class and its subclasses.
# Private Members: Accessible only within the class.

class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())
