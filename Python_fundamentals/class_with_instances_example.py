class Numbers:
    def __init__(self, num_a, num_b):
        self.value = 33
        self.num_a = num_a
        self.num_b = num_b

    def sum_numbers(self):
        return self.value + self.num_a + self.num_b


sums = Numbers(30, 33)
print(sums.sum_numbers())