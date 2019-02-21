import numpy as np
import cmath

class Register:
    def __init__(self, size, values=None):
        if size < 1 or size > 15:
            print("The number of qubits must be between 1 and 15.")
            exit()  # Quits the program due to a bad input
        self.vector = np.zeros((2**size,), dtype=complex)  # creates and zero array with a size of 2 to the power of m
        if values is not None and len(values) == len(self.vector):
            for i in range(0, 2**size):
                self.vector[i] = values[i]
        print(self.vector)

    def inner_product(self, other_vector:np.array):
        sum = complex(0,0)  # initializes the sum as a complex number
        if len(other_vector) != len(self.vector):
            print("The registers aren't the same size.")
        else:
            for i in range(0, len(self.vector)):
                sum = sum + (self.vector[i]*other_vector[i])
        print(sum)
        return sum

    def norm(self):
        return self.inner_product(self.vector)


class Operator:
    def __init__(self, size, values=None):
        if size < 1:
            print("The number of qubits must be greater than 1.")
            exit()  # Quits the program due to a bad input
        if values is None:
            values = np.zeros(shape=(2**size, 2**size), dtype=complex)
            for i in range(0, size):
                values[i][i] = 1
        print(values)


# register_min = Register(1)  # Tests the minimum size of the register
# register_max = Register(15)  # Tests the maximum size of the register
# register_above_max = Register(16)  # Tests above the max register
# register_below+min = Register(0)  # Tests below the min register
# register_zero = Register(2)  # Initializes an empty register

# v1 = np.ones(4)
# v2 = np.array([complex(1,2), complex(2,3), complex(0,0), complex(1,1)])
# register_one = Register(2, v1)
# register_two = Register(2, v2)
# register_one.inner_product(register_two.vector)
# register_two.inner_product(register_one.vector)
# register_one.norm()
# register_two.norm()

operator_zero = Operator(2)
v3 = np.ones(shape=(4, 4), dtype=complex)
operator_one = Operator(2, v3)
