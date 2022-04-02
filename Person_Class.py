class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"My name is {self.name}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


Ashish = Person("Ashish Gupta")
Ashish.talk()

Bob = Person("Bob Vanced")
Bob.sleep()
