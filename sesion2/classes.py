class Person:
    def __init__(self):
        self.name = "John"
        self.age = 36
        self.country = "USA"
        address = "njaghasjkh"

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

if __name__ == "__main__":
    print()