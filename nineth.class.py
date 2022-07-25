from codecs import BufferedIncrementalDecoder
from distutils.log import error


class Dog():

    num_of_limb = 4

    def __init__(self, breed: str, color: str, weight: int):
        self.breed = breed
        self.color = color
        self.weight = weight
        pass

    def __str__(self):
        return (f'the dog is {self.breed}')# to call the dog1 variable cos a variable cannot hold an object  
    
    def __add__(self,other):
        
        if isinstance(other,Dog):
            return self.weight + other.weight

        raise TypeError ('expected type of Dog but got %s' %type(other))

    def run(self):
        return f'the dog with {self.weight}kg is running '


dog1 = Dog('bull dog','black and white',25)
dog2 = Dog('bull dog','white',55)
print(dog1.run())
# print(dog1)
# print(dog1.breed, dog1.color)




# print(Dog.num_of_limb)

print(dog1 + dog2)