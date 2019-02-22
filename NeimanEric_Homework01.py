import numpy as np
import cmath

class Register:
    def __init__(self, size, values=None):
        # This method creates a vector of qubits with and takes an optional array of complex values
        if size < 1 or size > 15:
            print("The number of qubits must be between 1 and 15.")
            return
        self.vector = np.zeros((2**size,), dtype=complex)
        if values is not None and len(values) == len(self.vector):
            for i in range(0, 2**size):
                self.vector[i] = values[i]
        # print(self.vector)  # Printout for testing

    def inner_product(self, other_vector:np.array):
        # This method takes
        sum = complex(0,0)  # initializes the sum as a complex number
        if len(other_vector) != len(self.vector):
            print("The registers aren't the same size.")
        else:
            for i in range(0, len(self.vector)):
                sum = sum + (self.vector[i]*other_vector[i])
        # print(sum)  # Printout for testing
        return sum

    def norm(self):
        return self.inner_product(self.vector)


class Operator:
    def __init__(self, size, values=None):
        # This method creates the operator and takes an optional 2d array of complex values and creates a matrix
        if size < 1:
            print("The number of qubits must be greater than 1.")
            return  # Quits the program due to a bad input
        self.matrix = np.zeros(shape=(2 ** size, 2 ** size), dtype=complex)
        if values is None:
            for i in range(0, size):
                self.matrix[i][i] = 1  # initializes values as the identity matrix
        else:
            self.matrix = values
        # print(self.matrix)  # Printout for testing

    def outer_product_initialization(self, vector1, vector2):
        # This method takes in two vectors and sets this operator's matrix equal to their outer product
        if len(vector1) != len(vector2):
            print("The vectors must be the same size for operator initialization using the outer product")
            return
        for i in range(0, len(vector1)):
            for j in range(0, len(vector2)):
                self.matrix[i][j] = vector1[i] * vector2[j]
        # print(self.matrix)  # Printout for testing

    def add_operators(self, alpha, matrix2, beta):
        # This method takes in an alpha, a second matrix and a beta
        # It then multiplies this operator's matrix by alpha and adds matrix2 multiplied by beta to it
        # Then it sets this operator's matrix to the result of the calculation
        resulting_matrix = np.ones(shape=(len(self.matrix), len(self.matrix)), dtype=complex)
        for i in range(0, len(self.matrix[0])):
            for j in range(0, len(self.matrix)):
                resulting_matrix[i][j] = alpha * self.matrix[i][j] + matrix2[i][j] * beta
        # print(resulting_matrix)  # Printout for testing
        self.matrix = resulting_matrix

    def transform_register(self, register):
        vector = register.vector
        row_sum = 0
        if len(vector) != len(self.matrix[0]):
            print("The operator cannot operate on a register of this sise")
            return
        for i in range(0, len(self.matrix[0])):
            for j in range(0, len(self.matrix)):
                row_sum += vector[j] * self.matrix[i][j]
            register.vector[i] = row_sum
            row_sum = 0
        print(register.vector)  # Printout for testing


# All calls used to test the functionality below

# register_min = Register(1)  # Tests the minimum size of the register
# register_max = Register(15)  # Tests the maximum size of the register
# register_above_max = Register(16)  # Tests above the max register
# register_below_min = Register(0)  # Tests below the min register
# register_zero = Register(2)  # Initializes an empty register

v1 = np.ones(4)
v2 = np.array([complex(1, 2), complex(2, 3), complex(0, 0), complex(1, 1)])
register_one = Register(2, v1)
register_two = Register(2, v2)
print("Printing registers one and two: ", register_one.vector, register_two.vector)
print("Printing the inner product of registers one and two: ", register_one.inner_product(register_two.vector))  # Tests the inner product functionality
print("Printing the norm of register one:", register_one.norm())

operator_identity = Operator(2)
print("Printing the an identity matrix: ", operator_identity.matrix)
v3 = np.ones(shape=(4, 4), dtype=complex)
operator_one = Operator(2, v3)

# operator_one.outer_product_initialization(register_one.vector, register_two.vector)

alpha = complex(1, 0)
beta = complex(2, 1)
operator_two = Operator(2, v3)
operator_three = Operator(2, v3)
operator_two.add_operators(alpha, operator_three.matrix, beta)


