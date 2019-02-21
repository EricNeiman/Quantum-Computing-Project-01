import numpy as np

class Register:
    def __init__(self, m, k, infoBit):
        # m is the dimensionality of the vector
        # k is the location of the information bit
        if m < 1 | m > 15:
            print("The number of qubits must be between 1 and 15.")
            quit()  # Quits the program due to a bad input
        self.vector = np.zeros((2**m,), dtype=int)  # creates and zero array with a size of 2 to the power of m
        print(self.vector)

# class Operator:
#     def __init__(self):

register = Register(2, 0, 0)