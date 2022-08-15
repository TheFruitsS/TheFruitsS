#Instances example is Person.specific_name
class Person:
    specific_name = 'Special'

    def __init__(self):
        self.specific_name = 'Violeta'

print(Person.specific_name)
love = Person()
print(love.specific_name)
#kogato sazdavame obekt vinagi tarsi parvo po instanciqta ot metoda