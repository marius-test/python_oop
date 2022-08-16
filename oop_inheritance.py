class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old.")
    
    def hello(self):
        print("Hello!")
    

class Male(Human):
    def hello(self):
        print('How You Doing?')
        

class Female(Human):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def hello(self):
        print('Hi!')
        
    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old and my hair is {self.color}.")
        
        
human_1 = Human('Marius', 29)
human_1.hello()
human_1.introduce()

male_1 = Male('Paul', 28)
male_1.hello()
male_1.introduce()

female_1 = Female('Melanie', 24, 'brown')
female_1.hello()
female_1.introduce()
