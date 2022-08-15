class Numbers:
    phone_number = '+074'

    def __init__(self, num_a, num_b):
        self.value = 33
        self.num_a = num_a
        self.num_b = num_b

    @classmethod
    def phone_data(cls):
        return cls.phone_number


sums = Numbers(30, 33)
print(sums.phone_data())